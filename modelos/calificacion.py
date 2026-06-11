class Calificacion:
    def __init__(self, actividad, nota):
        self.__actividad = actividad
        self.__nota = None
        self.set_nota(nota)

    def get_actividad(self):
        return self.__actividad

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        if nota < 0.0 or nota > 5.0:
            raise ValueError("Nota debe ser entre 0.0 y 5.0")
        self.__nota = nota

    def mostrar_info(self):
        print("Actividad:", self.__actividad)
        print("Nota:", self.__nota)