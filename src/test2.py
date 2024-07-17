import tkinter as tk

class Form(tk.Canvas):
    
    @staticmethod
    def configs(cls):
        cls.config(
            width=500,
            height=300,
            bg='white'
        )

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configs(self)
        self.pack(expand=True, fill='both')
        self.frames = {}  # Diccionario para almacenar los frames
        print("Form: width=500, height=300")

    def add_frame(self, frame_class, name):
        """Agrega un frame al canvas"""
        frame = frame_class(self)
        frame.config(width=500, height=300)
        frame.grid_propagate(False)  # Evitar que el frame cambie de tamaño automáticamente
        frame.pack_propagate(False)  # Evitar que el frame cambie de tamaño automáticamente
        self.frames[name] = frame
        self.create_window(0, 0, anchor="nw", window=frame)

    def show_frame(self, name):
        """Muestra el frame con el nombre especificado"""
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()
        else:
            print(f"Frame '{name}' no encontrado.")

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cambio de Frames")
        self.geometry("500x300")

        self.form = Form(self)

        # Agregar frames al Form
        self.form.add_frame(StartPage, "StartPage")
        self.form.add_frame(CrudModule, "CrudModule")
        self.form.add_frame(CustomWindow, "CustomWindow")

        # Mostrar la página de inicio
        self.form.show_frame("StartPage")

class StartPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Página de Inicio", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Abrir CrudModule", command=lambda: self.master.show_frame("CrudModule")).pack(pady=10)
        tk.Button(self, text="Abrir CustomWindow", command=lambda: self.master.show_frame("CustomWindow")).pack(pady=10)

class CrudModule(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Este es el módulo CRUD", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Volver a Inicio", command=lambda: self.master.show_frame("StartPage")).pack(pady=10)

class CustomWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Esta es la ventana personalizada", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Volver a Inicio", command=lambda: self.master.show_frame("StartPage")).pack(pady=10)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
