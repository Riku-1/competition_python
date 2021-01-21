def find_min_index(array):
    min_index = 0
    for i in range(len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index


def switch(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp


def selection_sort(array):
    for i in range(len(array)):
        min_index = find_min_index(array[i:])
        switch(array, i, i + min_index)
