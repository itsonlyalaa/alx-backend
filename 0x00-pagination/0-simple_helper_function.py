#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Type-annotated function index_range that takes a integer arguments"""

    final: int = page * page_size
    start: int = final - page_size

    return (start, final)
