from modelos.estudiante import Estudiante

class GestorEstudiantes:
    def __init__(self):
        self.__estudiantes = []

    def registrar(self, estudiante):
        for e in self.__estudiantes:
            if e.get_identificacion() == estudiante.get_identificacion():
                print("Student already exists")
                return
        self.__estudiantes.append(estudiante)
        print("Student registered:", estudiante.get_nombre())

    def buscar_por_id(self, identificacion):
        for e in self.__estudiantes:
            if e.get_identificacion() == identificacion:
                return e
        return None

    def listar_todos(self):
        if len(self.__estudiantes) == 0:
            print("No students registered")
        for e in self.__estudiantes:
            e.mostrar_info()

    def eliminar(self, identificacion):
        for e in self.__estudiantes:
            if e.get_identificacion() == identificacion:
                self.__estudiantes.remove(e)
                print("Student deleted:", identificacion)
                return