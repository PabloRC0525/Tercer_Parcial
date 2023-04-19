from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorDB import *

#Instancia: Puente entre los 2 archivos
controlador = ControladorDB()

#Metodo que usa mi obj controlador para insertar

def ejecutaInsert():
    controlador.guardarUsuario(varNum.get(),varSal.get())
    
def ejecutaSelect():
    rUsu= controlador.consultarUsuario(varBus.get())
    for usu in rUsu:
        cadena= str(usu[0])+" "+str(usu[1])+" "+str(usu[2])

    if(rUsu): 
        textBus.config(state='normal')
        textBus.delete(1.0, 'end')
        textBus.insert('end', cadena)
        textBus.config(state='disabled') 
    else:
        messagebox.showerror("Error","El usuario no existe en la base de datos")
        
def ejecutaconsulta():
    rUsu= controlador.consulta()
    tabla.delete(*tabla.get_children())
    for usu in rUsu:
        tabla.insert('', 'end', text=usu[0], values=(usu[1], usu[2]))

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

#Pestaña 2: Buscar Cuenta
titulo2 = Label(pestaña2,text="Buscar Cuenta:",fg ="green",font=("Modern",18)).pack()

varBus=tk.StringVar()
lblid= Label(pestaña2,text="Identificador de la Cuenta:")
txtid= Entry(pestaña2,textvariable=varBus).pack()
btnBusqueda= Button(pestaña2,text="Buscar",command=ejecutaSelect).pack()

subBus= Label(pestaña2,text= "Registrado:",fg="blue",font=("Modern",15)).pack()
textBus = tk.Text(pestaña2, height=5, width=52)
textBus.pack() 

#Pestaña 3: Consultar usuarios

subUS= Label(pestaña3,text= "Usuarios:",fg="blue",font=("Modern",15)).pack()
tabla = ttk.Treeview(pestaña3)
tabla['columns'] = ('numero', 'saldo')
tabla.column('#0', width=50, minwidth=50)
tabla.column('numero', width=120, minwidth=120)
tabla.column('saldo', width=150, minwidth=150)

tabla.heading('#0', text='ID', anchor=tk.CENTER)
tabla.heading('numero', text='No. Cuenta', anchor=tk.CENTER)
tabla.heading('saldo', text='Saldo', anchor=tk.CENTER)
tabla.pack() 


#Pestaña 4: Eliminar usuario
titulo3 = Label(pestaña4,text="Eliminar Usuario:",fg ="red",font=("Modern",18))
titulo3.pack()

varElim = tk.StringVar()
lblidE = Label(pestaña4,text="Identificador de usuario:")
lblidE.pack()
txtidE = Entry(pestaña4,textvariable=varElim)
txtidE.pack()

btnElimina = Button(pestaña4,text="Eliminar usuario", command=ejecutadelete)
btnElimina.pack()

mensajeAE = tk.StringVar()
lblMensajeAE = Label(pestaña4, textvariable=mensajeAE)
lblMensajeAE.pack()
Consultar= Button(pestaña3,text="Consultar",command=ejecutaconsulta).pack()
panel.add(pestaña1,text="Formulario Cuentas")
panel.add(pestaña2,text="Buscar Cuenta")
panel.add(pestaña3,text="Consultar usuarios")
panel.add(pestaña4,text="Eliminar")



ventana.mainloop()