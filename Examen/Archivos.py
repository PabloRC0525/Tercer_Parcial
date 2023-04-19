from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorDB import *

#Instancia: Puente entre los 2 archivos
controlador = ControladorDB()

#Metodo que usa mi obj controlador para insertar

def ejecutaInsert():
    controlador.guardarUsuario(varNum.get(),varSal.get())
#Metodo que usa mi obj controlador para buscar un usuario
        
def ejecutaconsulta():
    # Obtiene los usuarios de la base de datos
    rUsu= controlador.consulta()
    # Borra los datos existentes en la tabla
    tabla.delete(*tabla.get_children())
    # Inserta los nuevos datos en la tabla
    for usu in rUsu:
        tabla.insert('', 'end', text=usu[0], values=(usu[1], usu[2], usu[3]))
    
def ejecutadelete():
    controlador.eliminar(varElim.get())
 
 

ventana = Tk()
ventana.title("Cuentas")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)

#Pestaña 1: Formulario de registro
titulo = Label(pestaña1,text="Registro de cuenta",fg="blue",font=("Modern",18)).pack()
varNum = tk.StringVar()
lblNum = Label(pestaña1,text="Numero de Cuenta: ").pack()
txtNum = Entry(pestaña1,textvariable=varNum).pack()
varSal = tk.StringVar()
lblSal = Label(pestaña1,text="Saldo inicial: ").pack()
txtSal = Entry(pestaña1,textvariable=varSal).pack()

btnGuard = Button(pestaña1,text="Guardar usuario",command = ejecutaInsert).pack()


#Pestaña 2: Consultar usuarios

subUS= Label(pestaña2,text= "Usuarios:",fg="blue",font=("Modern",15)).pack()
tabla = ttk.Treeview(pestaña2)
tabla['columns'] = ('numero', 'saldo')
tabla.column('#0', width=50, minwidth=50)
tabla.column('numero', width=120, minwidth=120)
tabla.column('saldo', width=150, minwidth=150)

tabla.heading('#0', text='ID', anchor=tk.CENTER)
tabla.heading('numero', text='No. Cuenta', anchor=tk.CENTER)
tabla.heading('saldo', text='Saldo', anchor=tk.CENTER)
tabla.pack() 

Consultar= Button(pestaña2,text="Consultar",command=ejecutaconsulta).pack()
#Pestaña 4: Eliminar usuario
titulo3 = Label(pestaña4,text="Eliminar Usuario:",fg ="red",font=("Modern",18))
titulo3.pack()

varElim = tk.StringVar()
lblidE = Label(pestaña4,text="Identificador de Cuenta:")
lblidE.pack()
txtidE = Entry(pestaña4,textvariable=varElim)
txtidE.pack()

btnElimina = Button(pestaña4,text="Eliminar usuario", command=ejecutadelete)
btnElimina.pack()

mensajeAE = tk.StringVar()
lblMensajeAE = Label(pestaña4, textvariable=mensajeAE)
lblMensajeAE.pack()

panel.add(pestaña1,text="Formulario Cuentas")
panel.add(pestaña2,text="Consultar usuarios")
panel.add(pestaña3,text="Actualizar")
panel.add(pestaña4,text="Eliminar")



ventana.mainloop()