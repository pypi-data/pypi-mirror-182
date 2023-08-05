#         ◦ tipo: tomará el valor “Triángulo”
#         ◦ lados: asígnale el valor 3
#         ◦ base: asígnale el valor 0
#         ◦ altura: asígnale el valor 0
# Crea un objeto tipo “triangulo” y muestra por pantalla el valor de sus cuatro propiedades.

class Triangulo:
    def __init__(self,tipo="Triangulo",lados=3,base=0,altura=0) -> None:
        self.tipo=tipo
        self.lados=lados
        self.base=base
        self.altura=altura
    
    def area(self):
        resultado =self.base*self.altura/2
        return resultado
  


tri1=Triangulo ()
tri2=Triangulo ("Triangulo",3,33,3)

print ("/***** TRIANGULO 1 ******/")
print (f"Tipo: {tri1.tipo}")
print (f"Lados: {tri1.lados}")
print (f"Base: {tri1.base} Altura:{tri1.altura}")
print (f"Area es {tri1.area()}")
print ()

print ("/***** TRIANGULO 2 ******/")
print (f"Tipo: {tri2.tipo}")
print (f"Lados: {tri2.lados}")
print (f"Base: {tri2.base} Altura:{tri2.altura}")
print (f"Area es {tri2.area()}")

