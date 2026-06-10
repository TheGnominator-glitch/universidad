class Curso:
    def __init__(self, codigo, nombre, creditos, cupo_maximo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__cupo_maximo = cupo_maximo
        self.__docente = None

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not nombre:
            raise ValueError("Course name cannot be empty")
        self.__nombre = nombre

    def get_creditos(self):
        return self.__creditos

    def get_cupo_maximo(self):
        return self.__cupo_maximo

    def get_docente(self):
        return self.__docente

    def asignar_docente(self, docente):
        self.__docente = docente

    def mostrar_info(self):
        print("Course:", self.__nombre)
        print("Code:", self.__codigo)
        print("Credits:", self.__creditos)
        print("Max capacity:", self.__cupo_maximo)
        if self.__docente:
            print("Teacher:", self.__docente.get_nombre())
        else:
            print("Teacher: not assigned")
