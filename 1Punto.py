# Desarrollar una función recursiva que permita listar los elementos de vector/lista de
# manera inversa al que están cargados. Preferentemente la función solo debe tener un
# parámetro que es la lista de elementos.

def inversa (vector):
    if len(vector)== 1:
        return vector
    else:
        return vector[-1:] + inversa(vector[:-1])
    
lista = ["gato", "sahumerio", "teclado", "chocolate"]
print(inversa(lista))