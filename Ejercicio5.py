import tkinter as tk
from tkinter import filedialog, messagebox
import os

class LeerArchivo:
    @staticmethod
    def leer_archivo(ruta):
        if not os.path.exists(ruta):
            raise FileNotFoundError("El archivo no existe.")
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.readlines()

    @staticmethod
    def leer_en_mayusculas(ruta):
        if not os.path.exists(ruta):
            raise FileNotFoundError("El archivo no existe.")
        with open(ruta, "r", encoding="utf-8") as archivo:
            return [linea.upper() for linea in archivo.readlines()]

class LeerArchivoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Archivos")
        self.root.geometry("600x400")

        tk.Label(root, text="Ruta del archivo:").pack(pady=5)
        self.entry = tk.Entry(root, width=60)
        self.entry.pack(pady=5)

        tk.Button(root, text="Buscar...", command=self.buscar_archivo).pack(pady=5)
        tk.Button(root, text="Leer Archivo", command=self.leer).pack(pady=5)
        tk.Button(root, text="Leer en Mayúsculas", command=self.leer_mayusculas).pack(pady=5)

        self.texto = tk.Text(root, wrap=tk.WORD, height=15, width=70)
        self.texto.pack(pady=10)

    def buscar_archivo(self):
        ruta = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
        if ruta:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, ruta)

    def leer(self):
        self.mostrar_contenido(LeerArchivo.leer_archivo)

    def leer_mayusculas(self):
        self.mostrar_contenido(LeerArchivo.leer_en_mayusculas)

    def mostrar_contenido(self, funcion):
        self.texto.delete(1.0, tk.END)
        ruta = self.entry.get()
        try:
            lineas = funcion(ruta)
            for linea in lineas:
                self.texto.insert(tk.END, linea)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LeerArchivoGUI(root)
    root.mainloop()