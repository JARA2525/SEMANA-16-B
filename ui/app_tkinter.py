import tkinter as tk
from tkinter import messagebox


class AppTareas:
    def __init__(self, root, servicio):
        self.servicio = servicio
        self.root = root

        root.title("Lista de Tareas")

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        # Eventos teclado
        self.entry.bind("<Return>", self.agregar_evento)
        root.bind("c", self.completar_evento)
        root.bind("<Delete>", self.eliminar_evento)
        root.bind("<Escape>", lambda e: root.destroy())

        # Botones
        tk.Button(root, text="Añadir", command=self.agregar).pack()
        tk.Button(root, text="Completar", command=self.completar).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar).pack()

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack()

        # Doble clic
        self.lista.bind("<Double-1>", self.completar_evento)

    # EVENTOS
    def agregar_evento(self, event):
        self.agregar()

    def completar_evento(self, event):
        self.completar()

    def eliminar_evento(self, event):
        self.eliminar()

    # FUNCIONES
    def agregar(self):
        texto = self.entry.get()

        if texto == "":
            messagebox.showwarning("Error", "Ingrese una tarea")
            return

        self.servicio.agregar(texto)
        self.entry.delete(0, tk.END)
        self.actualizar()

    def completar(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        index = seleccion[0]
        tarea = self.servicio.listar()[index]

        self.servicio.completar(tarea.get_id())
        self.actualizar()

    def eliminar(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        index = seleccion[0]
        tarea = self.servicio.listar()[index]

        self.servicio.eliminar(tarea.get_id())
        self.actualizar()

    def actualizar(self):
        self.lista.delete(0, tk.END)

        for t in self.servicio.listar():
            texto = t.get_descripcion()

            if t.esta_completada():
                texto += " ✔"

            self.lista.insert(tk.END, texto)