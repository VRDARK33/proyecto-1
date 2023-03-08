from tkinter import * # Se importa el módulo 'tkinter' para crear interfaces gráficas de usuario
import tkinter as tk # Se importa el módulo 'tkinter' bajo el alias 'tk'

def impresion(resultados_busqueda):
    ventana = Tk() # Se crea una instancia de la clase 'Tk' para crear una ventana principal
    ventana.title("RESULTADOS") # Se establece el título de la ventana
    ventana.iconbitmap("virus.ico") # Se establece el icono de la ventana

    # Crear un widget Canvas con una barra de desplazamiento vertical
    canvas = Canvas(ventana)
    scrollbar = Scrollbar(ventana, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Agregar el widget Canvas a la ventana principal
    canvas.pack(side="left", fill="both", expand=True)

    # Crear un frame dentro del widget Canvas para contener el contenido
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Agregar el contenido al frame
    columna = resultados_busqueda.columns
    y = 0
    for x in range(len(columna)):
        if columna[x] == "ubicacion" or columna[x] == "departamento_nom" or columna[x] == "ciudad_municipio_nom" or columna[x] == "edad" or columna[x] == "fuente_tipo_contagio" or columna[x] == "estado" or columna[x] == "tipo_recuperacion":
            columnas =Label(frame,text=f" {columna[x]} ")
            columnas.grid(row=0, column=y)
            y = y + 1

    z = 0
    for j in range (len(resultados_busqueda)):
        for i in range (len(resultados_busqueda.columns)):
            if columna[i] == "ubicacion" or columna[i] == "departamento_nom" or columna[i] == "ciudad_municipio_nom" or columna[i] == "edad" or columna[i] == "fuente_tipo_contagio" or columna[i] == "estado" or columna[i] == "tipo_recuperacion":
                fila = Label(frame,text=f"{resultados_busqueda.iloc[j][i]}")
                fila.grid(row=j+1, column=z)
                z = z + 1
            if i >= 18:
                i = 0
                z = 0
            else:                                               
                i+=1

    # Configurar el tamaño del widget Canvas y el frame interno
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.config(width=600, height=400)
    ventana.mainloop() # Se inicia el bucle de eventos de la ventana principal
