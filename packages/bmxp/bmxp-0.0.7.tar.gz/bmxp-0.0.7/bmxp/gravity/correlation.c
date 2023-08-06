#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Ranking {
  double value;
  uint32_t index;
} Ranking;

double sum_m(double* x, uint32_t size, int* mask) {
  double total = 0;
  for (uint32_t i = 0; i < size; i++) {
    if (mask[i]) total += x[i];
  }
  return total;
}

double covariance_m(double* x, double* y, double meanX, double meanY, uint32_t size, int* mask) {
  double result = 0;

  for (uint32_t i = 0; i < size; i++) {
    if (mask[i]) result += (x[i] - meanX) * (y[i] - meanY);
  }
  return result;
}

double stdev_m(double* x, double meanX, uint32_t size, int* mask, uint32_t mask_size) {
  double stdevSquared = 0;
  for (uint32_t i = 0; i < size; i++) {
    if (mask[i]) stdevSquared += pow(x[i] - meanX, 2);
  }
  stdevSquared = stdevSquared / mask_size;

  return sqrt(stdevSquared);
}

double sum(double* x, uint32_t size) {
  double total = 0;
  for (uint32_t i = 0; i < size; i++) {
    total += x[i];
  }
  return total;
}

double covariance(double* x, double* y, double meanX, double meanY, uint32_t size) {
  double result = 0;
  for (uint32_t i = 0; i < size; i++) {
    result += (x[i] - meanX) * (y[i] - meanY);
  }
  return result / size;
}

double stdev(double* x, double meanX, uint32_t size) {
  double stdevSquared = 0;
  for (uint32_t i = 0; i < size; i++) {
    stdevSquared += pow(x[i] - meanX, 2);
  }
  stdevSquared = stdevSquared / size;

  return sqrt(stdevSquared);
}

uint32_t removeNans(double* x, double* y, uint32_t size) {
  uint32_t newSize = size;
  uint32_t pos = 0;
  for (uint32_t i = 0; i < size; i++) {
    if (x[i] == 0 || y[i] == 0) {
      newSize--;
    } else {
      x[pos] = x[i];
      y[pos] = y[i];
      pos++;
    }
  }
  return newSize;
}

int comparator(const void* a, const void* b) {
  double valA = ((struct Ranking*)a)->value;
  double valB = ((struct Ranking*)b)->value;
  if (valA != valA) // if A is nan, move A up
  {
    return 1;
  }
  if (valB != valB) // if B is nan, move B up
  {
    return -1;
  }
  if (valA > valB) {
    return 1;
  }
  if (valA < valB) {
    return -1;
  }
  return 0;
}

int* nanMask(double* x, double* y, uint32_t size) {
  int* mask = malloc(sizeof(Ranking) * size);
  for (uint32_t i = 0; i < size; i++) {
    mask[i] = (x[i] == x[i]) && (y[i] == y[i]); // check if Nan
  }
  return mask;
}

double pearson_m(double* x, double* y, uint32_t size) {
  int* mask = nanMask(x, y, size);
  uint32_t mask_size = 0;
  for (uint32_t i = 0; i < size; i++) {
    mask_size += mask[i];
  }
  double meanX = sum_m(x, size, mask) / mask_size;
  double meanY = sum_m(y, size, mask) / mask_size;
  double cov = covariance_m(x, y, meanX, meanY, size, mask) / mask_size;
  double stdevX = stdev_m(x, meanX, size, mask, mask_size);
  double stdevY = stdev_m(y, meanY, size, mask, mask_size);

  return cov / (stdevX * stdevY);
}

double pearson(double* x, double* y, uint32_t size) {
  double meanX = sum(x, size) / size;
  double meanY = sum(y, size) / size;

  double cov = covariance(x, y, meanX, meanY, size);
  double stdevX = stdev(x, meanX, size);
  double stdevY = stdev(y, meanY, size);

  return cov / (stdevX * stdevY);
}

double spearman(double* x, double* y, uint32_t size) {

  int* mask = nanMask(x, y, size);

  Ranking* sortedX = malloc(sizeof(Ranking) * size);
  Ranking* sortedY = malloc(sizeof(Ranking) * size);

  for (uint32_t i = 0; i < size; i++) {

    memcpy(&sortedX[i].value, &x[i], 8);
    sortedX[i].index = i;
    memcpy(&sortedY[i].value, &y[i], 8);
    sortedY[i].index = i;
  }

  qsort(sortedX, size, sizeof(Ranking), comparator); // index and values of sorted x
  qsort(sortedY, size, sizeof(Ranking), comparator); // index and values of sorted y

  // biuld ranks for x
  uint32_t next_x = 1;
  uint32_t next_y = 1;
  for (uint32_t i = 0; i < size; i++) {
    if (mask[sortedX[i].index]) {
      x[sortedX[i].index] = next_x;
      next_x++;
    }
    if (mask[sortedY[i].index]) {
      y[sortedY[i].index] = next_y;
      next_y++;
    }
  }

  free(sortedX);
  free(sortedY);

  return pearson(x, y, size);
}

void main() {
  double array1[] = {1, 3.5, 5, 7.5, 9, 8, 7.2, 4, -2};
  double array2[] = {3, 5, 7, 9, 11, 10, 8, 6, 4};

  double x = pearson(array1, array2, 9);
  double y = spearman(array1, array2, 9);
  printf("%f, %f\n", x, y);
}
