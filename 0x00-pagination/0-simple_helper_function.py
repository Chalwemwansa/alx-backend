#!/usr/bin/env python3
"""this file contains a function index_range that takes two
integer arguments as parameters"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this function computes a given page from the
    page and the page size passed"""
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return (start_index, end_index)
