import hashlib

# Función para calcular el hash de un dato (SHA-256)
def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Función para construir un árbol de Merkle a partir de una lista de datos
def build_merkle_tree(data_list):
    current_level = [calculate_hash(data) for data in data_list]
    level = 0
    print(f"Nivel {level}: {current_level}")
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            combined_hash = calculate_hash(left + right)
            next_level.append(combined_hash)
        current_level = next_level
        level += 1
        print(f"Nivel {level}: {current_level}")
    return current_level[0]

# Función para generar una prueba de Merkle para un elemento específico
def generate_merkle_proof(data_list, target):
    target_hash = calculate_hash(target)
    current_level = [calculate_hash(data) for data in data_list]
    proof = []
    level = 0
    print(f"Nivel {level}: {current_level}")
    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else left
            if target_hash == left:
                proof.append((right, "R"))
            elif target_hash == right:
                proof.append((left, "L"))
            combined_hash = calculate_hash(left + right)
            next_level.append(combined_hash)
        current_level = next_level
        level += 1
        print(f"Nivel {level}: {current_level}")
    print(f"Prueba generada: {proof}")
    return proof


# Función para verificar una prueba de Merkle
def verify_merkle_proof(target, proof, merkle_root):
    target_hash = calculate_hash(target)
    print(f"Hash inicial del objetivo: {target_hash}")
    for sibling, direction in proof:
        if direction == "L":
            target_hash = calculate_hash(sibling + target_hash)
        else:
            target_hash = calculate_hash(target_hash + sibling)
        print(f"Hash actualizado: {target_hash}")
    print(f"Raíz calculada: {target_hash}")
    return target_hash == merkle_root


# Ejemplo de uso
data_list = ["user1@example.com", "user2@example.com", "user3@example.com", "user4@example.com"]

# Construir el árbol de Merkle
merkle_root = build_merkle_tree(data_list)
print("Raíz de Merkle:", merkle_root)

# Generar una prueba de Merkle para un elemento
target = "user4@example.com"
proof = generate_merkle_proof(data_list, target)
print("Prueba de Merkle para", target, ":", proof)

# Verificar la prueba de Merkle
is_valid = verify_merkle_proof(target, proof, merkle_root)
print("¿La prueba es válida?", is_valid)
