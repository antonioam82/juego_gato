from tkinter import *
from tkinter import messagebox
import random
import time
from tkinter import simpledialog


ventana=Tk()
ventana.title("Tres en Raya")
ventana.geometry("390x450")
turno=0

boton0=Button(ventana,width=9,height=3)
boton0.place(x=50,y=50)
boton1=Button(ventana,width=9,height=3)
boton1.place(x=150,y=50)
boton2=Button(ventana,width=9,height=3)
boton2.place(x=250,y=50)
boton3=Button(ventana,width=9,height=3)
boton3.place(x=50,y=150)
boton4=Button(ventana,width=9,height=3)
boton4.place(x=150,y=150)
boton5=Button(ventana,width=9,height=3)
boton5.place(x=250,y=150)
boton6=Button(ventana,width=9,height=3)
boton6.place(x=50,y=250)
boton7=Button(ventana,width=9,height=3)
boton7.place(x=150,y=250)
boton8=Button(ventana,width=9,height=3)
boton8.place(x=250,y=250)
turnoE=Label(ventana).place(x=120,y=20)
iniciar=Button(ventana,bg="dark blue",fg="white",text="Iniciar Juego",width=15,height=3).place(x=130,y=350)

ventana.mainloop()
