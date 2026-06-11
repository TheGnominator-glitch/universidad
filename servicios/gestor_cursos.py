from modelos.curso import Curso
from modelos.matricula import Matricula

class GestorCursos:
    def __init__(self):
        self.__cursos = []
        self.__matriculas = []

    def registrar_curso(self, curso):
        for c in self.__cursos:
            if c.get_codigo() == curso.get_codigo():
                print("Curso ya existe")
                return
        self.__cursos.append(curso)
        print("Curso registrado:", curso.get_nombre())

    def buscar_curso(self, codigo):
        for c in self.__cursos:
            if c.get_codigo() == codigo:
                return c
        return None

    def listar_cursos(self):
        if len(self.__cursos) == 0:
            print("No hay cursos registrados")
        for c in self.__cursos:
            c.mostrar_info()

    def matricular(self, estudiante, curso):
        for m in self.__matriculas:
            if m.get_estudiante().get_identificacion() == estudiante.get_identificacion() and m.get_curso().get_codigo() == curso.get_codigo():
                print("Estudiante ya esta en este curso")
                return
        matricula = Matricula(estudiante, curso)
        self.__matriculas.append(matricula)
        print(estudiante.get_nombre(), "inscrito en", curso.get_nombre())

    def buscar_matricula(self, identificacion_estudiante, codigo_curso):
        for m in self.__matriculas:
            if m.get_estudiante().get_identificacion() == identificacion_estudiante and m.get_curso().get_codigo() == codigo_curso:
                return m
        return None

    def listar_matriculas(self):
        if len(self.__matriculas) == 0:
            print("No hay matriculas registrados")
        for m in self.__matriculas:
            m.mostrar_info()