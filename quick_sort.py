from print_items import *
from colorama import Fore


def quick_sort(unsorted_list, constants, temp_list):
    """
    Sorts a list of numbers using quick sort algorithm, recursively
    Args:
        initial_list (list): list of numbers
        constants_dict (dict): dictionary of constants
        temp_list (list): list of numbers
    Returns:
        initial_list (list): sorted list of numbers
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        input("Press Press Enter to continue...")
        print("Entering quick sort")
        pivot = unsorted_list[0]
        print(f"""{Fore.GREEN}Pivot: {pivot}{Fore.WHITE}""")
        if len(unsorted_list) > 0:
            
            print_list_with_pivot(unsorted_list, pivot, constants)
            if len(unsorted_list) != len(temp_list):
                print_items(unsorted_list, constants)
                print()
        less_than_pivot = [x for x in unsorted_list[1:] if x <= pivot]
        if len(less_than_pivot) > 0:
            print(f"""Less than pivot: {Fore.YELLOW}{less_than_pivot}{Fore.WHITE}""")
            print_items(less_than_pivot, constants)
        else:
            print(f"""Less than pivot: {Fore.YELLOW}{less_than_pivot}{Fore.WHITE}""")
        greater_than_pivot = [x for x in unsorted_list[1:] if x > pivot]
        if len(greater_than_pivot) > 0:
            print(f"""Greater than pivot: {Fore.MAGENTA}{greater_than_pivot}{Fore.WHITE}""")
            print_items(greater_than_pivot, constants)
        else:
            print(f"""Greater than pivot: {Fore.MAGENTA}{greater_than_pivot}{Fore.WHITE}""")
        merged_list = get_whole_list(less_than_pivot, pivot, greater_than_pivot)
        if len(merged_list) > 0:
            input("Press Enter to see the merged list")
            print()
            print(f"""Merged list: {Fore.CYAN}{merged_list}{Fore.WHITE}""")
            print_items(merged_list, constants)
            print()
        return quick_sort(less_than_pivot, constants, temp_list) + [pivot] + quick_sort(greater_than_pivot, constants, temp_list)


def print_list_with_pivot(unsorted_list, pivot, constants):
    """
    Prints the items in a list
    Args:
        keys (list): list of numbers
        constants_dict (dict): dictionary of constants
    Returns:
        None
    """
    print("[", end="")
    last_index = len(unsorted_list) - 1
    for k in range(len(unsorted_list)):
            if k != last_index:
                if unsorted_list[k] == pivot:
                    print(
                        f"""{Fore.GREEN}{unsorted_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
                else:
                    print(
                        f"""{Fore.BLUE}{unsorted_list[k]}{Fore.WHITE}""",
                        end=", "
                    )
            else:
                if unsorted_list[k] == pivot:
                    print(
                        f"""{Fore.GREEN}{unsorted_list[k]}{Fore.WHITE}""",
                        end=""
                    )
                else:
                    print(
                        f"""{Fore.BLUE}{unsorted_list[k]}{Fore.WHITE}""",
                        end=""
                    )
    print("]")


def get_whole_list(less_than_pivot, pivot, greater_than_pivot):
    """
    Gets the whole list
    Args:
        less_than_pivot (list): list of numbers less than the pivot
        pivot (int): the pivot
        greater_than_pivot (list): list of numbers greater than the pivot
    Returns:
        list: the whole list
    """
    new_list = []
    for i in less_than_pivot:
        new_list.append(i)
    new_list.append(pivot)
    for i in greater_than_pivot:
        new_list.append(i)
    return new_list
