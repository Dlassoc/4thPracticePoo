class Estudiante:
    def __init__(self, id, nombre, nota):
        self.id = id
        self.nombre = nombre
        self.nota = nota


class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, id, nombre, nota):
        self.estudiantes.append(Estudiante(id, nombre, nota))

    def notas_a_cero(self):
        for estudiante in self.estudiantes:
            if estudiante.nota > 3.0:
                break
            else:
                estudiante.nota = 0.0

    def nota_mediana(self, nota):
        suma = 0
        notas = []
        for estudiante in self.estudiantes:
            notas.append(estudiante.nota)
            suma += estudiante.nota
        mediana = suma/len(notas)
        return mediana


