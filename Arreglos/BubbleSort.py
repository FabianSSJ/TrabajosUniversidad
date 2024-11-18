def bubble_sort(arr):
    
   # Ordena un arreglo utilizando bubble sort optimizado.
   # :param arr: List[int] - Arreglo de enteros.
   # :return: List[int] - Arreglo ordenado.
    
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Bubble Sort: {bubble_sort(array)}")