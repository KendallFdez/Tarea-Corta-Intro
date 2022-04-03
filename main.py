"""
Instituto Tecnológico De Costa Rica
Tarea corta Interfaz Gráfica
Profesor:Jeff Schmidt Peralta
Estudiante:Kendall Fernández Obando
Curso:Taller de Programación
Semeste 1 2022
"""
#Librerias
import tkinter as tk
from threading import Thread
from tkinter import messagebox
from timeit import default_timer

#Funciones
def mensaje():
	answer=messagebox.askyesno("Salir", "¿Desea Salir?")
	if(answer):
		ventana.destroy()
#fib:calcula el número n de la sucesión de Fibonacci
#e:n
#s:fib(n)
#r:n es un entero positivo
def fib():
    num1=(cuadronum.get())
    if isinstance(num1,int) and num1 >= 0:
        return fib_aux(num1)
    else:
        return "Debe ser un número entero positivo"
def fib_aux(num):
    if num == 0 or num == 1: 
        return numfib.set(fib)
    else:
        return fib_aux(num - 1) + fib_aux(num - 2)
"""ifib=default_timer()
fib()
ffib=default_timer()
tiempo=(ffib-ifib)"""

#Colores
negro="#4B4848"
naranja="#C57C37"
verdeLima="#B1CC14"
gris="#A5A5A5"

#Ventanas
ventana=tk.Tk()
ventana.title("Tarea Corta Kendall")
ventana.geometry("700x550")
ventana.resizable(False,False)
ventana.iconbitmap("icono.ico")

#Canvas 
panel_canvas = tk.Canvas(ventana, width=234, height=556, borderwidth=0, highlightthickness=0, bg=verdeLima)
panel_canvas.place(x=0, y=0)
anim_canvas = tk.Canvas(ventana, width=466, height=556, borderwidth=0, highlightthickness=0, bg=negro)
anim_canvas.place(x=236, y=0)

#Entry
numfib=tk.StringVar()
num0=tk.Label(panel_canvas,text="Inserte su número",font=("Times",18),bg=negro,fg="white")
num0.place(x=25,y=135)  
cuadronum=tk.Entry(panel_canvas)
cuadronum.place(x=50,y=175)
res=tk.Label(panel_canvas,textvariable=numfib,font=("Times",18),bg=negro,fg="white")
res.place(x=25,y=210)

#Botón
boton=tk.Button(panel_canvas,text="Calcular",font=("fixedsys", "15"),bg=gris,command=())
boton.place(x=70, y=195)

#Menu
barraMenu=tk.Menu(ventana)
barraMenu.add_command(label="Fibonacci",)
barraMenu.add_command(label="Animación",)
barraMenu.add_command(label="Ficha Personal",)
barraMenu.add_command(label='Salir',command=mensaje)
ventana.config(menu=barraMenu)

#Mainloop   
ventana.mainloop()
