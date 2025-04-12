import time
from insertionSortOtimizado import insertion_sort_otimizado

lista = [92, 18, 47, 2, 8, 86, 55, 75, 41, 61, 34, 63, 70, 11, 64, 88, 20, 6, 53, 78,
 85, 43, 45, 19, 81, 40, 7, 32, 91, 4, 25, 15, 76, 16, 62, 9, 87, 96, 56, 28,
 44, 35, 14, 22, 71, 24, 93, 82, 98, 1, 83, 26, 3, 38, 89, 67, 30, 5, 33, 13,
 99, 12, 31, 48, 10, 21, 59, 23, 27, 73, 50, 84, 66, 52, 36, 90, 95, 0, 94, 60,
 49, 97, 77, 74, 42, 46, 80, 17, 29, 39, 68, 65, 69, 72, 37, 54, 51, 57, 58, 79]

print("Lista desordenada: ", lista)

inicio = time.time()
insertion_sort_otimizado(lista)
fim = time.time()

print("Lista ordenada: ", lista)

print(f"Tempo gasto: {fim - inicio:.6f} segundos", flush=True)