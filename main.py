import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTareas


def main():
    servicio = TareaServicio()
    root = tk.Tk()
    app = AppTareas(root, servicio)
    root.mainloop()


if __name__ == "__main__":
    main()