#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """finding peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    elif list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    left = 0
    right = len(list_of_integers)

    while left <= right:
        mid = (right + left) // 2

        if (
            list_of_integers[mid] >= list_of_integers[mid - 1]
            and list_of_integers[mid] >= list_of_integers[mid + 1]
        ):
            return list_of_integers[mid]
        elif list_of_integers[mid] >= list_of_integers[mid - 1]:
            left += 1
        else:
            right += 1
