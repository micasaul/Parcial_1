# criterios de orden
def by_name(item):
    """Ordena por nombre como key"""
    return item['name']

def by_name_ll(item):
    """Ordena por nombre como key en lista de lista"""
    return item[0]['nombre']

def by_height(item):
    """Ordena por otros criterios"""
    return item['altura']

def by_species(item):
    """Ordena por otros criterios"""
    return item['species']

# busqueda elementos compuestos
def search (lista, criterio, value):
    """Busco elementos en los criterios"""
    for index, elemento in enumerate(lista):
        if elemento[criterio]== value:
            return index

# eliminar elemento de la lista
def remove(lista, criterio, value):
    """Elimino un elemento"""
    index= search(lista, criterio, value)
    if index is not None:
        return lista.pop(index)
    
# barrido
def show_list(title, list_values):
    """Barrido de lista"""
    print()
    print(title)
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()

def show_list_list(title, subtitle, list_values):
    """Barrido de lista de lista"""
    print()
    print(title)
    for index, elemento in enumerate(list_values):
        print(index, elemento["nombre"], elemento["torneos_ganados"], elemento["batallas_perdidas"], elemento["batallas_ganadas"])
        print(f"   {subtitle}")
        for second_index, second_element in enumerate(elemento['sublist']):
            print(f"   {second_index, second_element}")
    print()