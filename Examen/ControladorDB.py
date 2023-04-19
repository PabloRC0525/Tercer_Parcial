from tkinter import messagebox
import sqlite3

class ControladorDB:
    
    def __init__(self):
        pass
    
    def conexionDB (self):
        try:
            conexion = sqlite3.connect("C:/Users/Pablo/Documents/GitHub/Tercer_Parcial/Examen/BD_Banco.db")
            print("Conectado a la DB")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
    
    def guardarUsuario(self,num,sal):
        #1. llamo el metodo conexion
        conx = self.conexionDB()
        #2. Validar vacios
        if(num =="" or sal == ""):
            messagebox.showwarning("Aguas!!","Formulario incompleto")
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (num,sal)
            sqlInsert = "insert into TBCuentas(NoCuenta,Saldo) values (?,?)"
            
            #5. Ejecutamos el Insert y cerramos la conexion
            cursor.execute(sqlInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Cuenta creada")
        
    def consultarUsuario(self,id):
        #1. realizar conexion DB
        conx = self.conexionDB()
        #2. verificar que el id vacio
        if(id==""):
            messagebox.showwarning("Cuidado","Escribe un identificador")
        else:
            #3. Ejecutar la consulta
            try:
                #4. Preparamos lo necesario
                cursor=conx.cursor()
                sqlselect= "select * from TBCuentas where id ="+id
                #5. Ejecutamos y cerramos conexion
                cursor.execute(sqlselect)
                RSUsuario = cursor.fetchall()
                conx.close()
                return RSUsuario
                
            except sqlite3.OperationalError:
                print("Error de consulta")
                
    def consulta(self):
        #1. realizar conexion DB
        conx = self.conexionDB()
        try:
            #4. Preparamos lo necesario
            cursor=conx.cursor()
            sqlselect= "select * from TBCuentas"
            #5. Ejecutamos y cerramos conexion
            cursor.execute(sqlselect)
            RSUsuarios = cursor.fetchall()
            conx.close()
            return RSUsuarios
                
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def eliminar(self, id):
        conx = self.conexionDB()
        # 2. Validar vacios
        if(id==""):
            messagebox.showwarning("Error","Ingresa un ID")
        else:
            try:
                cursor = conx.cursor()
                cursor.execute("SELECT * FROM TBCuentas WHERE id=" + id)
                if cursor.fetchone() is None:
                    messagebox.showerror("Error", "El ID no existe")
                else:
                    sqldelete = "DELETE FROM TBCuentas WHERE id=?"
                    cursor.execute(sqldelete, id)
                    sqlupdate = "UPDATE TBCuentas SET id=id-1 WHERE id > ?"
                    cursor.execute(sqlupdate, id)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Exito", "Usuario eliminado exitosamente")
            except sqlite3.OperationalError:
                    print("Error al eliminar")