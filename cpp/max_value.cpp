#include <vector>
#include <limits>
#include <iostream>

float maxValue(std::vector<float> numbers) {
  float max = -std::numeric_limits<float>::infinity();
  for (float num : numbers) {
    if (num > max) {
      max = num;
    }
  }
  return max;
}

int main() {
    std::vector<float> numbers1{ 4, 7, 2, 8, 10, 9 };
    std::cout << maxValue(numbers1) << std::endl; // -> 10

    std::vector<float> numbers2{ 10, 5, 40, 40.3 };
    std::cout << maxValue(numbers2) << std::endl; // -> 40.3

    std::vector<float> numbers3{ -5, -2, -1, -11 };
    std::cout << maxValue(numbers3) << std::endl;// -> -1

    std::vector<float> numbers4{ 42 };
    std::cout << maxValue(numbers4) << std::endl; // -> 42

    std::vector<float> numbers5{ 1000, 8 };
    std::cout << maxValue(numbers5) << std::endl; // -> 1000

    std::vector<float> numbers6{ 1000, 8, 9000 };
    std::cout << maxValue(numbers6) << std::endl; // -> 9000

    std::vector<float> numbers7{ 2, 5, 1, 1, 4 };
    std::cout << maxValue(numbers7) << std::endl; // -> 5

  return 0;
}
