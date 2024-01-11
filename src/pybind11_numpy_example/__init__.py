# here we import the contents of our compiled C++ module into this package:
from ._pybind11_numpy_example import *


# this allows us to also include pure python code in the same namespace:
def pure_python_list(size: int):
    return list(range(size))
