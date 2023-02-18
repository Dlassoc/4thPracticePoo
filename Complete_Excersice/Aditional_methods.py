class Estudiante:
    def __init__(self, id, nombre, nota):
        self.id = id
        self.nombre = nombre
        self.nota = nota

    def califications_to_0(self, nota):
        list_notes = [nota]
        for i in list_notes:
            if self.nota >= 3.0:
                break
            else:
                self.nota = 0

class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, id, nombre, nota):
        self.estudiantes.append(Estudiante(id, nombre, nota))

