import tkinter as tk
from tkinter import messagebox
import re # Módulo para expresiones regulares, usado en la validación

# ==============================================================================
# 1. Clases de Excepción Personalizadas
# ==============================================================================

class ErrorEquipoLleno(Exception):
    """Excepción generada cuando se intenta añadir un programador a un equipo lleno."""
    pass

class ErrorCampoInvalido(Exception):
    """Excepción base para errores de validación de campos (nombre/apellido)."""
    pass

class ErrorCampoContieneDigitos(ErrorCampoInvalido):
    """Excepción generada cuando un campo contiene dígitos."""
    pass

class ErrorCampoLongitudExcedida(ErrorCampoInvalido):
    """Excepción generada cuando la longitud de un campo es >= 20 caracteres."""
    pass

# ==============================================================================
# 2. Clases de Modelo
# ==============================================================================

class Programador:
    """Modela un integrante de un equipo de programadores. Posee nombre y apellidos."""
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class EquipoMaratonProgramacion:
    """Modela un equipo de programadores para una maratón."""
    
    # El equipo está conformado por varios programadores, mínimo dos y máximo tres.
    MIN_PROGRAMADORES = 2
    MAX_PROGRAMADORES = 3

    def __init__(self, nombreEquipo: str, universidad: str, lenguajeProgramacion: str):
        """
        Constructor que inicializa los atributos del equipo.
        El array de programadores se inicializa con capacidad máxima.
        """
        self.nombreEquipo = nombreEquipo
        self.universidad = universidad
        self.lenguajeProgramacion = lenguajeProgramacion
        # Inicializa una lista (equivalente al array) con capacidad para MAX_PROGRAMADORES
        self.programadores: list[Programador] = []
        self.tamañoEquipo = 0 # El tamaño del equipo inicialmente es cero

    def está_lleno(self) -> bool:
        """Determina si el equipo ha alcanzado el número máximo de programadores (3)."""
        return self.tamañoEquipo == self.MAX_PROGRAMADORES

    def está_completo(self) -> bool:
        """Determina si el equipo tiene el número mínimo (2) o máximo (3) de programadores."""
        return self.tamañoEquipo >= self.MIN_PROGRAMADORES

    def añadir(self, programador: Programador):
        """
        Añade un programador al equipo.
        :param programador: El objeto Programador a agregar.
        :raises ErrorEquipoLleno: Si el equipo ya tiene 3 programadores.
        """
        if self.está_lleno():
            raise ErrorEquipoLleno("El equipo está completo (3/3). No se pudo agregar programador.")
        
        # Se añade el programador a la lista
        self.programadores.append(programador)
        self.tamañoEquipo += 1
    
    @staticmethod
    def validar_campo(campo: str):
        """
        Valida que el campo:
        1. Solo contenga texto (no dígitos).
        2. Tenga una longitud estrictamente menor a 20 caracteres.
        :param campo: El string (nombre o apellido) a validar.
        :raises ErrorCampoContieneDigitos: Si el campo tiene dígitos.
        :raises ErrorCampoLongitudExcedida: Si la longitud es >= 20.
        """
        if not campo.strip(): # Verifica si el campo está vacío o solo tiene espacios
            # Se puede lanzar una excepción de campo vacío si se desea, pero el requerimiento es sobre dígitos y longitud
            return 

        # 1. Validar que no contenga dígitos (usando expresión regular)
        if re.search(r'\d', campo):
            raise ErrorCampoContieneDigitos(f"El campo '{campo}' no puede tener dígitos.")

        # 2. Validar longitud (no se permiten >= 20)
        if len(campo) >= 20:
            raise ErrorCampoLongitudExcedida(f"La longitud de '{campo}' ({len(campo)} caracteres) no debe ser superior a 20.")


# ==============================================================================
# 3. Clase de Interfaz Gráfica (Tkinter)
# ==============================================================================

class AppMaraton(tk.Tk):
    """Clase principal de la aplicación con Interfaz Gráfica (GUI)."""
    def __init__(self):
        super().__init__()
        self.title("Registro de Equipo de Programación")
        self.geometry("450x550")
        
        # Objeto para el equipo
        self.equipo: EquipoMaratonProgramacion = None
        
        self.crear_widgets()
        self.mostrar_paso_1()

    def crear_widgets(self):
        """Crea y organiza los componentes de la interfaz."""
        
        # --- Variables de control ---
        self.var_nombre_equipo = tk.StringVar()
        self.var_universidad = tk.StringVar()
        self.var_lenguaje = tk.StringVar()
        self.var_nombre_prog = tk.StringVar()
        self.var_apellidos_prog = tk.StringVar()

        # --- Frames para organizar los pasos ---
        self.frame_paso1 = tk.Frame(self, padx=10, pady=10) # Datos del equipo
        self.frame_paso2 = tk.Frame(self, padx=10, pady=10) # Datos del programador

        # --- Paso 1: Datos del Equipo ---
        tk.Label(self.frame_paso1, text="Registro del Equipo", font=('Arial', 14, 'bold')).pack(pady=10)
        
        tk.Label(self.frame_paso1, text="Nombre del Equipo:").pack(anchor='w', pady=(5, 0))
        tk.Entry(self.frame_paso1, textvariable=self.var_nombre_equipo, width=50).pack()
        
        tk.Label(self.frame_paso1, text="Universidad:").pack(anchor='w', pady=(5, 0))
        tk.Entry(self.frame_paso1, textvariable=self.var_universidad, width=50).pack()
        
        tk.Label(self.frame_paso1, text="Lenguaje de Programación:").pack(anchor='w', pady=(5, 0))
        tk.Entry(self.frame_paso1, textvariable=self.var_lenguaje, width=50).pack()
        
        tk.Button(self.frame_paso1, text="Crear Equipo y Continuar", command=self.crear_equipo).pack(pady=20)

        # --- Paso 2: Datos de Programadores ---
        self.lbl_paso2_titulo = tk.Label(self.frame_paso2, text="Añadir Programador (1/3)", font=('Arial', 14, 'bold'))
        self.lbl_paso2_titulo.pack(pady=10)

        tk.Label(self.frame_paso2, text="Nombre del Programador:").pack(anchor='w', pady=(5, 0))
        tk.Entry(self.frame_paso2, textvariable=self.var_nombre_prog, width=50).pack()
        
        tk.Label(self.frame_paso2, text="Apellidos del Programador:").pack(anchor='w', pady=(5, 0))
        tk.Entry(self.frame_paso2, textvariable=self.var_apellidos_prog, width=50).pack()
        
        tk.Button(self.frame_paso2, text="Añadir Programador", command=self.añadir_programador).pack(pady=20)
        tk.Button(self.frame_paso2, text="Finalizar Registro (Mínimo 2)", command=self.finalizar_registro, bg='lightcoral').pack(pady=5)
        
        self.lbl_estado_equipo = tk.Label(self.frame_paso2, text="Programadores actuales: 0", fg='blue')
        self.lbl_estado_equipo.pack(pady=10)


    def mostrar_paso_1(self):
        """Muestra la interfaz para registrar los datos del equipo."""
        self.frame_paso2.pack_forget()
        self.frame_paso1.pack(expand=True, fill='both')

    def mostrar_paso_2(self):
        """Muestra la interfaz para registrar los programadores."""
        self.frame_paso1.pack_forget()
        self.frame_paso2.pack(expand=True, fill='both')
        self.actualizar_estado_programadores()

    def crear_equipo(self):
        """
        Crea el objeto EquipoMaratonProgramacion con los datos ingresados.
        """
        nombre = self.var_nombre_equipo.get().strip()
        universidad = self.var_universidad.get().strip()
        lenguaje = self.var_lenguaje.get().strip()
        
        if not all([nombre, universidad, lenguaje]):
            messagebox.showerror("Error de Datos", "Todos los campos del equipo son obligatorios.")
            return

        try:
            # Aunque el requisito no pide validación para estos campos, 
            # se podría añadir (e.g., que no estén vacíos)
            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
            messagebox.showinfo("Éxito", f"Equipo '{nombre}' creado. ¡Añade los programadores!")
            self.mostrar_paso_2()
        except Exception as e:
            messagebox.showerror("Error al Crear Equipo", str(e))

    def actualizar_estado_programadores(self):
        """Actualiza el texto del estado de los programadores en la GUI."""
        if self.equipo:
            self.lbl_estado_equipo.config(text=f"Programadores actuales: {self.equipo.tamañoEquipo}")
            self.lbl_paso2_titulo.config(text=f"Añadir Programador ({self.equipo.tamañoEquipo + 1}/{self.equipo.MAX_PROGRAMADORES})")
        
        # Deshabilita el botón de añadir si el equipo está lleno
        if self.equipo and self.equipo.está_lleno():
            self.lbl_paso2_titulo.config(text="Equipo Completo (3/3)", fg='red')
            # Busca el botón "Añadir Programador" y lo deshabilita
            for widget in self.frame_paso2.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget('text') == "Añadir Programador":
                    widget.config(state=tk.DISABLED)
                    break
        else:
            # Habilita el botón si no está lleno
            for widget in self.frame_paso2.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget('text') == "Añadir Programador":
                    widget.config(state=tk.NORMAL)
                    break
    
    def añadir_programador(self):
        """
        Valida y añade un programador al equipo.
        """
        nombre_prog = self.var_nombre_prog.get().strip()
        apellidos_prog = self.var_apellidos_prog.get().strip()

        if not all([nombre_prog, apellidos_prog]):
            messagebox.showwarning("Advertencia", "El nombre y los apellidos del programador son obligatorios.")
            return

        try:
            # 1. Validar nombre y apellidos
            EquipoMaratonProgramacion.validar_campo(nombre_prog)
            EquipoMaratonProgramacion.validar_campo(apellidos_prog)
            
            # 2. Crear y añadir el programador
            programador = Programador(nombre_prog, apellidos_prog)
            self.equipo.añadir(programador)
            
            # 3. Éxito y limpieza
            messagebox.showinfo("Éxito", f"Programador {nombre_prog} añadido al equipo.")
            self.var_nombre_prog.set("") # Limpiar campos
            self.var_apellidos_prog.set("")
            self.actualizar_estado_programadores() # Actualizar contador en la GUI
            
        except ErrorEquipoLleno as e:
            messagebox.showerror("Error de Capacidad", str(e))
        except ErrorCampoContieneDigitos as e:
            messagebox.showerror("Error de Validación", str(e))
        except ErrorCampoLongitudExcedida as e:
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error Desconocido", f"Ocurrió un error inesperado: {str(e)}")

    def finalizar_registro(self):
        """
        Verifica el tamaño mínimo del equipo y finaliza el registro.
        """
        if not self.equipo:
            messagebox.showwarning("Advertencia", "Primero debe crear el equipo.")
            return

        if self.equipo.tamañoEquipo < self.equipo.MIN_PROGRAMADORES:
            messagebox.showwarning("Advertencia", f"El equipo debe tener un mínimo de {self.equipo.MIN_PROGRAMADORES} programadores. Actualmente tiene {self.equipo.tamañoEquipo}.")
            return
        
        # Registro exitoso, muestra la información final del equipo
        integrantes = "\n".join([f"- {p.nombre} {p.apellidos}" for p in self.equipo.programadores])
        
        messagebox.showinfo(
            "Registro Finalizado", 
            f"✅ ¡Equipo '{self.equipo.nombreEquipo}' registrado con éxito!\n\n"
            f"Universidad: {self.equipo.universidad}\n"
            f"Lenguaje: {self.equipo.lenguajeProgramacion}\n"
            f"Total de Programadores: {self.equipo.tamañoEquipo}\n\n"
            f"Integrantes:\n{integrantes}"
        )
        self.destroy() # Cierra la aplicación


# --- Ejecución del programa principal ---
if __name__ == "__main__":
    app = AppMaraton()
    app.mainloop()