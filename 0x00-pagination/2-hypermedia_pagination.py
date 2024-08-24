#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from math import ceil
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Type-annotated function index_range that takes a integer arguments"""

    final: int = page * page_size
    start: int = final - page_size

    return (start, final)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get the page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range[0]:range[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hypermedia pagination"""
        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        total_page: int = len(dataset) if dataset else 0
        total_page = ceil(total_page / page_size)
        prev_page: int = (page - 1) if (page - 1) >= 1 else None
        next_page: int = (page + 1) if (page + 1) <= total_page else None

        hyper: Dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_page,
        }

        return hyper
