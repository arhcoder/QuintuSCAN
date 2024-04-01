import tkinter as tk
from tkinter import messagebox

miventana = tk.Tk()
miventana.title("Botones y cajas de mensajes o dialogos")

def mensaje(): 
    #messagebox.showinfo("Información", "Primer mensaje")
    print("Hola")

btn1= tk.Button(miventana, text="Primer botón", command=mensaje)
#btn1.pack()
btn1.place(x=15, y=30)
miventana.geometry("300x300")

miventana.resizable(False, False)
miventana.mainloop()