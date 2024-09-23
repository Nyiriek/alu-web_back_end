#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """Get a dictionary with the following key-value pairs:
        - index: the current index in the dataset of the first element
        - next_index: the next index to query with
        - prev_index: the previous index to query with
        - page_size: the current page size
        - data: the dataset page
        """
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        if index is None or index not in indexed_dataset:
            return {
                'index': 0,
                'next_index': None,
                'prev_index': None,
                'page_size': page_size,
                'data': list(indexed_dataset.values())[:page_size]
            }

        data = list(indexed_dataset.values())[index:index + page_size]
        next_index = index + page_size
        prev_index = index - page_size if index > 0 else None
        return {
            'index': index,
            'next_index': next_index,
            'prev_index': prev_index,
            'page_size': page_size,
            'data': data
        }
