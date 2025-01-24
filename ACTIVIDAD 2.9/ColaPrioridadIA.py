import heapq
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Generar datos simulados para entrenamiento
def generate_data(samples=1000):
    """Genera datos simulados para entrenar el modelo de predicción."""
    customer_type = np.random.randint(0, 3, samples)  # 0: Regular, 1: VIP, 2: Frecuente
    current_load = np.random.randint(1, 100, samples)  # Carga actual del sistema
    arrival_time = np.random.randint(0, 60, samples)  # Tiempo desde la apertura (en minutos)
    
    # Tiempo de espera simulado (objetivo a predecir)
    wait_time = (
        10 * (1 / (customer_type + 1)) + 
        0.5 * current_load + 
        0.2 * arrival_time + 
        np.random.normal(0, 5, samples) 
    )
    
    return np.column_stack((customer_type, current_load, arrival_time)), wait_time

# Generar datos
X, y = generate_data()

# Dividir en entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Verifica los datos generados
print("Datos de entrada (X):", X[:5])  # Muestra las primeras 5 filas
print("Datos de salida (y):", y[:5])  # Muestra los primeros 5 valores de salida

# Crear el modelo de regresión
model = Sequential([
    Dense(64, activation='relu', input_shape=(3,)),  # 3 características
    Dense(32, activation='relu'),
    Dense(1)  # Predicción del tiempo de espera
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Graficar el entrenamiento
plt.plot(history.history['loss'], label='Pérdida de entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida de validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida (MSE)')
plt.legend()
plt.show()

class PriorityQueue:
    def __init__(self):
        self.queue = []
        heapq.heapify(self.queue)
    
    def push(self, priority, item):
        """Inserta un elemento con una prioridad dada."""
        heapq.heappush(self.queue, (priority, item))
    
    def pop(self):
        """Saca el elemento con la mayor prioridad (menor valor de prioridad)."""
        return heapq.heappop(self.queue)
    
    def __len__(self):
        return len(self.queue)

# Crear una instancia de la cola
priority_queue = PriorityQueue()


# Simular clientes llegando a la cola
for i in range(20):  # Simular 20 clientes
    customer_type = random.randint(0, 2)
    current_load = random.randint(1, 100)
    arrival_time = random.randint(0, 60)
    
    # Predecir el tiempo de espera con el modelo
    features = np.array([[customer_type, current_load, arrival_time]])
    predicted_wait_time = model.predict(features)[0][0]
    
    # Asignar prioridad basada en el tiempo de espera predicho
    priority_queue.push(predicted_wait_time, f"Cliente {i + 1}")

# Procesar la cola
print("Orden de atención (por prioridad):")
while len(priority_queue) > 0:
    priority, customer = priority_queue.pop()
    print(f"{customer} con prioridad {priority:.2f}")
