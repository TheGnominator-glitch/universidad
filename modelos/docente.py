from modelos.persona import Persona

class Docente(Persona):
    def __init__(self, identificacion, nombre, email, especialidad, titulo):
        super().__init__(identificacion, nombre, email)
        self.__especialidad = especialidad
        self.__titulo = titulo

    def get_especialidad(self):
        return self.__especialidad

    def set_especialidad(self, especialidad):
        if not especialidad:
            raise ValueError("Specialty cannot be empty")
        self.__especialidad = especialidad

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        if not titulo:
            raise ValueError("Title cannot be empty")
        self.__titulo = titulo

    def mostrar_info(self):
        print("Teacher:", self.get_nombre())
        print("ID:", self.get_identificacion())
        print("Email:", self.get_email())
        print("Specialty:", self.__especialidad)
        print("Title:", self.__titulo)
