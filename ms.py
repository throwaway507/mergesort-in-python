import random


def merge(l, m, r, a):
    t1 = [0] * (m - l + 1)
    t2 = [0] * (r - m)
    for i in range(len(t1)):
        t1[i] = a[l + i]
    for j in range(len(t2)):
        t2[j] = a[j + m + 1]

    i = j = 0
    k = l
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            a[k] = t1[i]
            i += 1
        else:
            a[k] = t2[j]
            j += 1
        k += 1

    while i < len(t1):
        a[k] = t1[i]
        i += 1
        k += 1

    while j < len(t2):
        a[k] = t2[j]
        j += 1
        k += 1


def mergesort(l, r, a):
    """mergesort that sorts the array passed in by the user"""
    if l < r:
        m = l + ((r-l) // 2)  # no overflow
        mergesort(l, m, a)
        mergesort(m+1, r, a)
        merge(l, m, r, a)


def randomArray():
    elements = 10  # you can change how many elements u want
    arr = []
    for i in range(elements):
        arr.append(random.randint(0, 20))
    return arr


arr = randomArray()
print("Before sorting: ")
print(arr)
mergesort(0, len(arr)-1, arr)
print("After sorting: ")
print(arr)