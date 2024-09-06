import random
import string

def generar_letra_aleatoria():
    return random.choice(string.ascii_letters)

# Generar y mostrar una letra al azar
letra_aleatoria = generar_letra_aleatoria()
print("Letra aleatoria:", letra_aleatoria)