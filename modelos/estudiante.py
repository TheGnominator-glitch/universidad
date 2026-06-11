from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, identificacion, nombre, email, codigo, programa):
        super().__init__(identificacion, nombre, email)
        self.__codigo = codigo
        self.__programa = programa
        self.__promedio = 0.0

    def get_codigo(self):
        return self.__codigo

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        if not programa:
            raise ValueError("Program cannot be empty")
        self.__programa = programa

    def get_promedio(self):
        return self.__promedio

    def set_promedio(self, promedio):
        if promedio < 0.0 or promedio > 5.0:
            raise ValueError("Average must be between 0.0 and 5.0")
        self.__promedio = promedio

    def mostrar_info(self):
        print("Student:", self.get_nombre())
        print("ID:", self.get_identificacion())
        print("Email:", self.get_email())
        print("Code:", self.__codigo)
        print("Program:", self.__programa)
        print("Average:", self.__promedio)