def find_min_index(li: [], start_index: int):
    min_index = start_index
    for i in range(start_index, len(li)):
        print(i)
        if li[i] < li[min_index]:
            min_index = i
    return min_index


def switch(li: [], a: int, b: int):
    tmp = li[a]
    li[a] = li[b]
    li[b] = tmp


def selection_sort(li: []):
    for i in range(len(li)):
        min_index = find_min_index(li, i)
        switch(li, i, min_index)
