# -*- coding: utf-8 -*-

import math
import tkinter as tk
from tkinter import messagebox


class CalculosNumericos:

    @staticmethod
    def calcularLogaritmoNeperiano(valor):
        try:
            valor = float(valor)
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            return math.log(valor)
        except ArithmeticError:
            messagebox.showerror("Error", "El valor debe ser un número positivo para calcular el logaritmo")
        except ValueError:
            messagebox.showerror("Error", "El valor debe ser numérico para calcular el logaritmo")

    @staticmethod
    def calcularRaizCuadrada(valor):
        try:
            valor = float(valor)
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            return math.sqrt(valor)
        except ArithmeticError:
            messagebox.showerror("Error", "El valor debe ser un número positivo para calcular la raíz cuadrada")
        except ValueError:
            messagebox.showerror("Error", "El valor debe ser numérico para calcular la raíz cuadrada")


class VentanaPrincipal(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Cálculos Numéricos")
        self.geometry("400x300")

        # Etiquetas
        tk.Label(self, text="Número").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Logaritmo neperiano").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Raíz cuadrada").grid(row=2, column=0, padx=10, pady=10, sticky="e")

        # Campos de texto
        self.txtNumero = tk.Entry(self)
        self.txtLogaritmo = tk.Entry(self)
        self.txtRaiz = tk.Entry(self)
        self.txtNumero.grid(row=0, column=1)
        self.txtLogaritmo.grid(row=1, column=1)
        self.txtRaiz.grid(row=2, column=1)

        # Botones
        self.btnCalcular = tk.Button(self, text="Calcular", command=self.btnCalcularActionPerformed)
        self.btnLimpiar = tk.Button(self, text="Limpiar", command=self.btnLimpiarActionPerformed)
        self.btnCalcular.grid(row=3, column=0, pady=20)
        self.btnLimpiar.grid(row=3, column=1, pady=20)

        # Mensaje inferior
        self.txtMensaje = tk.Label(self, text="", fg="red")
        self.txtMensaje.grid(row=4, column=0, columnspan=2)

    def btnCalcularActionPerformed(self):
        numero = self.txtNumero.get()
        logaritmo = CalculosNumericos.calcularLogaritmoNeperiano(numero)
        raiz = CalculosNumericos.calcularRaizCuadrada(numero)

        try:
            numero_float = float(numero)
            if numero_float > 0:
                if logaritmo is not None and raiz is not None:
                    self.txtLogaritmo.delete(0, tk.END)
                    self.txtRaiz.delete(0, tk.END)
                    self.txtLogaritmo.insert(0, f"{logaritmo:.5f}")
                    self.txtRaiz.insert(0, f"{raiz:.5f}")
                    self.txtMensaje.config(text="")
        except ValueError:
            # No hace nada aquí porque el mensaje ya se mostró desde CalculosNumericos
            pass

    def btnLimpiarActionPerformed(self):
        self.txtNumero.delete(0, tk.END)
        self.txtLogaritmo.delete(0, tk.END)
        self.txtRaiz.delete(0, tk.END)
        self.txtMensaje.config(text="")


if __name__ == "__main__":
    ventana = VentanaPrincipal()
    ventana.mainloop()
