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
            raise ValueError("Grade must be between 0.0 and 5.0")
        self.__nota = nota

    def mostrar_info(self):
        print("Activity:", self.__actividad)
        print("Grade:", self.__nota)