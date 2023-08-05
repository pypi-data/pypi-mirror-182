#         ◦ tipo: tomará el valor “Triángulo”
#         ◦ lados: asígnale el valor 3
#         ◦ base: asígnale el valor 0
#         ◦ altura: asígnale el valor 0
# Crea un objeto tipo “triangulo” y muestra por pantalla el valor de sus cuatro propiedades.

class Triangulo:
    def __init__(self,tipo="Triangulo",lados=3,base=0,altura=0) -> None:
        self.tipo=tipo
        self.lados=lados
        self.__base=base
        self.__altura=altura
    
    def area(self):
        resultado =self.__base*self.__altura/2
        return resultado
    
    def setBase(self,nuevoValor):
        self.__base=nuevoValor

    def setAltura(self,nuevoValor):
        self.__altura=nuevoValor
        
    def getAltura(self):
        return self.__altura

    def getBase(self):
        return self.__base




tri1=Triangulo ()
tri2=Triangulo ("Triangulo",3,33,3)

print ("/***** TRIANGULO 1 ******/")
print (f"Tipo: {tri1.tipo}")
print (f"Lados: {tri1.lados}")
print (f"Base: {tri1.getBase()} Altura:{tri1.getAltura()}")
print (f"Area es {tri1.area()}")
print ()

#tri1.__altura=4
#tri1.__base=5

tri1.setBase(5)
tri1.setAltura(4)

print ("/***** TRIANGULO 1 ******/")
print (f"Tipo: {tri1.tipo}")
print (f"Lados: {tri1.lados}")
print (f"Base: {tri1.getBase()} Altura:{tri1.getAltura()}")
print (f"Area es {tri1.area()}")
print ()