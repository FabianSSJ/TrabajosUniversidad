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
        np.random.normal(0, 5, samples)  # Ruido aleatorio
    )
    
    return np.column_stack((customer_type, current_load, arrival_time)), wait_time

# Generar datos
X, y = generate_data()

# Dividir en entrenamiento y prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
