
import tkinter as tk
from tkinter import messagebox

class PruebaExcepciones:
    @staticmethod
    def dividir(a, b):
        try:
            resultado = a / b
            return f"Resultado: {resultado}"
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."
        except ValueError:
            return "Error: Ingreso inválido. Debe ingresar números."
        except Exception as e:
            return f"Error inesperado: {str(e)}"

class ExcepcionesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Manejo de Excepciones")
        self.root.geometry("400x250")

        tk.Label(root, text="Ingrese el primer número:").pack(pady=5)
        self.entry_a = tk.Entry(root)
        self.entry_a.pack(pady=5)

        tk.Label(root, text="Ingrese el segundo número:").pack(pady=5)
        self.entry_b = tk.Entry(root)
        self.entry_b.pack(pady=5)

        tk.Button(root, text="Dividir", command=self.dividir_numeros).pack(pady=10)
        self.resultado_label = tk.Label(root, text="", fg="blue")
        self.resultado_label.pack(pady=5)

    def dividir_numeros(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            mensaje = PruebaExcepciones.dividir(a, b)
            self.resultado_label.config(text=mensaje)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcepcionesGUI(root)
    root.mainloop()