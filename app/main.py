import random
import sys
import time

sys.setrecursionlimit(5000000)


def quickSort(A, p, r):
    if len(A) == 1:
        return A
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = (p - 1)
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def maxHeapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and A[l] > A[largest]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, n, largest)


def buildMaxHeap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        maxHeapify(A, n, i)


def heapSort(A):
    n = len(A)
    buildMaxHeap(A)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        maxHeapify(A, i, 0)


def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def mergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


A = [random.randint(1, 100) for _ in range(100000)]
B = sorted(A)
C = sorted(A, reverse=True)
A1 = A
B1 = B
C1 = C
n = len(A1)
begin = time.time()
quickSort(A1, 0, n - 1)
end = time.time()
print("QuickSort random:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
#quickSort(B1, 0, n - 1)
end = time.time()
print("QuickSort sorted:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
#quickSort(C1, 0, n - 1)
end = time.time()
print("QuickSort reversed:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
A2 = A
B2 = B
C2 = C
begin = time.time()
heapSort(A2)
end = time.time()
print("HeapSort random:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
heapSort(B2)
end = time.time()
print("HeapSort sorted:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
heapSort(C2)
end = time.time()
print("HeapSort reversed:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
A3 = A
B3 = B
C3 = C
begin = time.time()
bubbleSort(A3)
end = time.time()
print("BubbleSort random:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
bubbleSort(B3)
end = time.time()
print("BubbleSort sorted:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
bubbleSort(C3)
end = time.time()
print("BubbleSort reversed:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
A4 = A
B4 = B
C4 = C
begin = time.time()
mergeSort(A4)
end = time.time()
print("MergeSort random:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
mergeSort(B4)
end = time.time()
print("MergeSort sorted:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")
begin = time.time()
mergeSort(C4)
end = time.time()
print("MergeSort reversed:")
print(f"Total runtime of the program is {round((end - begin), 2)} s.")