class Libro:
    def __init__(self,propietario,read=False) -> None:
        self.propietario=propietario
        self.read=read

    def informar (self):
        if self.read==False:
            print ("Todavía no has leido el libro")
        else:
            print ("Libro ya leído")
        
    def setRead (self,nuevoValor):
        self.read=nuevoValor

    def setPropietario (self,nuevoValor):
        self.propietario=nuevoValor


libro1= Libro ("David")
libro2= Libro ("Luis",True)
libro3= Libro ("Angel",False)

print (f"Libro 1: {libro1.propietario}  leido: {libro1.read}")
print (f"Libro 2: {libro2.propietario}  leido: {libro2.read}")
libro1.informar()
libro1.setRead(True)
libro1.informar()
libro2.informar()