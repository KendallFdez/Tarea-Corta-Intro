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

#Funciones
def mensaje():
	answer=messagebox.askyesno("Salir", "¿Desea Salir?")
	if(answer):
		ventana.destroy()
#fib:calcula el número n de la sucesión de Fibonacci
#e:n
#s:fib(n)
#r:n es un entero positivo
def fib(num):
    if isinstance(num, int) and num >= 0:
        return fib_aux(num)
    else:
        return "Debe ser un número entero positivo"
def fib_aux(num):
    if num == 0 or num == 1: 
        return num
    else:
        return fib_aux(num - 1) + fib_aux(num - 2)
numfib=tk.StringVar()
num0=tk.Label(panel_canvas,text=numfib.get(),font=("Times",18),bg=verdeLima,fg=negro)
def getNum():
    num0.config(text=numfib.get())
    num0.place(x=70,y=200)
"""ifib=default_timer()
fib()
ffib=default_timer()
tiempo=(ffib-ifib)"""

#Entry
cuadronum=tk.Entry(panel_canvas,textvariable=numfib)
cuadronum.place(x=50,y=175)

#Botón
boton=tk.Button(panel_canvas,text="Calcular",font=("fixedsys", "15"),bg=gris,command=getNum())
boton.place(x=65, y=135)
#Menu
barraMenu=tk.Menu(ventana)
barraMenu.add_command(label="Fibonacci",)
barraMenu.add_command(label="Animación",)
barraMenu.add_command(label="Ficha Personal",)
barraMenu.add_command(label='Salir',command=mensaje)
ventana.config(menu=barraMenu)

#Mainloop   
ventana.mainloop()
