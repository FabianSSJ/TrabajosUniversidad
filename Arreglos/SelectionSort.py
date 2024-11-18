def selection_sort(arr):
    
   # Ordena un arreglo utilizando selection sort.
   # :param arr: List[int] - Arreglo de enteros.
   # :return: List[int] - Arreglo ordenado.
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Selection Sort: {selection_sort(array)}")
