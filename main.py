# Importamos las librerías que necesitamos
from tkinter import *
from api.importacion import *
from tkinter import messagebox
from ui.ui import *

# Definimos la función consultar
def consultar():
    # Obtenemos el valor del departamento y lo pasamos a mayúsculas
    dep = n_departamento.get().upper()
    # Obtenemos el valor del límite de registros
    lim = n_limites.get()
    
    # Realizamos la consulta a la base de datos
    results = base_de_datos(dep,lim)
    
    # Si no hay resultados, mostramos un mensaje de error
    if results.empty == True:
        messagebox.showinfo(message="no hay resultados de busqueda", title="error")
    # Si hay resultados, los mostramos en la ventana
    else:
        impresion(results)
    # Imprimimos los resultados por consola
    print(results)

# Creamos la ventana principal
ventana = Tk()
# Le damos un título a la ventana
ventana.title("CONSULTAS COVID-19 EN COLOMBIA")
# Definimos las dimensiones de la ventana
ventana.geometry("620x300")
# Definimos un ícono para la ventana
ventana.iconbitmap("virus.ico")
# Bloqueamos la opción de redimensionar la ventana
ventana.resizable(False,False)

# Creamos la etiqueta principal
etiqueta1 = Label(ventana, text="consulte aqui los contaminados de COVID-19",font="Arial 20")
etiqueta1.pack(fill= X,pady= 10)
etiqueta1.place(x=50,y=50)

# Creamos las etiquetas para los campos de entrada
etiqueta2 = Label(ventana, text="Departamentos",bd=4, bg="#5AEC0C",font=("Curier 10"))
etiqueta2.place(x=225, y=170)
etiqueta3 = Label(ventana, text="Limite de registros",bd=4, bg="#5AEC0C",font=("Curier 10"))
etiqueta3.place(x=350, y=170)

# Creamos los campos de entrada
n_departamento = Entry(ventana)
n_departamento.place(x=220,y=200)

n_limites = Entry(ventana)
n_limites.place(x=350,y=200)

# Creamos el botón de búsqueda
boton1 = Button(ventana,text="buscar",command=consultar, bg="#5AEC0C",height=1,width=11)
boton1.pack()
boton1.place(x=130,y=200)

# Iniciamos el loop principal de la ventana
ventana.mainloop()




