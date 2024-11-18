# Implementacion de algoritmos de busqueda y ordenacion en Python

# Busqueda del elemento mayor o menor en un arreglo
def buscar_mayor_menor(arr):
    if not arr:
        return None, None  # Devuelve None si el arreglo no contiene informacion
    mayor = menor = arr[0]
    for num in arr:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    return mayor, menor

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Pruebas
if __name__ == "__main__":
    datos = [74, 24, 15, 22, 42, 110, 80]
    print("Arreglo original:", datos)

    # Encontrar mayor y menor
    mayor, menor = buscar_mayor_menor(datos)
    print(f"Mayor: {mayor}, Menor: {menor}")

    # Bubble Sort
    datos_bubble = datos[:]
    print("Ordenado con Bubble Sort:", bubble_sort(datos_bubble))

    # Selection Sort
    datos_selection = datos[:]
    print("Ordenado con Selection Sort:", selection_sort(datos_selection))