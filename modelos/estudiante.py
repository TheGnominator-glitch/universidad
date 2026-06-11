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
            raise ValueError("Programa no puede estar vacio")
        self.__programa = programa

    def get_promedio(self):
        return self.__promedio

    def set_promedio(self, promedio):
        if promedio < 0.0 or promedio > 5.0:
            raise ValueError("Promedio tiene que estar entre 0.0 y 5.0")
        self.__promedio = promedio

    def mostrar_info(self):
        print("Estudiante:", self.get_nombre())
        print("ID:", self.get_identificacion())
        print("Email:", self.get_email())
        print("Codigo:", self.__codigo)
        print("Programa:", self.__programa)
        print("Promedio:", self.__promedio)