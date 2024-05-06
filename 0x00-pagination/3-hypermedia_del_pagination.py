#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """this function makes sure that even if a row is deleted no page
        will be skipped when returning the pages"""
        dataset = self.indexed_dataset()
        assert (index >= 0 and index <= max(dataset))
        data = [dataset[key] for key in dataset.keys() if
                (key >= index and key < (index + page_size))]
        page_dict: Dict[str, Union[int, List[List]]] = {}
        page_dict['index'] = index
        page_dict['data'] = data
        page_dict['page_size'] = len(data)
        page_dict['next_index'] = index + page_size
        return page_dict
