from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.contador = 1

    def agregar(self, descripcion):
        tarea = Tarea(self.contador, descripcion)
        self.tareas.append(tarea)
        self.contador += 1

    def listar(self):
        return self.tareas

    def completar(self, id):
        for t in self.tareas:
            if t.get_id() == id:
                t.completar()

    def eliminar(self, id):
        self.tareas = [t for t in self.tareas if t.get_id() != id]