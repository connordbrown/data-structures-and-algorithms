#include <cmath>
#include <iostream>

bool isPrime(int n) {
  if (n < 2) {
    return false;
  }
  for (int i = 2; i <= std::sqrt(n); ++i) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {

    std::cout << isPrime(1) << " == " << 0 << std::endl; // -> 0
    std::cout << isPrime(2) << " == " << 1 << std::endl; // -> 1
    std::cout << isPrime(3) << " == " << 1 << std::endl; // -> 1
    std::cout << isPrime(4) << " == " << 0 << std::endl; // -> 0
    std::cout << isPrime(5) << " == " << 1 << std::endl; // -> 1
    std::cout << isPrime(6) << " == " << 0 << std::endl; // -> 0
    std::cout << isPrime(7) << " == " << 1 << std::endl; // -> 1
    std::cout << isPrime(8) << " == " << 0 << std::endl; // -> 0
    std::cout << isPrime(25) << " == " << 0 << std::endl; // -> 0
    std::cout << isPrime(31) << " == " << 1 << std::endl; // -> 1
    std::cout << isPrime(2017) << " == " << 1 << std::endl; // -> 1
    std::cout << isPrime(2048) << " == " << 0 << std::endl; // -> 0
    std::cout << isPrime(713) << " == " << 0 << std::endl; // -> 0

    return 0;
}