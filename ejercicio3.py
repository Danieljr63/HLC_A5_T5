class Persona:
    def __init__(self, nombre, edad, profesion, grado):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.grado = grado
    def presentarse(self):
        print (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion}")
    
class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa = empresa
    def presentarse(self):
        print (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y trabajo de {self.empresa}")

Elena = Persona("Elena", 35, "Arquitecta", "Construcciones XYZ")
Elena.presentarse()