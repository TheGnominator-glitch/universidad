from modelos.calificacion import Calificacion

class Matricula:
    def __init__(self, estudiante, curso):
        self.__estudiante = estudiante
        self.__curso = curso
        self.__calificaciones = []

    def get_estudiante(self):
        return self.__estudiante

    def get_curso(self):
        return self.__curso

    def agregar_calificacion(self, actividad, nota):
        self.__calificaciones.append(Calificacion(actividad, nota))

    def get_calificaciones(self):
        return self.__calificaciones

    def promedio(self):
        if len(self.__calificaciones) == 0:
            return 0.0
        total = 0.0
        for calificacion in self.__calificaciones:
            total += calificacion.get_nota()
        return total / len(self.__calificaciones)

    def mostrar_info(self):
        print("Student:", self.__estudiante.get_nombre())
        print("Course:", self.__curso.get_nombre())
        print("Average:", self.promedio())
        for calificacion in self.__calificaciones:
            calificacion.mostrar_info()
