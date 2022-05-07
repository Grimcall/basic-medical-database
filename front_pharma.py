from tkinter import *
import datetime
#from back_pharma import Database

#database = Database("Clientes.db")

"""
ATRIBUTOS DE DB:

-ci = CEDULA
-nombre = NOMBRE
-apellido
-numero = numero telefonico
-direccion
-correo
-tipo de sangre
-comentarios
-fecha 

METODOS:

*Ver todos
*Agregar
*Borrar
*Modificar
*Cerrar
*Exportar a csv.

"""

class Window(object):
    
    def __init__(self, window):
        self.window = window

        self.window.wm_title("Pharmacy")

        #Cedula
        l1 = Label(window, text = "Cedula")
        l1.grid(row = 0, column = 0)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable = self.title_text)
        self.e1.grid(row = 0, column = 1)

        #Nombre
        l2 = Label(window, text = "Nombre")
        l2.grid(row  = 0, column = 2)

        self.title_text = StringVar()
        self.e2 = Entry(window, textvariable = self.title_text)
        self.e2.grid(row = 0, column = 3)        

        #Apellido
        l3 = Label(window, text = "Apellido")
        l3.grid(row  = 0, column = 4)

        self.title_text = StringVar()
        self.e3 = Entry(window, textvariable = self.title_text)
        self.e3.grid(row = 0, column = 5)

        #Numero Telefonico
        l4 = Label(window, text = "Numero Telefonico")
        l4.grid(row  = 1, column = 0)

        self.title_text = StringVar()
        self.e4 = Entry(window, textvariable = self.title_text)
        self.e4.grid(row = 1, column = 1)

        #Direccion
        l5 = Label(window, text = "Direccion")
        l5.grid(row = 1, column = 2)

        self.title_text = StringVar()
        self.e5 = Entry(window, textvariable = self.title_text)
        self.e5.grid(row = 1, column = 3)

        #Correo        
        l6 = Label(window, text = "Correo")
        l6.grid(row = 1, column = 4)

        self.title_text = StringVar()
        self.e6 = Entry(window, textvariable = self.title_text)
        self.e6.grid(row = 1, column = 5)

        #Tipo de Sangre
        l8 = Label(window, text = "Tipo de Sangre")
        l8.grid(row = 2, column = 0)

        self.title_text = StringVar()
        self.e8 = Entry(window, textvariable = self.title_text)
        self.e8.grid(row = 2, column = 1)

        #Comentarios
        l7 = Label(window, text = "Comentarios")
        l7.grid(row = 2, column = 2)

        self.title_text = StringVar()
        self.e7 = Entry(window, textvariable = self.title_text)
        self.e7.grid(row = 2, column = 3)     

        #Fecha
        l9 = Label(window, text = "Fecha")
        l9.grid(row = 2, column = 4)

        self.title_text = StringVar()
        self.e9 = Entry(window, textvariable = self.title_text)
        self.e9.grid(row = 2, column = 5)

        self.list1 = Listbox(window, height = 6, width = 70)
        self.list1.grid(row = 3, column = 0, rowspan = 6, columnspan = 5)

        sb1 = Scrollbar(window)
        sb1.grid(row = 3, column = 2, rowspan = 6)

        self.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command = self.list1.yview)

  #      self.list1.bind('<<ListBoxSelect>>', self.get_selected_row)

        b1 = Button(window, text = "Ver todos", width = 12)
        b1.grid(row = 3, column = 5)




window = Tk()
Window (window)
window.mainloop()

