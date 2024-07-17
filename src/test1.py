import tkinter as tk
from tkinter import messagebox
from Controller.CrudDatabase import Crud

class CrudModule(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crud Module")
        self.geometry("500x300")
        self.resizable(False, False)
        self.transient(parent)  # Para mantener la ventana principal activa

        # Centrar la ventana
        self.center_window()

        self.crud = Crud()
        self.current_id = None

        self.create_widgets()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10)

        tk.Label(main_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.id_entry = tk.Entry(main_frame, state="disabled", width=10)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(main_frame, text="Pregunta:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.question_entry = tk.Entry(main_frame, width=50)
        self.question_entry.grid(row=0, column=3, padx=5, pady=5, columnspan=3)

        tk.Label(main_frame, text="Opciones y Respuesta:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.options_answer_entry = tk.Entry(main_frame, width=50)
        self.options_answer_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=4)

        self.data_listbox = tk.Listbox(main_frame, width=70, height=8)
        self.data_listbox.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        self.data_listbox.bind("<ButtonRelease-1>", self.fill_entries)

        action_frame = tk.Frame(main_frame)
        action_frame.grid(row=4, column=0, columnspan=5, pady=10)

        tk.Button(action_frame, text="Buscar", command=self.search_data, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Eliminar", command=self.delete_data, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Insertar", command=self.insert_data, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Actualizar", command=self.update_data, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Limpiar", command=self.clear_entries, width=10).pack(side=tk.LEFT, padx=5)

        self.show_all_data()

    def show_all_data(self):
        self.data_listbox.delete(0, tk.END)
        all_data = self.crud.getAllData()
        for data in all_data:
            self.data_listbox.insert(tk.END, f"ID: {data['Question'][0]}, Pregunta: {data['Question'][1]}")

    def search_data(self):
        id_to_search = self.id_entry.get()
        if id_to_search.strip().isdigit():
            data = self.crud.getData(int(id_to_search))
            if data:
                self.current_id = data["Question"][0]
                self.question_entry.insert(0, data["Question"][1])
                self.options_answer_entry.insert(0, data["Question"][2])
                if data["Answer"][0] is not None:
                    self.options_answer_entry.insert(tk.END, f", Respuesta: {data['Answer'][1]}")
            else:
                messagebox.showinfo("Error", f"No se encontró la pregunta con ID {id_to_search}")
        else:
            messagebox.showinfo("Error", "ID debe ser un número entero")

    def insert_data(self):
        queText = self.question_entry.get()
        options_answer = self.options_answer_entry.get()

        options = options_answer.split(", Respuesta:")[0].strip()
        ansText = options_answer.split(", Respuesta:")[1].strip() if ", Respuesta:" in options_answer else ""

        if queText and options:
            result = self.crud.setData(None, queText, options, ansText)
            if result:
                messagebox.showinfo("Éxito", "Datos insertados correctamente")
                self.clear_entries()
                self.show_all_data()
            else:
                messagebox.showinfo("Error", "Error al insertar los datos")
        else:
            messagebox.showinfo("Error", "Todos los campos son requeridos")

    def update_data(self):
        queText = self.question_entry.get()
        options_answer = self.options_answer_entry.get()

        options = options_answer.split(", Respuesta:")[0].strip()
        ansText = options_answer.split(", Respuesta:")[1].strip() if ", Respuesta:" in options_answer else ""

        if self.current_id and queText and options:
            result = self.crud.setData(self.current_id, queText, options, ansText)
            if result:
                messagebox.showinfo("Éxito", "Datos actualizados correctamente")
                self.clear_entries()
                self.show_all_data()
            else:
                messagebox.showinfo("Error", "Error al actualizar los datos")
        else:
            messagebox.showinfo("Error", "Todos los campos son requeridos y asegúrese de buscar primero")

    def delete_data(self):
        id_to_delete = self.id_entry.get()
        if id_to_delete.strip().isdigit():
            result = self.crud.dropData(int(id_to_delete))
            if result:
                messagebox.showinfo("Éxito", "Datos eliminados correctamente")
                self.clear_entries()
                self.show_all_data()
            else:
                messagebox.showinfo("Error", f"Error al eliminar los datos con ID {id_to_delete}")
        else:
            messagebox.showinfo("Error", "ID debe ser un número entero")

    def fill_entries(self, event):
        selected_index = self.data_listbox.curselection()
        if selected_index:
            selected_data = self.data_listbox.get(selected_index)
            id_to_fill = int(selected_data.split(":")[1].split(",")[0].strip())
            self.clear_entries()
            self.id_entry.insert(0, id_to_fill)
            self.search_data()

    def clear_entries(self):
        self.current_id = None
        self.id_entry.config(state="normal")
        self.id_entry.delete(0, tk.END)
        self.id_entry.config(state="disabled")
        self.question_entry.delete(0, tk.END)
        self.options_answer_entry.delete(0, tk.END)

class CustomWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Custom Window")
        self.geometry("400x300")
        self.transient(parent)  # Para mantener la ventana principal activa

        # Centrar la ventana
        self.center_window()

        self.create_widgets()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        tk.Label(self, text="Esta es tu ventana personalizada").pack(pady=20)
        tk.Button(self, text="Cerrar", command=self.destroy).pack(pady=20)

class StartPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Página de Inicio")
        self.geometry("400x200")
        self.resizable(False, False)

        # Centrar la ventana
        self.center_window()

        self.create_widgets()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        tk.Label(self, text="Bienvenido a la aplicación", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Abrir Crud Module", command=self.open_crud_module, width=20).pack(pady=10)
        tk.Button(self, text="Abrir Custom Window", command=self.open_custom_window, width=20).pack(pady=10)

    def open_crud_module(self):
        CrudModule(self)

    def open_custom_window(self):
        CustomWindow(self)

if __name__ == "__main__":
    app = StartPage()
    app.mainloop()
