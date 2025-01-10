def generar_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fibonacci = [0, 1]
    i = 2
    while i < n:
        nuevo_termino = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(nuevo_termino)
        i += 1 
    
    return fibonacci

num_terminos = int(input("Ingresar el numero de términos: "))
resultado = generar_fibonacci(num_terminos)
print(f"La serie de Fibonacci con {num_terminos} terminos es: {resultado}")
