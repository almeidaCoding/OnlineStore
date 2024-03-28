from tkinter import *

# Todas las propiedades que agregamos al frame, también podemos agregarlos a la raíz

raiz = Tk()
raiz.title("Register user")
raiz.iconbitmap("C:\\Users\\chpal\\OneDrive\\Escritorio\\Código\\Desarrollo de interfaces\\Python\\user.ico")
raiz.config(background="#CCD6EB")

FrameRegister = Frame()

# Ponerle 'side=right,left,bottom,top' al pack es para mover el frame dentro de la raíz de posición y ponerle 'anchor' es para moverlo en puntos cardinales (norte, sur, este, oeste). Si le colocamos a 'pack' la propiedad 'fill=x, y o both' y también 'expand=true' se va a rellenar toda la raíz o en horizontal, en vertical, o completa.
FrameRegister.pack()

FrameRegister.config(background="#393E41")
FrameRegister.config(width=400, height=300)
FrameRegister.config(border="35")
FrameRegister.config(relief="ridge")
FrameRegister.config(cursor="hand2")


# Para darle tamaño a un frame debemos quitar el tamaño de la raiz, ya que la raiz siempre se adaptará a su contenedor interno
# raiz.geometry("400x300")

# Este método no permite ensanchar la ventana en ninguna dirección
#raiz.resizable(0,0)

# El mainloop siempre debe estar de último
raiz.mainloop()