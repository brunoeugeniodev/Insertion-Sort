def insertion_sort(v):
    for i in range(1, len(v)):
        aux = v[i]
        j = i - 1
        while j >= 0 and aux < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = aux
