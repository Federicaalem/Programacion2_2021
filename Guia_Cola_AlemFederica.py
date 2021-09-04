#Ejercicicio 3: Implementar en un archivo de python la clase cola vista en clase
class Cola:
    """La cola es una coleccion de datos lineales, FIFO (First in First out)"""
    def __init__(self):
      self.elementos = []
      
    def agregar(self, item):
        self.elementos.append(item)

    def es_vacia(self)->bool: 
        return self.elementos == []

    def primero(self): # fijarse que no este vacia
        if not self.es_vacia():
            return self.elementos[0]

    def tamanio(self):
        return len(self.elementos)

    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)
        
    def __str__(self):
        return ("{}".format(self.elementos))
"""
p = Cola() # crea una cola (vacia)
print(p.es_vacia()) #True
p.agregar(4) # 
p.agregar('perro')
print(p.elementos) # [4,'perro']
print(p.primero()) # 4
p.agregar(True) # [4,'perro',true]
print(p.tamanio()) # 3
print(p.es_vacia()) #False
p.agregar(8.4) # [4,'perro',true,8.4]
print(p.sacar()) # imprime el 4 y lo saca
print(p.sacar()) # impreme perro y lo saca
print(p.tamanio()) # 2
"""
print()

# Ejercicio 4: 
# Agregar a la clase cola los siguientes métodos (usando preferentemente los métodos ya utilizados)
#    1. Imprimir cola
#    2. Vaciar la cola.
#    3. Dar vuelta cola

class Cola:
    """La cola es una coleccion de datos lineales, FIFO (First in First out)"""
    
    def __init__(self):
      self.elementos = []
      
    def agregar(self, item):
        self.elementos.append(item)

    def es_vacia(self)->bool: 
        return self.elementos == []

    def primero(self): # fijarse que no este vacia
        if not self.es_vacia():
            return self.elementos[0]

    def tamanio(self):
        return len(self.elementos)

    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)
        
    def __str__(self):
        return ("{}".format(self.elementos))
    
    #    1. Imprimir cola
    def imprimir_Cola(self):
        #elemento a elemento, de a uno.
        for i in self.elementos:
                 print(i)
    
    #    2. Vaciar la cola.
    def vaciar_Cola(self):       
        while self.es_vacia() != []:
            self.elementos.pop(0)
            if self.elementos == []:
                return True
            
    #    3. Dar vuelta cola
    def dar_vuelta(self):
        nuevaCola =[]
        
        while not self.es_vacia():                
            nuevaCola.append(self.sacar())
        
        for i in nuevaCola:
             self.elementos.insert(0, i)
             
             
p = Cola()
p.agregar(4)
p.agregar(2)
p.agregar(1)
assert p.primero() == 4
assert p.elementos == [4, 2, 1]
p.dar_vuelta()
assert p.elementos == [1, 2, 4]
assert p.sacar() == 1
assert p.primero() == 2
p.vaciar_Cola()
assert p.es_vacia() == True