import os
import time
from print_items import print_items, print_temp_item
from constant_dictionary import *


def insertion_sort_animation(list_data, constants):
    for scan_index in range(1, len(list_data)):
        temp = list_data[scan_index]
        min_index = scan_index
        while min_index > 0 and temp < list_data[min_index - 1]:
            list_data[min_index] = list_data[min_index - 1]
            min_index -= 1
            list_data[min_index] = temp
            printing_animation(temp, list_data, constants)
        printing_animation(temp, list_data, constants)
    return list_data


