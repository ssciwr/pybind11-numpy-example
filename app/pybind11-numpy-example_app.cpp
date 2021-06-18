#include "pybind11-numpy-example/pybind11-numpy-example.hpp"
#include <iostream>

int main(){
  int result = pybind11numpyexample::add_one(1);
  std::cout << "1 + 1 = " << result << std::endl;
}