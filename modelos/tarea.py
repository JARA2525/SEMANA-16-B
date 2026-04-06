class Tarea:
    def __init__(self, id, descripcion):
        self.__id = id
        self.__descripcion = descripcion
        self.__completada = False

    # GETTERS
    def get_id(self):
        return self.__id

    def get_descripcion(self):
        return self.__descripcion

    def esta_completada(self):
        return self.__completada

    # SETTERS
    def completar(self):
        self.__completada = True