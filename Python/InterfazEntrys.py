from tkinter import *

def configurar_etiqueta(etiqueta):
    etiqueta.config(background="#393E41", foreground="#F1FEC6", font="Calibri")
    
def buttonFunctionality():
    myName.set("Chanti")

raiz = Tk()

FrameEntrys = Frame(raiz, width=800, height=400)
FrameEntrys.pack()
FrameEntrys.config(background="#393E41", padx=25, pady=25)

myName = StringVar()

cuadroName = Entry(FrameEntrys, textvariable=myName)
cuadroName.grid(row=0, column=1, padx=10)

cuadroEmail = Entry(FrameEntrys)
cuadroEmail.grid(row=1, column=1, padx=10)

cuadroPassword = Entry(FrameEntrys)
cuadroPassword.grid(row=2, column=1, padx=10)
cuadroPassword.config(show="*")

cuadroComents = Text(FrameEntrys, width=15, height=5)
cuadroComents.grid(row=3, column=1, padx=10, pady=10)

scrollVert = Scrollbar(FrameEntrys, command=cuadroComents.yview)
scrollVert.grid(row=3, column=2)
cuadroComents.config(yscrollcommand=scrollVert.set)

nameLabel = Label(FrameEntrys, text="Nombre:")
nameLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

emailLabel = Label(FrameEntrys, text="Email:")
emailLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)

passwordLabel = Label(FrameEntrys, text="Contraseña:")
passwordLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)

comentsLabel = Label(FrameEntrys, text="Comentários:")
comentsLabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)

configurar_etiqueta(nameLabel)
configurar_etiqueta(emailLabel)
configurar_etiqueta(passwordLabel)
configurar_etiqueta(comentsLabel)

buttonRegister = Button(FrameEntrys, text="Registrarse", command=buttonFunctionality)
buttonRegister.grid(row=4, column=1)

raiz.mainloop()