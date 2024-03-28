from tkinter import *

raiz = Tk()
LabelFrame = Frame(raiz, width=400, height=400)
LabelFrame.pack()

Image = PhotoImage(file="C:\\Users\\chpal\\OneDrive\\Escritorio\\Código\\Desarrollo de interfaces\\Python\\corazon.png")

# En caso de que un label no lo vayamos a utilizar mas, podemos juntarlo con el 'place' de la siguiente manera: Label(LabelFrame, text="Probando Labels", fg="red", font=("Calibri", 18)).place(x=100, y=200)
labelText = Label(LabelFrame, text="Probando Labels")
labelText.place(x=150, y=180)
labelText.config(foreground="#393E41")
labelText.config(font=("Calibri", 12))

# Si queremos que el label sea una imagen en vez de texto, se hace lo siguiente ->
Label(LabelFrame, image=Image).place(x=150, y=180)


raiz.mainloop()