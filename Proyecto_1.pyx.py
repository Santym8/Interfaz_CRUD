from tkinter import *
from tkinter import messagebox
import sqlite3


#----------------------------------------------------------------------Funciones----------------------------


def Conexion():
    try:
        MiConexion=sqlite3.connect("Base de Datos")
        Cursor=MiConexion.cursor()
        Cursor.execute('''
        CREATE TABLE REGISTROS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(25),
            CONTRASEÑA VARCHAR(10),
            APELLIDO VARCHAR(25),
            DIRECCION VARCHAR(25),
            COMENTARIO VARCHAR(100))
        ''')
        messagebox.showinfo(title="Conexión", message="La base de datos se ha creado con ÉXITO")

    except:
        messagebox.showerror(title="Conexión", message="La base de datos ya existe")


    
def Salir():
    salir=messagebox.askyesno(title="SALIR", message="¿Desea cerrar la aplicación?")
    if salir == True:
        root.destroy()


def Licencia():
    messagebox.showinfo(title="Licencia", message="Producto de codigo abierto" )


def Ayuda():
    messagebox.showinfo(title="Ayuda", message='''-Para Agregar un nuevo registro a la base de datos, llene todos los campos y precione CREATE. 
    \n-Si desea Leer los campos de un registro ya creado llene unicamente el campo ID y presione READ
    \n-Si desea Actualizar un campo de un registro ya creado, primero llene el campo ID, presione READ, modifique la informacion y posteriormente pulse UPDATE
    \n-Si desea Eliminar un registro llene el campo ID, presione el boton DELETE''')



def Limpiar():
    Id.set("")
    Nombre.set("")
    Contraseña.set("")
    Apellido.set("")
    Direccion.set("")
    ComentarioText.delete(1.0,"end")



def Create():
    try:
        confirmacion=messagebox.askyesno(title="CREATE", message="¿Estas seguro?")
        if confirmacion == True:
            MiConexion=sqlite3.connect("Base de Datos")
            Cursor=MiConexion.cursor()
            registro=Nombre.get(),Contraseña.get(),Apellido.get(),Direccion.get(),ComentarioText.get("1.0",END)
            Cursor.execute("INSERT INTO REGISTROS VALUES (NULL,?,?,?,?,?)", registro)
            MiConexion.commit()
            Limpiar()
            messagebox.showinfo(title="CREATE", message="El registro se guardó con ÉXITO")
    except:
        messagebox.showerror(title="Base de Datos", message="Cree la conexion con la base de datos")



def Read():
    try:
        
        MiConexion=sqlite3.connect("Base de Datos")
        Cursor=MiConexion.cursor()
        Cursor.execute(f"SELECT * FROM REGISTROS WHERE ID={Id.get()}")
        Datos=Cursor.fetchall()
        MiConexion.commit()

        Limpiar()

        Id.set(str(Datos[0][0]))
        Nombre.set(str(Datos[0][1]))
        Contraseña.set(str(Datos[0][2]))
        Apellido.set(str(Datos[0][3]))
        Direccion.set(str(Datos[0][4]))
        ComentarioText.insert(1.0,str(Datos[0][5]))   
        return True
        
    except:
        messagebox.showerror(title="Read", message="ID no encontrado")
        return False


def Delete():

   if Read() == True:

         
        MiConexion=sqlite3.connect("Base de Datos")
        Cursor=MiConexion.cursor()
        if messagebox.askyesno(title="Delete", message="¿Estas seguro?")==True:
            Cursor.execute(f"DELETE FROM REGISTROS WHERE ID={Id.get()}")
            MiConexion.commit()
            Limpiar()
            messagebox.showinfo(title="Delete", message="Registro eliminado")



def Update():
    MiConexion=sqlite3.connect("Base de Datos")
    Cursor=MiConexion.cursor()
    registro=Nombre.get(),Contraseña.get(),Apellido.get(),Direccion.get(),ComentarioText.get("1.0",END)
    Cursor.execute(f"UPDATE REGISTROS SET NOMBRE= ?, CONTRASEÑA= ?, APELLIDO=?, DIRECCION=?, COMENTARIO=? WHERE ID='{Id.get()}'", registro)
    MiConexion.commit()
    messagebox.showinfo(title="Update", message="SE ha actualizado el registro con exito")




#--------------------------------------------------------------------------Interfaz Grafica--------------------
root= Tk()
root.title("Proyecto Bases de Datos")

                                   
frame_1=Frame(root)
frame_1.pack()

#------------------------------------------------Textos
IDLabel=Label(frame_1, text="ID")
IDLabel.grid(row=0, column=0, padx=10, pady=10)

NombreLabel=Label(frame_1, text="Nombre")
NombreLabel.grid(row=1, column=0, padx=10, pady=10)

ContraseñaLabel=Label(frame_1, text="Contraseña")
ContraseñaLabel.grid(row=2, column=0, padx=10, pady=10)

ApellidoLabel=Label(frame_1, text="Apellido")
ApellidoLabel.grid(row=3, column=0, padx=10, pady=10)

DireccionLabel=Label(frame_1, text="Dirección")
DireccionLabel.grid(row=4, column=0, padx=10, pady=10)

ComentarioLabel=Label(frame_1, text="Comentario")
ComentarioLabel.grid(row=5, column=0, padx=10, pady=10)

#---------------------------------------------Cuadros de texto
Id=StringVar()
IDEntry=Entry(frame_1, textvariable=Id, )
IDEntry.grid(row=0, column=1, padx=10, pady=10)

Nombre=StringVar()
NombreEntry=Entry(frame_1, textvariable=Nombre)
NombreEntry.grid(row=1, column=1, padx=10, pady=10)

Contraseña=StringVar()
ContraseñaEntry=Entry(frame_1, textvariable=Contraseña,show="*")
ContraseñaEntry.grid(row=2, column=1, padx=10, pady=10)

Apellido=StringVar()
ApellidoEntry=Entry(frame_1, textvariable=Apellido)
ApellidoEntry.grid(row=3, column=1, padx=10, pady=10)

Direccion=StringVar()
DireccionEntry=Entry(frame_1, textvariable=Direccion)
DireccionEntry.grid(row=4, column=1, padx=10, pady=10)


ComentarioText=Text(frame_1, width=20, height=5)
ComentarioText.grid(row=5, column=1, padx=10, pady=10)
scrollvert=Scrollbar(frame_1, command=ComentarioText.yview)
scrollvert.grid(row=5, column=2, sticky="nsew")
ComentarioText.config(yscrollcommand=scrollvert.set)



#-----------------------------------------------Botones

frame_2=Frame(root)
frame_2.pack()

ReadButton=Button(frame_2, text="Read", command=Read)
ReadButton.grid(row=0, column=0, padx=10, pady=10)

UpdateButton=Button(frame_2, text="Update", command=Update)
UpdateButton.grid(row=0, column=1, padx=10, pady=10)

DeleteButton=Button(frame_2, text="Delete", command=Delete)
DeleteButton.grid(row=0, column=2, padx=10, pady=10)

CreateButton=Button(frame_2, text="Create", command=Create)
CreateButton.grid(row=0, column=3, padx=10, pady=10)

#---------------------------------------------Menu

BarraMenu=Menu(root)
root.config(menu=BarraMenu)

BBDDMenu=Menu(BarraMenu, tearoff=0)
BBDDMenu.add_command(label="Conectar", command=Conexion)
BBDDMenu.add_separator()
BBDDMenu.add_command(label="Salir", command=Salir)

LimpiarMenu=Menu(BarraMenu, tearoff=0)
LimpiarMenu.add_cascade(label="Limpiar Campos", command=Limpiar)

CRUDMenu=Menu(BarraMenu, tearoff=0)
CRUDMenu.add_command(label="Read", command=Read)
CRUDMenu.add_command(label="Update", command=Update)
CRUDMenu.add_command(label="Delete", command=Delete)
CRUDMenu.add_command(label="Create", command=Create)

AyudaMenu=Menu(BarraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia", command=Licencia)
AyudaMenu.add_command(label="Ayuda", command=Ayuda)

BarraMenu.add_cascade(label="BBDD", menu=BBDDMenu)
BarraMenu.add_cascade(label="Limpiar", menu=LimpiarMenu)
BarraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
BarraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)



root.mainloop()