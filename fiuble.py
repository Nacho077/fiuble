from tkinter import *
import wordle


raiz = Tk()
raiz.title("Wordle")
raiz.resizable(0,0)
# raiz.iconbitmap('')  hay que poner un icono

miFrame= Frame(raiz)
miFrame.pack()
miFrame.config(bg= '#121212', 
    width=500, height=800)

header = Label(miFrame, 
    text='FIUBLE', 
    fg='#D7DADC', # color de la fuente
    bg= '#121212', 
    font=('Cambria', 30)) # habria q encontrar una mejor fuente de texto 
header.grid(row=0, column=1, padx=100, columnspan=5)

labels = []

for i in range(5):
    for j in range(5):
        letter_label = Label(miFrame,
        fg='#D7DADC',
        bg= '#121212',
        font=('Cambria', 30),
        width=2,
        text="",
        justify=CENTER)
        letter_label.grid(row=i+1, column=j+1, pady=10)
        labels.append(letter_label)

def mismo_arriesgo(i):
    resultado = False 

    if i < 5:
        resultado = True

    if labels[i - 5]["bg"] != "#121212":
        resultado = True
            
    return resultado

def cambiar_label(tecla):
    if tecla.keysym == "Escape":
        raiz.destroy()
    else:
        i = 0
        label_vacio = False
        while i < len(labels) - 1 and not label_vacio:
            if labels[i]["text"] != "":
                i += 1
            else:
                label_vacio =True
        if tecla.keysym == "BackSpace":
            labels[i - 1]["text"] = ""
        elif mismo_arriesgo(i):
            labels[i]["text"] = tecla.keysym

def validar_arriesgo():
    arriesgo, index = traer_ultima_palabra()
    arriesgo = wordle.normalize(arriesgo)
    if wordle.validar_arriesgo(arriesgo):
        resultado = wordle.procesar_intento("CASAS", arriesgo)
        print(arriesgo, index, resultado)

def traer_ultima_palabra():
    i = 0
    while labels[i]["bg"] != "#121212":
        i += 5

    palabra = ""
    for j in range(5):
        palabra += labels[i + j]["text"]
    
    return[palabra, i]

boton_chequear_palabra = Button(miFrame,
    text='Probar intento', 
    fg='#D7DADC', # color de la fuente
    bg= '#121212', 
    font=('Cambria', 20),
    command=validar_arriesgo) # habria q encontrar una mejor fuente de texto 
boton_chequear_palabra.grid(row=7, column=2, padx=20, pady=20, columnspan=3)

raiz.bind_all("<KeyRelease>", cambiar_label)
raiz.mainloop()