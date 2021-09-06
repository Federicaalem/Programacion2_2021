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


print()
# Ejercicio 5:
# Escriba una función que reciba una Cola C1 y mueva sus elementos a una nueva Cola c2,
# manteniendo el orden de salida de los elementos. Al finalizar la Cola C1 no debe contener elementos.

def trasladar(c1)->Cola:
    
    c2 = Cola()

    for i in range (c1.tamanio()):
        c2.agregar(c1.sacar()) 

c1 = Cola()
c1.agregar("Federica")
c1.agregar("Romina")
#c2 = trasladar(c1)
trasladar(c1)

assert c1.es_vacia() == True


print()
# Ejercicio 6
""" Escriba un metodo de Cola que dada una cola C1 reciba una cola C2  de 
números enteros y devuelva una nueva Cola con los elementos concatenados en el 
orden C1 y C2. Es de destacar que las Colas recibidas no deben sufrir ningún 
tipo de cambio o alteración.(en principio utilizar los métodos de cola para la 
tarea)"""

class Cola:
    
    def __init__(self):
      self.elementos = []
      
      
    def agregar(self, item):
        self.elementos.append(item)


    def es_vacia(self)->bool: 
        return self.elementos == []


    def primero(self):
        if not self.es_vacia():
            return self.elementos[0]


    def tamanio(self):
        return len(self.elementos)


    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)
        
        
    def __str__(self):
        return ("{}".format(self.elementos))


    def imprimir_Cola(self):
       
        for i in self.elementos:
                 print(i)


    def vaciar_Cola(self):       
        while self.es_vacia() != []:
            self.elementos.pop(0)
            if self.elementos == []:
                return True            


    def dar_vuelta(self):
        nuevaCola =[]
        
        while not self.es_vacia():                
            nuevaCola.append(self.sacar())
        
        for i in nuevaCola:
             self.elementos.insert(0, i)
             
             
             
    def concat(self, c1,c2): # resultado = C1+C2
        res1 = []
        res2= []
        
        for i in range (c1.tamanio()): #en el rango del tamaño de c1
           
            res1.append(c1.sacar())
        
        c1.agregar(res1)
            
        for i in range (c2.tamanio()):
            
            res2.append(c2.sacar())
        
        c2.agregar(res2)
        
        resultado = res1 + res2
        print(c1)
        print(c2)
        return resultado
    
c1 = Cola()
c2 = Cola()
c3 = Cola()

c1.agregar(2)
c1.agregar(3)
c1.agregar(4)

c2.agregar(5)
c2.agregar(6)
c2.agregar(7)

assert c3.concat(c1,c2) == [2, 3, 4, 5, 6, 7]



print()
# Ejercicio 7
"""Escriba una rutina que reciba dos Colas C1 y C2 de números enteros y 
proceda a intercambiar sus elementos, manteniendo el orden de salida de los mismos.
 Al finalizar la rutina, la Cola C1 tendrá los elementos de la 
Cola C2 y ésta a su vez tendrá los elementos de la Cola C1."""

class Cola:
    
    def __init__(self):
      self.elementos = []
      
      
    def agregar(self, item):
        self.elementos.append(item)


    def es_vacia(self)->bool: 
        return self.elementos == []


    def primero(self):
        if not self.es_vacia():
            return self.elementos[0]


    def tamanio(self):
        return len(self.elementos)


    def sacar(self):
        if not self.es_vacia():
            return self.elementos.pop(0)
        
        
    def __str__(self):
        return ("{}".format(self.elementos))


    def imprimir_Cola(self):
       
        for i in self.elementos:
                 print(i)


    def vaciar_Cola(self):       
        while self.es_vacia() != []:
            self.elementos.pop(0)
            if self.elementos == []:
                return True            


    def dar_vuelta(self):
        nuevaCola =[]
        
        while not self.es_vacia():                
            nuevaCola.append(self.sacar())
        
        for i in nuevaCola:
             self.elementos.insert(0, i)
             
             
             
    def concat(self, c1,c2): # resultado = C1+C2
        res1 = []
        res2= []
        
        for i in range (c1.tamanio()): #en el rango del tamaño de c1
           
            res1.append(c1.sacar())
        
        c1.agregar(res1)
            
        for i in range (c2.tamanio()):
            
            res2.append(c2.sacar())
        
        c2.agregar(res2)
        
        resultado = res1 + res2

        return resultado
    
    
    def intercambiar(self, c2):
         intercambio = Cola()
         
         for i in range (c1.tamanio()):
             intercambio.agregar(c1.sacar())
            
             c1.agregar(c2.sacar())
        
         
#          #c2.agregar(intercambio)
         
             c2.agregar(intercambio.sacar())
         
         print(f"c1: {c1}")
         print(f"c2: {c2}")
         print(intercambio)
         
         return c1
    
c1= Cola()
c1.agregar(1)
c1.agregar(4)
c1.agregar(8)
# c1 = [1,4,8]

c2= Cola()
c2.agregar(4)
c2.agregar(2)
c2.agregar(7)
# c2 = [4,2,7]

c1.intercambiar(c2)
# c1 == [4,2,7]
# c2 == [1,4,8]




## Ejercicio 8
"""Dè una lista de ejemplos de problemas donde puede usarse una cola como sistema
de administración de la información y como podría pensarse un programa pensando estas ideas."""

"""
En un examen o practico para que aquel que primero entrego su trabajo pueda recibir primero la nota, y asi
sucesivamente.
Un programa donde controle la cola de entregas de trabajos, es decir el orden.

Con respecto actualmente serviria para las vacunas, aquel que se anoto pueda estar recibiendo su vacuna en orden.

Para un banco, gestor de turnos.
"""