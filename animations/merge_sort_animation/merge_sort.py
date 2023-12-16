from animations.merge_sort_animation.split_functionality import split_list
from animations.merge_sort_animation.merge_functionality import merge


def merge_sort_animation(list, constants, temp_list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(kn log n) time
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split_list(list, constants)
    left = merge_sort_animation(left_half, constants, temp_list)
    print("left in merge_sort: ", left)
    right = merge_sort_animation(right_half, constants, temp_list)
    print("right in merge_sort: ", right)

    return merge(left, right, constants, temp_list)
