#include <iostream>
#include <vector>
#include <omp.h>

void highPerformanceComputing() {
  int numThreads = omp_get_max_threads();
  std::vector<int> data(1000000);

  #pragma omp parallel for num_threads(numThreads)
  for(int i = 0; i < data.size(); i++) {
    data[i] = i * i;
  }

  int sum = 0;
  #pragma omp parallel for reduction(+:sum)
  for (int i = 0; i < data.size(); i++) {
    sum += data[i];
  }

  std::cout << "Sum: " << sum << std::endl;
}

int main() {
  highPerformanceComputing();
  return 0;
}
