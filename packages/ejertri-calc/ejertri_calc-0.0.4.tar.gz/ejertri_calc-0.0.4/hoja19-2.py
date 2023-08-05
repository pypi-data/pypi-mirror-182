class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self._password = password

@Usuario
def password(self):
    return self._password

# Crear un objeto Usuario
usuario = Usuario("pepe","teta")

# Imprimir el nombre del usuario
print(usuario.nombre)

# Intentar imprimir el password del usuario directamente
# Esto generará un error porque la propiedad password es una propiedad de solo lectura
print(usuario.password)
