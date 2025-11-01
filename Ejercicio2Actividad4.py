# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 15:37:25 2025

@author: Caro
"""

import tkinter as tk
from tkinter import messagebox

class Vendedor:
    # Atributos: nombre, apellidos, edad
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    # Muestra los datos del vendedor
    def imprimir(self):
        info = f"Nombre del vendedor = {self.nombre}\n"
        info += f"Apellidos del vendedor = {self.apellidos}\n"
        info += f"Edad del vendedor = {self.edad}"
        messagebox.showinfo("Datos del vendedor", info)

    # Verifica que la edad sea válida
    def verificarEdad(self, edad):
        if 0 < edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        elif edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        else:
            self.edad = edad


#Las excepciones IllegalArgumentException usadas en Java se reemplazaron por ValueError, que es la más similar en Python.

def crear_vendedor():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    try:
        edad = int(entry_edad.get())
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return

    vendedor = Vendedor(nombre, apellidos)
    try:
        vendedor.verificarEdad(edad)
        vendedor.imprimir()
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Ventana principal
root = tk.Tk()
root.title("Clase Vendedor")

# Etiquetas y campos
tk.Label(root, text="Nombre del vendedor:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Apellidos del vendedor:").grid(row=1, column=0, padx=5, pady=5)
entry_apellidos = tk.Entry(root)
entry_apellidos.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Edad del vendedor:").grid(row=2, column=0, padx=5, pady=5)
entry_edad = tk.Entry(root)
entry_edad.grid(row=2, column=1, padx=5, pady=5)

# Botón
tk.Button(root, text="Crear Vendedor", command=crear_vendedor).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
