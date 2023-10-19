import tkinter as tk
from tkinter import messagebox
import os
import re

def es_entero_valido(valor):
    return valor.isdigit()

def es_decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_entero_valido_de_10_digitos(valor):
    return len(valor) == 10 and valor.isdigit()

def es_texto_valido(valor):
    return bool(re.match(r'^[a-zA-Z\s]+$', valor))

def validar_edad():
    if not es_entero_valido(edad_var.get()):
        messagebox.showerror("Error", "Por favor, ingrese una edad válida")
        edad_var.set("")

def validar_estatura():
    if not es_decimal_valido(estatura_var.get()):
        messagebox.showerror("Error", "Por favor, ingrese una estatura válida")
        estatura_var.set("")

def validar_telefono():
    input_value = telefono_var.get()
    if len(input_value) < 10:
        messagebox.showerror("Error", "Por favor, ingrese un número de teléfono válido de 10 dígitos")
        telefono_var.set("")

def validar_nombre_apellidos(valor):
    if not es_texto_valido(valor):
        messagebox.showerror("Error", "Por favor, ingrese un valor válido (sólo letras y espacios)")
        return ""

def guardar_datos():
    nombres = nombre_var.get()
    apellidos = apellidos_var.get()
    telefono = telefono_var.get()
    estatura = estatura_var.get()
    edad = edad_var.get()
    genero = genero_var.get()

    if genero == 1:
        genero = "Hombre"
    elif genero == 2:
        genero = "Mujer"
    else:
        genero = ""

    if (es_entero_valido(edad) and es_decimal_valido(estatura) and es_entero_valido_de_10_digitos(telefono) and
            es_texto_valido(nombres) and es_texto_valido(apellidos)):

        datos = f"Nombres: {nombres}\nApellidos: {apellidos}\nTeléfono: {telefono}\nEstatura: {estatura}\nEdad: {edad}\nGénero: {genero}"

        ruta_archivo = "datos.txt"
        archivo_existe = os.path.exists(ruta_archivo)

        if not archivo_existe:
            with open(ruta_archivo, "w") as archivo:
                archivo.write(datos)
        else:
            with open(ruta_archivo, "a") as archivo:
                archivo.write("\n" + datos)

        messagebox.showinfo("Información", f"Datos guardados con éxito\n\n{datos}")
    else:
        messagebox.showerror("Error", "Por favor, ingrese datos válidos en los campos.")

app = tk.Tk()
app.title("Formulario")
app.geometry("400x300")

nombre_label = tk.Label(app, text="Nombres:")
nombre_label.pack()
nombre_var = tk.StringVar()
nombre = tk.Entry(app, textvariable=nombre_var)
nombre.pack()
nombre_var.trace_add("write", lambda *args: validar_nombre_apellidos(nombre_var.get()))

apellidos_label = tk.Label(app, text="Apellidos:")
apellidos_label.pack()
apellidos_var = tk.StringVar()
apellidos = tk.Entry(app, textvariable=apellidos_var)
apellidos.pack()
apellidos_var.trace_add("write", lambda *args: validar_nombre_apellidos(apellidos_var.get()))

telefono_label = tk.Label(app, text="Teléfono:")
telefono_label.pack()
telefono_var = tk.StringVar()
telefono = tk.Entry(app, textvariable=telefono_var)
telefono.pack()
telefono_var.trace_add("write", lambda *args: validar_telefono())

estatura_label = tk.Label(app, text="Estatura:")
estatura_label.pack()
estatura_var = tk.StringVar()
estatura = tk.Entry(app, textvariable=estatura_var)
estatura.pack()
estatura_var.trace_add("write", lambda *args: validar_estatura())

edad_label = tk.Label(app, text="Edad:")
edad_label.pack()
edad_var = tk.StringVar()
edad = tk.Entry(app, textvariable=edad_var)
edad.pack()
edad_var.trace_add("write", lambda *args: validar_edad())

genero_var = tk.IntVar()
genero_label = tk.Label(app, text="Género:")
genero_label.pack()

genero_hombre = tk.Radiobutton(app, text="Hombre", variable=genero_var, value=1)
genero_mujer = tk.Radiobutton(app, text="Mujer", variable=genero_var, value=2)
genero_hombre.pack()
genero_mujer.pack()

guardar_button = tk.Button(app, text="Guardar", command=guardar_datos)
guardar_button.pack()

limpiar_button = tk.Button(app, text="Limpiar", command=lambda: [entry.delete(0, tk.END) for entry in [nombre, apellidos, telefono, estatura, edad]])
limpiar_button.pack()

app.mainloop()
