class Usuario:
 def __init__(self, nombre, password):
    self.nombre = nombre
    self.__password = password

def get_password(self):
    return self.__password

def set_password(self, password):
        self.__password = password

# Creamos un objeto Usuario
usuario = Usuario("johndoe", "mypassword")

# Mostramos sus propiedades
print(usuario.nombre)
print(usuario.get_password())

# Intentamos acceder directamente a la contraseña
# print(usuario.__password)   # Esto lanzará un error

# Modificamos la contraseña usando el setter
usuario.set_password("newpassword")
print(usuario.get_password())
