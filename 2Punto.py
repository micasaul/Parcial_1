# Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:

from Pila import Stack

dino_datos = Stack()

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },
  ]

for dino in dinosaurios:
    dino_datos.push(dino)

# a) Contar cuantas especies hay;
def especies (pila):
    dino_especies=[]
    aux= Stack()
    for i in range(pila.size()):
        dino = pila.pop()
        if dino['especie'] not in dino_especies:
            dino_especies.append(dino['especie'])
        aux.push(dino)
    print(f"hay {len(dino_especies)} especies de dinosaurios")
    return aux

# b) Determinar cuantos descubridores distintos hay;
def descubridores (pila):
    dino_descubridores=[]
    aux= Stack()
    for i in range(pila.size()):
        dino = pila.pop()
        if dino['descubridor'] not in dino_descubridores:
            dino_descubridores.append(dino['descubridor'])
        aux.push(dino)
    print(f"hay {len(dino_descubridores)} descubridores distintos")
    return aux

# c) Mostrar todos los dinosaurios que empiecen con T;
def dino_T (pila):
    aux=Stack()
    print("Los dinosaurios cuyos nombres empiezan con T son: ")
    for i in range (pila.size()):
        dino = pila.pop()
        if dino['nombre'][0] == "T":
            print(dino['nombre'])
        aux.push(dino)
    return aux

# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
def dino_275 (pila):
    aux=Stack()
    print("Los dinosaurios que pesan menos que 275 kg son: ")
    for i in range(pila.size()):
        dino=pila.pop()
        if dino['peso']<275:
            print(f"{dino['nombre']}, pesa {dino['peso']}")
        aux.push(dino)
    return aux    

# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
def dino_pila (pila):
    aux=Stack()
    a_q_s=Stack()
    for i in range(pila.size()):
        dino= pila.pop()
        if dino['nombre'][0]=="A" or dino['nombre'][0]=="Q" or dino['nombre'][0]=="S":
            a_q_s.push(dino)
        else:
            aux.push(dino)
    return aux, a_q_s

dino_datos=especies(dino_datos)
print()
dino_datos=descubridores(dino_datos)
print()
dino_datos=dino_T(dino_datos)
print()
dino_datos=dino_275(dino_datos)

dino_datos, dino_AQS = dino_pila(dino_datos)