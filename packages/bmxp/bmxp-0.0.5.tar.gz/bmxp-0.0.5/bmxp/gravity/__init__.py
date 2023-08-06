"""
Gravity clusters LCMS datasets by RT and Correlation
"""
import logging
import math
import pandas as pd
import networkx as nx
from ctypes import CDLL, c_double, c_uint32
import os
import platform
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
if platform.system() == "Windows":
    correlation = CDLL(os.path.join(dir_path, "correlation.dll"))
else:
    correlation = CDLL(os.path.join(dir_path, "correlation.so"))

c_array = np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS")

correlation.pearson.argtypes = [c_array, c_array, c_uint32]
correlation.pearson.restype = c_double
# experimental masked-type
correlation.pearson_m.argtypes = [c_array, c_array, c_uint32]
correlation.pearson_m.restype = c_double
correlation.spearman.argtypes = [c_array, c_array, c_uint32]
correlation.spearman.restype = c_double

correlation.removeNans.argtypes = [c_array, c_array, c_uint32]
correlation.removeNans.restype = c_uint32

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

__version__ = "0.0.2"
ECLIPSE_COLUMNS = [
    "RT",
    "MZ",
    "Intensity",
    "Non_Quant",
    "Compound_ID",
    "Adduct",
    "Annotation_ID",
    "Metabolite",
    "Cluster_Num",
    "Cluster_Size",
]


def pearson_m(x, y):
    return correlation.pearson_m(x, y, len(x))


def pearson(x, y):
    return correlation.pearson(x, y, len(x))


def spearman(x, y):
    return correlation.spearman(x, y, len(x))


def deconvolute(df_index, graph):
    cluster_df = pd.DataFrame({"Cluster_Num": None, "Cluster_Size": 1}, index=df_index)
    i = 0
    while True:
        # delete singletons
        graph.remove_nodes_from(list(nx.isolates(graph)))

        # find largest cliques
        # find the largest cliques
        cliques = []
        max_size = 0
        for clique in nx.find_cliques(graph):
            if len(clique) > max_size:
                max_size = len(clique)
                cliques = [[set(clique), 0]]
            elif len(clique) == max_size:
                cliques.append([set(clique), 0])
        if not cliques:
            break

        for clique in cliques:
            clique_graph = graph.subgraph(clique[0])
            temp = 0
            for edge in clique_graph.edges(data=True):
                temp += edge[2]["coor"]
            clique[1] = temp
        cliques.sort(key=lambda x: x[1], reverse=True)

        to_remove = set()
        while len(cliques) > 0:
            # add the best one
            best_clique = cliques[0]
            features = list(best_clique[0])
            cluster_df.loc[features, "Cluster_Num"] = i
            cluster_df.loc[features, "Cluster_Size"] = max_size
            if i % 50 == 0:
                LOGGER.info(f"On cluster {i}, which contains {max_size} features.")
            i += 1

            # search the clique for ones to remove
            cliques = [
                clique
                for clique in cliques
                if not clique[0].intersection(best_clique[0])
            ]
            # add to our "to remove" queue
            to_remove.update(best_clique[0])
        graph.remove_nodes_from(to_remove)
        if max_size == 2:
            break
    return cluster_df


# new
def by_corr(batch_a, batch_b, rt_series, corr_value, rt_thresh, method):
    if method == "Spearman":
        batch_a = batch_a.rank(na_option="top")
        batch_b = batch_b.rank(na_option="top")
    a_zs = batch_a - batch_a.mean()
    b_zs = batch_b - batch_b.mean()
    corr = (
        a_zs.T.dot(b_zs)
        .div(len(batch_a))
        .div(b_zs.std(ddof=0))
        .div(a_zs.std(ddof=0), axis=0)
    )
    links = corr.stack().reset_index()
    links.columns = ["var1", "var2", "Correlation"]
    links = links.loc[
        (links["Correlation"] > corr_value) & (links["var1"] != links["var2"])
    ]
    links["RT_diff"] = rt_series[links["var1"]].values - rt_series[links["var2"]].values
    links["RT_diff"] = links["RT_diff"].abs()
    return links.loc[(links["RT_diff"] < rt_thresh)]


# old
def by_rt(i, j, rt_series, df, corr_value, rt_thresh, method, nan_policy):

    # rt_matrix = batch_a.apply(lambda x: batch_b - x)
    np_batch_a = rt_series.iloc[i[0] : i[1]].values
    np_batch_b = rt_series.iloc[j[0] : j[1]].values
    rt_flattened = np.absolute(np.subtract.outer(np_batch_b, np_batch_a)).flatten()
    a_index = np.tile(np.fromiter(range(i[0], i[1]), int), (j[1] - j[0]))
    b_index = np.tile(np.fromiter(range(j[0], j[1]), int), ((i[1] - i[0]), 1)).flatten(
        order="F"
    )
    to_keep = (rt_flattened <= rt_thresh) & (a_index != b_index)
    # rt_flattened = rt_flattened[to_keep]
    a_index = a_index[to_keep]
    b_index = b_index[to_keep]
    corr_results = np.empty(len(a_index))
    values = df.values
    for k in range(len(a_index)):
        a_val = a_index[k]
        b_val = b_index[k]

        corr1 = values[:, a_val].copy()
        corr2 = values[:, b_val].copy()
        # corr_df = np.stack([corr1, corr2])

        if nan_policy == "backfill":
            pass
            # fill var1
            corr_df = np.nan_to_num(corr_df)

            total_zeroes = len(corr_df[0]) - np.count_nonzero(corr_df[0])
            num_to_be_filled = min(len(corr_df[0]) - total_zeroes, total_zeroes)
            if num_to_be_filled > 0:
                fill_values = list(range(-num_to_be_filled, 0))
                sorted_index = np.lexsort((corr_df[1], corr_df[0]))
                index_to_fill = sorted_index[
                    total_zeroes - num_to_be_filled : total_zeroes
                ]
                corr_df[0][index_to_fill] = fill_values

            total_zeroes = len(corr_df[1]) - np.count_nonzero(corr_df[1])
            num_to_be_filled = min(len(corr_df[1]) - total_zeroes, total_zeroes)
            if num_to_be_filled > 0:
                fill_values = list(range(-num_to_be_filled, 0))
                sorted_index = np.lexsort((corr_df[0], corr_df[1]))
                index_to_fill = sorted_index[
                    total_zeroes - num_to_be_filled : total_zeroes
                ]
                corr_df[1][index_to_fill] = fill_values

            corr_df[corr_df == 0] = np.nan
            corr1 = corr_df[0]
            corr2 = corr_df[1]

        to_drop = np.isnan(corr1) | np.isnan(corr2)
        corr1 = corr1[~to_drop].argsort().argsort().astype("float64")
        corr2 = corr2[~to_drop].argsort().argsort().astype("float64")
        corr_results[k] = 0
        if len(corr1) < 2:
            corr_results[k] = 0
        else:
            corr_results[k] = pearson(corr1, corr2)

    to_return = corr_results > corr_value
    return a_index[to_return], b_index[to_return], corr_results[to_return]


def cluster(
    df,
    rt_thresh=0.02,
    corr_value=0.8,
    batch_size=1000,
    method="Spearman",
    nan_policy="fill",
):
    """
    Cluster aggregates LCMS features into groups based on sample-correlation and
        retention time. It builds a network based on retention time difference and
        correlation. Then it labels the largest clique as a cluster, deletes the
        features from the network, and identifies the next largest clique. Ties are
        broken but a summation of correlations in the cluster.

    df: Dataframe, Eclipse compatible
    rt_thresh: float, maximum Rt different for clustering
    corr_value: float, correlation cutoff
    batch_size: int, batch size for calculating correlations
    method: string, "Spearman" or "Pearson" correlation
    Returns
    Dataframe, containing cluster number and number of members for each feature. -1
       indicates a single, unclustered feature.
    """
    rt_series = df["RT"]
    rt_series.index.name = None  # otherwise it crashes during stack
    sample_df = df.copy().drop(ECLIPSE_COLUMNS, axis=1, errors="ignore").transpose()
    sample_df.columns.name = None  # otherwise it crashes during stack
    num_batches = math.ceil(len(sample_df.columns) / batch_size)
    graph = nx.Graph()

    for i in range(num_batches):
        LOGGER.info(f"Correlating Batch {i + 1}/{num_batches}...")
        for j in range(i, num_batches):

            if nan_policy == "fill":
                batch_a = sample_df.iloc[:, i * batch_size : (i + 1) * batch_size]
                batch_b = sample_df.iloc[:, j * batch_size : (j + 1) * batch_size]
                links = by_corr(
                    batch_a, batch_b, rt_series, corr_value, rt_thresh, method
                )
                a_index = df.loc[links["var1"], :].index
                b_index = df.loc[links["var2"], :].index
                corrs = links["Correlation"]
            else:
                i_indices = [
                    i * batch_size,
                    min((i + 1) * batch_size, len(sample_df.columns)),
                ]
                j_indices = [
                    j * batch_size,
                    min((j + 1) * batch_size, len(sample_df.columns)),
                ]
                a_index, b_index, corrs = by_rt(
                    i_indices,
                    j_indices,
                    rt_series,
                    sample_df,
                    corr_value,
                    rt_thresh,
                    method,
                    nan_policy,
                )
                a_index = df.index[a_index]
                b_index = df.index[b_index]

            edges = [
                (s, t, {"coor": coor}) for s, t, coor in zip(a_index, b_index, corrs)
            ]
            graph.add_nodes_from(a_index)
            graph.add_nodes_from(b_index)
            graph.add_edges_from(edges)
    return deconvolute(df.index, graph)
