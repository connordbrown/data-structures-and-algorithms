#include <string>
#include <cctype>
#include <iostream>

std::string uncompress(std::string s) {
  std::string output = "";
  int i = 0;
  int j = 0;
  while (j < s.length()) {
    if (std::isdigit(s[j])) {
      ++j;
    }
    else {
      int count = std::stoi(s.substr(i, j - i));
      output.append(std::string(count, s[j]));
      ++j;
      i = j;
    }
  }
  return output;
}

int main() {

    std::cout << (uncompress("2c3a1t") == "ccaaat") << std::endl;
    std::cout << (uncompress("4s2b") == "ssssbb") << std::endl;
    std::cout << (uncompress("2p1o5p") == "ppoppppp") << std::endl;
    std::cout << (uncompress("3n12e2z") == "nnneeeeeeeeeeeezz") << std::endl;
    std::cout << (uncompress("127y") == "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy") << std::endl;

    return 0;
}