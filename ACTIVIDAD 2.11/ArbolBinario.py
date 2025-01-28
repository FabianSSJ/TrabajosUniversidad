class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolExpresion:
    def __init__(self):
        self.raiz = None

    def construir_desde_postfija(self, expresion):
        """
        Construye el árbol binario a partir de una expresión en notación postfija.
        """
        pila_nodos = []
        
        for elemento in expresion:
            if isinstance(elemento, (int, float)):  
                pila_nodos.append(Nodo(elemento))
            elif callable(elemento): 
                nuevo_nodo = Nodo(elemento)
                nuevo_nodo.derecho = pila_nodos.pop()
                nuevo_nodo.izquierdo = pila_nodos.pop()
                pila_nodos.append(nuevo_nodo)
        
        self.raiz = pila_nodos.pop()

    def evaluar_arbol(self, nodo=None):
        """
        Evalúa la expresión representada por el árbol binario.
        """
        if nodo is None:
            nodo = self.raiz

        if nodo.izquierdo is None and nodo.derecho is None: 
            return nodo.valor

        # Evaluar recursivamente los hijos izquierdo y derecho
        valor_izquierdo = self.evaluar_arbol(nodo.izquierdo)
        valor_derecho = self.evaluar_arbol(nodo.derecho)

        # Aplicar la operación del nodo actual
        return nodo.valor(valor_izquierdo, valor_derecho)

# Ejemplo de uso
if __name__ == "__main__":
    # Definir operadores
    suma = lambda a, b: a + b
    resta = lambda a, b: a - b
    multiplicacion = lambda a, b: a * b
    division = lambda a, b: a / b

    # Expresión 1: Evaluar 7 + 8
    expresion1 = [7, 8, suma]  
    arbol1 = ArbolExpresion()
    arbol1.construir_desde_postfija(expresion1)
    print("Resultado de 7 + 8:", arbol1.evaluar_arbol())

    # Expresión 2: Evaluar (5 * 3) - 2
    expresion2 = [5, 3, multiplicacion, 2, resta]  
    arbol2 = ArbolExpresion()
    arbol2.construir_desde_postfija(expresion2)
    print("Resultado de (5 * 3) - 2:", arbol2.evaluar_arbol())

    # Expresión 3: Evaluar (9 / 3) + (6 * 2)
    expresion3 = [9, 3, division, 6, 2, multiplicacion, suma]  
    arbol3 = ArbolExpresion()
    arbol3.construir_desde_postfija(expresion3)
    print("Resultado de (9 / 3) + (6 * 2):", arbol3.evaluar_arbol())
