
# Evaluador de Expresiones Matematicas
Paso 1: Selección del TDA y la Aplicación
TDA elegido: Pila
Aplicación: Evaluador de expresiones matematicas (que soporte operaciones básicas como suma, resta, multiplicación y división).

Paso 2: Investigacion y Diseño
Diseño de la Pila:
La pila es una estructura LIFO (Last In, First Out), lo que significa que el ultimo elemento insertado será el primero en salir. Las operaciones básicas para una pila son:

## Descripción

codigo en Python implementa a un **Evaluador de Expresiones Matematicas** que usa una estructura de datos **Pila** para manejar la precedencia de operadores y evaluar expresiones aritméticas que incluyen paréntesis. La pila se utiliza para almacenar los operandos y operadores durante el proceso de evaluación.

### Funcionalidades:
- Evaluacion de expresiones matematicas con operadores básicos (`+`, `-`, `*`, `/`).
- Manejo de paréntesis para definir el orden de las operaciones.
- Soporta expresiones sin espacios entre los operadores y operandos.

## TDA Implementado

### Pila
La pila es una estructura de datos de tipo LIFO (Last In, First Out). En este proyecto, la pila se usa para:
1. **Almacenar los operadores** mientras se evaluan los operandos.
2. **Gestionar los parentesis** que delimitan subexpresiones.

Las operaciones basicas implementadas para la pila son:
- **push(x)**: Inserta un elemento `x` en la pila.
- **pop()**: Elimina y devuelve el elemento superior de la pila.
- **peek()**: Devuelve el elemento superior sin eliminarlo.
- **is_empty()**: Verifica si la pila está vacía.

### Evaluador de Expresiones
El evaluador utiliza la pila para procesar la expresion de izquierda a derecha, aplicando la precedencia de los operadores y evaluando las subexpresiones en función de los paréntesis.

