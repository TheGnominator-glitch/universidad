from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, identificacion, nombre, email):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__email = email

    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not nombre:
            raise ValueError("Nombre no puede estar vacio")
        self.__nombre = nombre

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if not email:
            raise ValueError("Email no puede estar vacio")
        self.__email = email

    @abstractmethod
    def mostrar_info(self):
        pass