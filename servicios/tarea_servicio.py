class TareaServicio:

    def __init__(self):
        self.tareas = []
        self.contador = 1

    def agregar(self, descripcion):
        tarea = {
            "id": self.contador,
            "descripcion": descripcion,
            "completada": False
        }
        self.tareas.append(tarea)
        self.contador += 1

    def completar(self, id):
        for t in self.tareas:
            if t["id"] == id:
                t["completada"] = True

    def eliminar(self, id):
        self.tareas = [t for t in self.tareas if t["id"] != id]

    def listar(self):
        return self.tareas