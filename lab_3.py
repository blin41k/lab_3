import random
import time
import matplotlib.pyplot as mtp

def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        current = a[i]
        j = i - 1

        while j >= 0 and a[j] > current:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = current

    return a

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
times_insertion = []
times_bubble = []
times_quick = []

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]

    times_insertion.append(measure_time(insertion_sort, arr))
    times_bubble.append(measure_time(bubble_sort, arr))
    times_quick.append(measure_time(quick_sort, arr))

print("Размер | Вставками | Пузырьком | Быстрая")
for i in range(len(sizes)):
    print(
        sizes[i], "|",
        times_insertion[i], "|",
        times_bubble[i], "|",
        times_quick[i]
    )

mtp.plot(sizes, times_insertion, marker='o', label='Сортировка вставками')
mtp.plot(sizes, times_bubble, marker='o', label='Сортировка пузырьком')
mtp.plot(sizes, times_quick, marker='o', label='Быстрая сортировка')

mtp.xlabel("Количество элементов в массиве")
mtp.ylabel("Время выполнения, с")
mtp.title("Сравнение алгоритмов сортировки")
mtp.legend()
mtp.grid(True)
mtp.show()