def find_min_index(li: []):
    min_index = 0
    for i in range(len(li)):
        if li[i] < li[min_index]:
            min_index = i
    return min_index


def switch(li: [], a: int, b: int):
    tmp = li[a]
    li[a] = li[b]
    li[b] = tmp


def selection_sort(li: []):
    for i in range(len(li)):
        min_index = find_min_index(li[i:])
        switch(li, i, i + min_index)
