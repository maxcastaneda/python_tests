from tkinter import *
import random
import datetime
from tkinter import messagebox, filedialog

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]
operador = ""

def click_boton(valor):
    global operador
    operador = operador + valor
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)

def obtenerresultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, resultado)
    operador = ""

def revisar_check():
    x=0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            c.config(state=NORMAL)
            if c.get() == "0":
                c.delete(0, END)
                c.focus()
        else:
            c.config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1

    x=0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            c.config(state=NORMAL)
            if c.get() == "0":
                c.delete(0, END)
                c.focus()
        else:
            c.config(state=DISABLED)
            texto_bebida[x].set("0")
        x += 1    

    x=0
    for c in cuadros_postre:
        if variables_postre[x].get() == 1:
            c.config(state=NORMAL)
            if c.get() == "0":
                c.delete(0, END)
                c.focus()
        else:
            c.config(state=DISABLED)
            texto_postre[x].set("0")
        x += 1            

# caclular total
def total():
    sub_total_comida = 0
    sub_total_bebida = 0
    sub_total_postre = 0
    for x in range(len(lista_comidas)):
        sub_total_comida += float(texto_comida[x].get()) * precios_comida[x]
    for x in range(len(lista_bebidas)):
        sub_total_bebida += float(texto_bebida[x].get()) * precios_bebida[x]
    for x in range(len(lista_postres)):
        sub_total_postre += float(texto_postre[x].get()) * precios_postres[x]

    var_costo_comida.set(f"${round(sub_total_comida,2)}")
    var_costo_bebida.set(f"${round(sub_total_bebida,2)}")
    var_costo_postre.set(f"${round(sub_total_postre,2)}")

    subtotal = sub_total_comida + sub_total_bebida + sub_total_postre
    var_costo_subtotal.set(f"${round(subtotal,2)}")

    impuestos = subtotal * 0.16
    var_costo_impuestos.set(f"${round(impuestos,2)}")

    total = subtotal + impuestos
    var_costo_total.set(f"${round(total,2)}")

def recibo():
    total()
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000,9999)}"
    fecha_recibo = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    texto_recibo.insert(END, "Antojitos Mexicanos \"El burro alegre\"\n")    
    texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t {fecha_recibo}\n")
    texto_recibo.insert(END, f"*"*45+"\n")
    texto_recibo.insert(END, "Item\t\tCantidad\t\tTotal\n")
    texto_recibo.insert(END, f"-"*59+"\n")
    for x in range(len(lista_comidas)):
        if int(texto_comida[x].get()) > 0:
            texto_recibo.insert(INSERT, f"{lista_comidas[x]}\t\t {texto_comida[x].get()}\t\t${round(float(texto_comida[x].get()) * precios_comida[x],2)}\n")
    for x in range(len(lista_bebidas)):
        if int(texto_bebida[x].get()) > 0:
            texto_recibo.insert(INSERT, f"{lista_bebidas[x]}\t\t {texto_bebida[x].get()}\t\t${round(float(texto_bebida[x].get()) * precios_bebida[x],2)}\n")
    for x in range(len(lista_postres)):
        if int(texto_postre[x].get()) > 0:
            texto_recibo.insert(INSERT, f"{lista_postres[x]}\t\t {texto_postre[x].get()}\t\t${round(float(texto_postre[x].get()) * precios_postres[x],2)}\n")

    texto_recibo.insert(END, f"*"*45+"\n")
    texto_recibo.insert(INSERT, f"Comida: {var_costo_comida.get()}\n")
    texto_recibo.insert(INSERT, f"Bebida: {var_costo_bebida.get()}\n")
    texto_recibo.insert(INSERT, f"Postre: {var_costo_postre.get()}\n")
    texto_recibo.insert(END, f"*"*45+"\n")
    texto_recibo.insert(INSERT, f"Subtotal: {var_costo_subtotal.get()}\n")
    texto_recibo.insert(INSERT, f"Impuestos: {var_costo_impuestos.get()}\n")
    texto_recibo.insert(INSERT, f"Total: {var_costo_total.get()}\n")
    texto_recibo.insert(INSERT, "Gracias, vuelva prontos\n")

def guardar():
    recibo()
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(
        mode="w",
        defaultextension=".txt",
        title="Guardar recibo", filetypes=(("Archivos de texto", "*.txt"),))
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Guardado", "El recibo ha sido guardado con exito")

def resetear():
    for x in range(len(lista_comidas)):
        texto_comida[x].set("0")
    for x in range(len(lista_bebidas)):
        texto_bebida[x].set("0")
    for x in range(len(lista_postres)):
        texto_postre[x].set("0")
    for c in cuadros_comida:
        c.config(state=DISABLED)
    for c in cuadros_bebida:
        c.config(state=DISABLED)
    for c in cuadros_postre:
        c.config(state=DISABLED)
    for ck in variables_comida:
        ck.set(0)
    for ck in variables_bebida:
        ck.set(0)
    for ck in variables_postre:
        ck.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_costo_subtotal.set("")
    var_costo_impuestos.set("")
    var_costo_total.set("")
    texto_recibo.delete(1.0, END)

application = Tk()

# configuraciones de la pantalla
application.geometry("1024x768")
application.resizable(0, 0)
application.title("Mi Restaurante - Sistema de facuracion")
application.config(bg="khaki4")

# panel
panel_superior = Frame(application, relief=FLAT, )
panel_superior.pack(side=TOP, fill=X)

# etiqueta titulo
etiqueta_titulo = Label(
                        panel_superior, 
                        text="Antojitos Mexicanos \"El burro alegre\"", 
                        fg="white",
                        font=("Dubai Light", 24),   
                        bg="black" ,                                 
                        height=2
                        )
etiqueta_titulo.pack(fill=X)

# panel izquierdo
panel_izquierdo = Frame(application, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT,fill=Y)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=50)
panel_costos.pack(side=BOTTOM, fill=X)

# panel_comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Dubai Light",15,"bold"), bd=1, relief=FLAT, fg="gray25")
panel_comidas.pack(side=LEFT, padx=10, pady=10)

# panel_bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dubai Light",15,"bold"), bd=1, relief=FLAT, fg="gray25")
panel_bebidas.pack(side=LEFT, padx=10, pady=10)

# panel_postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dubai Light",15,"bold"), bd=1, relief=FLAT, fg="gray25")
panel_postres.pack(side=LEFT, padx=10, pady=10)

# panel derecha
panel_derecho = Frame(application, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT, fill=Y)

# panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="khaki4")
panel_calculadora.pack(side=TOP, fill=X)

# panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg="khaki4")
panel_recibo.pack(fill=X)

# panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="khaki4")
panel_botones.pack(side=BOTTOM, fill=X)

# lista de productos
lista_comidas = ["Flautas", "Chimichangas", "Sopes", "Gorditas", "Tlayuda", "Tampiqueña", "Arrachera", "Fajitas de pollo"]
lista_bebidas = ["Limonada", "Agua de Fresa", "Agua de Jamainca", "Agua de Horchata", "Tecate Light", "Indio", "Carta balnca", "Tequila"]
lista_postres = ["Helado de Chocolate","Helado de Fresa","Plato de fruta","Pastel Tres Leches","Gansito","Pinguinos","Glorias","Alfajores"]


# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comidastr in lista_comidas:
    # crear check buttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comidastr, font=("Dubai Light",11), onvalue=1, offvalue=0, variable=variables_comida[contador], command=revisar_check)
    comida.grid(row=contador, column=0, sticky=W)
    #crear cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, font=("Dubai Light",11), bd=1, width=4, state=DISABLED, textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1


# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebidastr in lista_bebidas:
    # crear check buttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebidastr, font=("Dubai Light",11), onvalue=1, offvalue=0, variable=variables_bebida[contador], command=revisar_check)
    bebida.grid(row=contador, column=0, sticky=W)
    #crear cuadros de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=("Dubai Light",11), bd=1, width=4, state=DISABLED, textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1


# generar items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0
for postrestr in lista_postres:
    # crear check buttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postrestr, font=("Dubai Light",11), onvalue=1, offvalue=0, variable=variables_postre[contador], command=revisar_check)
    postre.grid(row=contador, column=0, sticky=W)
    #crear cuadros de entrada
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')    
    cuadros_postre[contador] = Entry(panel_postres, font=("Dubai Light",11), bd=1, width=4, state=DISABLED, textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1


# Etiquetas de costo y campos de entrada

#variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_costo_impuestos = StringVar()
var_costo_total = StringVar()

etiqueta_comida = Label(panel_costos, text="Costo Comida", font=("Dubai Light",13), bg="azure4", fg="white")
etiqueta_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos, font=("Dubai Light",13), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_bebida = Label(panel_costos, text="Costo bebida", font=("Dubai Light",13), bg="azure4", fg="white")
etiqueta_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos, font=("Dubai Light",13), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_postre = Label(panel_costos, text="Costo postre", font=("Dubai Light",13), bg="azure4", fg="white")
etiqueta_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos, font=("Dubai Light",13), bd=1, width=10, state='readonly', textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos, text="Subtotal", font=("Dubai Light",13), bg="azure4", fg="white")
etiqueta_subtotal.grid(row=0, column=2)
texto_costo_subtotal = Entry(panel_costos, font=("Dubai Light",13), bd=1, width=10, state='readonly', textvariable=var_costo_subtotal)
texto_costo_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos, text="Impuestos", font=("Dubai Light",13), bg="azure4", fg="white")
etiqueta_impuestos.grid(row=1, column=2)
texto_costo_impuestos = Entry(panel_costos, font=("Dubai Light",13), bd=1, width=10, state='readonly', textvariable=var_costo_impuestos)
texto_costo_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos, text="Total", font=("Dubai Light",13), bg="azure4", fg="white")
etiqueta_total.grid(row=2, column=2)
texto_costo_total = Entry(panel_costos, font=("Dubai Light",13), bd=1, width=10, state='readonly', textvariable=var_costo_total)
texto_costo_total.grid(row=2, column=3, padx=41)


#botones
botones = ["total","recibo","guardar","resetear"]
botones_guardados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones, text=boton.title(), font=("Dubai Light",13), bg="azure4", fg="white", width=9, bd=1)
    boton.grid(row=0, column=columnas, padx=2, pady=2)
    columnas += 1
    botones_guardados.append(boton)

botones_guardados[0].config(command=total)
botones_guardados[1].config(command=recibo)
botones_guardados[2].config(command=guardar)
botones_guardados[3].config(command=resetear)

# recibo
texto_recibo = Text(panel_recibo, font=("Dubai Light",12), bd=1, width=40, height=10)
texto_recibo.grid(row=0, column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora, font=("Dubai Light",13), bd=1, width=40)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# botones calculadora
botones_calculadora = [
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "C","<","0","/"
]
botones_guardados = []
fila=1
columna=0
for boton in botones_calculadora:
    boton = Button(panel_calculadora, text=boton, font=("Dubai Light",13), bg="azure4", fg="white", width=8, bd=1)    
    boton.grid(row=fila, column=columna, padx=2, pady=2)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1
    botones_guardados.append(boton)

botones_guardados[0].config(command=lambda: click_boton("7"))
botones_guardados[1].config(command=lambda: click_boton("8"))
botones_guardados[2].config(command=lambda: click_boton("9"))
botones_guardados[3].config(command=lambda: click_boton("+"))
botones_guardados[4].config(command=lambda: click_boton("4"))
botones_guardados[5].config(command=lambda: click_boton("5"))
botones_guardados[6].config(command=lambda: click_boton("6"))
botones_guardados[7].config(command=lambda: click_boton("-"))
botones_guardados[8].config(command=lambda: click_boton("1"))
botones_guardados[9].config(command=lambda: click_boton("2"))
botones_guardados[10].config(command=lambda: click_boton("3"))
botones_guardados[11].config(command=lambda: click_boton("*"))
botones_guardados[12].config(command=lambda: obtenerresultado())
botones_guardados[13].config(command=lambda: borrar())
botones_guardados[14].config(command=lambda: click_boton("0"))
botones_guardados[15].config(command=lambda: click_boton("/"))

# evitar que la ventana se cierra.
application.mainloop()


