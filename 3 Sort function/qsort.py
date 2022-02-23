import random


def quicksort(array, left_element, right_element):
    if left_element >= right_element:
        return

    i, j = left_element, right_element
    pivot = array[random.randint(left_element, right_element)]

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quicksort(array, left_element, j)
    quicksort(array, i, right_element)


def sort_array(array):
    quicksort(array, 0, len(array) - 1)
