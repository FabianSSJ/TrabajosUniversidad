def fibonacci(n, secuencia=None):
    if secuencia is None:
        secuencia = [0, 1] if n > 1 else [0]  
    
    if len(secuencia) == n:
        return secuencia
    
    nuevo_termino = secuencia[-1] + secuencia[-2]
    secuencia.append(nuevo_termino)
    
    return fibonacci(n, secuencia)

num_terminos = int(input("Ingresar el numero de terminos: "))
resultado = fibonacci(num_terminos)
print(f"La serie de Fibonacci con {num_terminos} terminos es: {resultado}")
