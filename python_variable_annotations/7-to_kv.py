#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function to_kv that takes a string k and an int OR float v as
    arguments and returns a tuple. The first element of the tuple is the
    string k. The second element is the square of the int/float v and should
    be annotated as a float.

    Args:
        k (str): A string.
        v (Union[int, float]): A number which can be an integer or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is `k` and the
        second element is the square of `v`, represented as a float.
    """
    return(k, float(v ** 2))
