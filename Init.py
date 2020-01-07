# Código funcional, aunque aún queda pendiente corregir detalles en cuanto a cómo se guardan los datos requeridos
# por el programa.

# -*- coding: cp1252 -*-

# from Tkinter import Tk, Label, Button, Entry, Text, StringVar
from tkinter import Tk, Label, Button, Entry, Text, StringVar

colorFondo = "#00F"
colorLetra = "#000"

#############################################################

lecturaApellido1="xxxxxxxx"
lecturaApellido2="xxxxxxxx"
lecturaNombre1="xxxxxxxx"   
lecturaNombre2="xxxxxxxx"
lecturaNombre3="xxxxxxxx"
lecturaDni="xxxxxxxx"
lecturaNivel="xxxxxxxx"
lecturaInstitucion="xxxxxxxx"
lecturaContacto="xxxxxxxx"
lecturaCopiasAnteriores="xxxxxxxx"
lecturaAnadirCopias="xxxxxxxx"
    
#############################################################

def crearBecario():
    
    f = open("Base de datos/"+datoDni.get()+".txt","w")
             
    f.write(datoApellido1.get()+"\n")
    f.write(datoApellido2.get()+"\n")
    f.write(datoNombre1.get()+"\n")
    f.write(datoNombre2.get()+"\n")
    f.write(datoNombre3.get()+"\n")
    f.write(datoDni.get()+"\n")
    f.write(datoNivel.get()+"\n")
    f.write(datoInstitucion.get()+"\n")
    f.write(datoContacto.get()+"\n")
    f.write(datoCopiasAnteriores.get()+"\n")
    f.write(datoAnadirCopias.get()+"\n")

    f.close()

#############################################################

def verEstado():

    f = open("Base de datos/"+datoDni.get()+".txt","r")
 #   it=(linea for i,linea in enumerate(f) if i>=0)
 #   for linea in it:
  #      print linea

    it1=(lecturaApellido1 for i,lecturaApellido1 in enumerate(f) if i==0)
    for lecturaApellido1 in it1:
        print (lecturaApellido1)
    
    lecturaApellido2=(linea for i,linea in enumerate(f) if i==1)
    lecturaNombre1=(linea for i,linea in enumerate(f) if i==2)    
    lecturaNombre2=(linea for i,linea in enumerate(f) if i==3)
    lecturaNombre3=(linea for i,linea in enumerate(f) if i==4)
    lecturaDni=(linea for i,linea in enumerate(f) if i==5)
    lecturaNivel=(linea for i,linea in enumerate(f) if i==6)
    lecturaInstitucion=(linea for i,linea in enumerate(f) if i==7)
    lecturaContacto=(linea for i,linea in enumerate(f) if i==8)
    lecturaCopiasAnteriores=(linea for i,linea in enumerate(f) if i==9)
    lecturaAnadirCopias=(linea for i,linea in enumerate(f) if i==10)

    
    #lecturaApellido1=
    #lecturaApellido2=
    #lecturaNombre1=
    #lecturaNombre2=
    #lecturaNombre3=
    #lecturaDni=
    #lecturaNivel=
    #lecturaInstitucion=
    #lecturaContacto=
    #lecturaCopiasAnteriores=
    #lecturaAnadirCopias=
    
#############################################################
    

ventana = Tk()
		
ventana.title("Base de datos")
ventana.resizable(width=False,height=False)
ventana.geometry("600x450")
ventana.configure(background = colorFondo)

#######################################################

boton1 = Button(ventana, text="Agregar becario", width=15, height=1, command=crearBecario).place(x=450,y=40)
boton2 = Button(ventana, text="Ver estado", width=15, height=1, command=verEstado).place(x=450,y=80)
boton3 = Button(ventana, text="Modificar datos", width=15, height=1).place(x=450,y=120)
boton4 = Button(ventana, text="Borrar datos", width=15, height=1).place(x=450,y=160)
      

#######################################################

etiquetaTitulo = Label(ventana, text="Becarios fotocopias", font='bold', bg=colorFondo, fg=colorLetra).place(x=40,y=10)
etiquetaApellido1 = Label(ventana, text="Apellido 1", bg=colorFondo, fg=colorLetra).place(x=10,y=40)
etiquetaApellido2 = Label(ventana, text="Apellido 2", bg=colorFondo, fg=colorLetra).place(x=10,y=70)
etiquetaNombre1 = Label(ventana, text="Nombre 1", bg=colorFondo, fg=colorLetra).place(x=10,y=100)
etiquetaNombre2 = Label(ventana, text="Nombre 2", bg=colorFondo, fg=colorLetra).place(x=10,y=130)
etiquetaNombre3 = Label(ventana, text="Nombre 3", bg=colorFondo, fg=colorLetra).place(x=10,y=160)
etiquetaDni = Label(ventana, text="DNI", bg=colorFondo, fg=colorLetra).place(x=10,y=190)
etiquetaNivel = Label(ventana, text="Nivel", bg=colorFondo, fg=colorLetra).place(x=10,y=220)
etiquetaInstitucion = Label(ventana, text="Institucion", bg=colorFondo, fg=colorLetra).place(x=10,y=250)
etiquetaContacto = Label(ventana, text="Contacto", bg=colorFondo, fg=colorLetra).place(x=10,y=280)
etiquetaCopiasAnteriores = Label(ventana, text="Copias anteriores", bg=colorFondo, fg=colorLetra).place(x=10,y=310)
etiquetaAnadirCopias = Label(ventana, text="Añadir copias", bg=colorFondo, fg=colorLetra).place(x=10,y=340)

datoApellido1=StringVar()
datoApellido2=StringVar()
datoNombre1=StringVar()
datoNombre2=StringVar()
datoNombre3=StringVar()
datoDni=StringVar()
datoNivel=StringVar()
datoInstitucion=StringVar()
datoContacto=StringVar()
datoCopiasAnteriores=StringVar()
datoAnadirCopias=StringVar()


apellido1Caja = Entry(ventana, textvariable=datoApellido1).place(x=200,y=40)
apellido2Caja = Entry(ventana, textvariable=datoApellido2).place(x=200,y=70)
nombre1Caja = Entry(ventana, textvariable=datoNombre1).place(x=200,y=100)
nombre2Caja = Entry(ventana, textvariable=datoNombre2).place(x=200,y=130)
nombre3Caja = Entry(ventana, textvariable=datoNombre3).place(x=200,y=160)
dniCaja = Entry(ventana, textvariable=datoDni).place(x=200,y=190)
nivelCaja = Entry(ventana, textvariable=datoNivel).place(x=200,y=220)
institucionCaja = Entry(ventana, textvariable=datoInstitucion).place(x=200,y=250)
contactoCaja = Entry(ventana, textvariable=datoContacto).place(x=200,y=280)
copiasAnterioresCaja = Entry(ventana, textvariable=datoCopiasAnteriores).place(x=200,y=310)
anadirCopiasCaja = Entry(ventana, textvariable=datoAnadirCopias).place(x=200,y=340)


ventana.mainloop()

#############################################################
        	

