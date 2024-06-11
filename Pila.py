class Stack: 

    def __init__(self) -> None: 
        self.__elements = [] 

    def push(self, element): 
        """Agrega elementos"""
        self.__elements.append(element)

    def pop(self): 
        """Saca el elemento de arriba"""
        if len(self.__elements) > 0 :
            return self.__elements.pop() 
        else:
            return None

    def on_top(self): 
        """Muestra el elemento de arriba"""
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        """Muestra el tamaño de la pila"""
        return len(self.__elements)

