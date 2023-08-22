"""Model wrapper for C++ kernel."""

import os
import ctypes
from typing import Union

_PATH_TO_lib: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "cpp_dynamic_lib/model.so"
)

_NUMBER_OF_STEPS: int = 2000


def calculate(expression: str) -> Union[str, None]:
    """
    Calculate the result of a mathematical expression.

    Args:
        expression (str): Mathematical expression.

    Returns:
        Union[str, None]: Calculated result as a string or None when error.
    """
    model_lib = ctypes.CDLL(_PATH_TO_lib)
    model_lib.GetResult.argtypes = [ctypes.c_char_p,
                                    ctypes.POINTER(ctypes.c_double)]
    model_lib.GetResult.restype = ctypes.c_bool
    result: ctypes.c_double = ctypes.c_double()
    if model_lib.GetResult(expression.encode(), ctypes.byref(result)):
        return str(result.value)
    else:
        return None


def graph_calculate(expression: str, x_min: str, x_max: str) -> Union[list, None]:  # pylint: disable=line-too-long
    """
    Calculate the result of a graph expression over a range of x values.

    Args:
        expression (str): Graph expression.
        x_min (str): Minimum value of x.
        x_max (str): Maximum value of x.

    Returns:
        Union[list, None]: List of calculated x & y values or None when error.
    """
    model_lib = ctypes.CDLL(_PATH_TO_lib)
    model_lib.GetResultForGraph.argtypes = [
        ctypes.c_char_p,
        ctypes.c_double,
        ctypes.c_double,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double),
    ]
    model_lib.GetResultForGraph.restype = ctypes.c_bool

    x_values_buffer = (ctypes.c_double * _NUMBER_OF_STEPS)()
    y_values_buffer = (ctypes.c_double * _NUMBER_OF_STEPS)()
    x_buf_ptr = ctypes.cast(x_values_buffer, ctypes.POINTER(ctypes.c_double))
    y_buf_ptr = ctypes.cast(y_values_buffer, ctypes.POINTER(ctypes.c_double))

    if model_lib.GetResultForGraph(
        expression.encode(),
        float(x_min),
        float(x_max),
        _NUMBER_OF_STEPS,
        x_buf_ptr,
        y_buf_ptr,
    ):
        x_result_list: list = [x_buf_ptr[i] for i in range(_NUMBER_OF_STEPS)]
        y_result_list: list = [y_buf_ptr[i] for i in range(_NUMBER_OF_STEPS)]
        return [x_result_list, y_result_list]
    else:
        return None
