class Persona:
    def __init__(self, nombre, edad, profesion, grado):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.grado = grado

    def presentarse(self):
        print (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.profesion} y estudio {self.grado}.")
    
Carlos = Persona("Carlos", 22, "Estudiante", "Matematicas")
Carlos.presentarse()