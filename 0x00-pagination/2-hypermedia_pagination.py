#!/usr/bin/env python3
"""this file contains a function index_range that takes two
integer arguments as parameters"""
import csv
import math
from typing import Tuple, List, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this function computes a given page from the
    page and the page size passed"""
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return (start_index, end_index)


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
        """this function returns a list of liss
        for a given page required"""
        # check if the values passed are ints greater than 0
        flag: bool = type(page) is int and type(page_size) is int
        assert (flag and page > 0 and page_size > 0)
        #  get the indexes tuple from the index_range function
        start_index: int
        end_index: int
        start_index, end_index = index_range(page, page_size)
        #  get the list of lists for the different rows in the file
        data_set: List[List] = self.dataset()
        #  get the write rows from the dataset using the returned indexes
        my_page: List[List]
        try:
            my_page = data_set[start_index: end_index]
        except IndexError:
            my_page = [[]]
        return my_page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """this function returns a list of liss for a given page required"""
        #  get the list of lists for the required pages
        page_data: List[List] = self.get_page(page, page_size)
        #  get the total number of pages
        num_pages: int = math.ceil(len(self.dataset()) / page_size)
        #  check if next_page and Previous page exist
        next_page: Union[None, int] = None if (page + 1 > num_pages)\
            else page + 1
        prev_page: Union[None, int] = page - 1 if (page - 1 >= 1) else None
        #  make a dictionary
        page_dict: Dict[str, Union[int, List[List], None]] = {}
        page_dict['page_size'] = len(page_data)
        page_dict['page'] = page
        page_dict['data'] = page_data
        page_dict['next_page'] = next_page
        page_dict['prev_page'] = prev_page
        page_dict['total_pages'] = num_pages
        return page_dict
