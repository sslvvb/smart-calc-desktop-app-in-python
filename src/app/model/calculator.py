"""Model wrapper for C++ kernel."""

import ctypes
from typing import Union

PATH_TO_lib = '/Users/sslvvb/Documents/S21/Projects/Python/python_calc_3/my_git_rep_python_calc/src/app/model/cpp_dynamic_lib/model.so'
# относительный пть
number_of_steps: int = 2000


def calculate(expression: str) -> Union[str, None]:
    model_lib = ctypes.CDLL(PATH_TO_lib)
    model_lib.GetResult.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)]
    model_lib.GetResult.restype = ctypes.c_bool
    result: ctypes.c_double = ctypes.c_double()
    if model_lib.GetResult(expression.encode(), ctypes.byref(result)):
        return str(result.value)
    else:
        return None


def graph_calculate(expression: str, x_min: str, x_max: str) -> Union[list, None]:
    model_lib = ctypes.CDLL(PATH_TO_lib)
    model_lib.GetResultForGraph.argtypes = [ctypes.c_char_p, ctypes.c_double, ctypes.c_double, ctypes.c_int,
                                            ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
    model_lib.GetResultForGraph.restype = ctypes.c_bool

    x_values_buffer = (ctypes.c_double * number_of_steps)()
    y_values_buffer = (ctypes.c_double * number_of_steps)()
    x_buf_ptr = ctypes.cast(x_values_buffer, ctypes.POINTER(ctypes.c_double))
    y_buf_ptr = ctypes.cast(y_values_buffer, ctypes.POINTER(ctypes.c_double))

    if model_lib.GetResultForGraph(expression.encode(), float(x_min), float(x_max),
                                   number_of_steps, x_buf_ptr, y_buf_ptr):
        x_result_list: list = [x_buf_ptr[i] for i in range(number_of_steps)]
        y_result_list: list = [y_buf_ptr[i] for i in range(number_of_steps)]
        return [x_result_list, y_result_list]
    else:
        return None

# docstring
# относительный путь
# стиль для констант


if __name__ == "__main__":
    print(graph_calculate("x*2", "-5.0", "5.0"))
