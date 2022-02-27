from tkinter import *
from tkinter import messagebox as mss
#from PIL import ImageTk, Image

import os
import csv
import time
import random

from personajes import *
from constantes import *

#----

# Creamos la ventana de inicializacion
vn = Tk()
#vn.geometry("500x500") # Definir tamaño de la ventana
vn.geometry("300x300") # Definir tamaño de la ventana
vn.title(title) # Titulo de la ventana
vn.config(bg=color_bg) # https://htmlcolorcodes.com/es/

#-----------------------
#-----------------------
def iniciar():
    global E1, E2, vn_init
    
    # Cerramos la ventana
    vn.destroy()
    
    # Creamos una nueva ventana
    vn_init = Tk()
    vn_init.geometry("300x300") # Definir tamaño de la ventana
    vn_init.title("Proyecto videojuego") # Titulo de la ventana
    vn_init.config(bg=color_bg)
    
    # Labels
    L1 = Label(vn_init, text="PyMonster 2022", bg="#eeeff2")
    L2 = Label(vn_init, text="Usuario", bg="#eeeff2")
    L3 = Label(vn_init, text="Contraseña", bg="#eeeff2")
    
    # Coordenadas labels
    L1.place(x=90, y=20)
    L2.place(x=110, y=70)
    L3.place(x=100, y=160)
    
    # Entry
    E1 = Entry(vn_init)
    E2 = Entry(vn_init)
    
    # Coordenadas entry
    E1.place(x=50, y=100)
    E2.place(x=50, y=190)
    
    # Boton de inicio de sesion
    B2 = Button(vn_init, text="Iniciar", command=user_validation)
    B2.place(x=120, y=240)

    vn_init.mainloop()

def user_validation():
    global E1, E2
    usuario = path_users + E1.get() +".csv"
    password2 = E2.get()
    
    if os.path.exists(usuario):
        info = []
        with open(usuario) as archivo:
            rows = csv.reader(archivo, delimiter=",")
            for row in rows:
                info.append(row)
        password1 = info[-1][0]
        personaje = int(info[-1][1])
        nivel = int(info[-1][2])
        
        select_train["usuario"] = usuario
        select_train["password"] = password1
        select_train["nivel"] = nivel
        select_train["id_personaje"] = personaje
        
        if password2 == password1:
            # Pasamos a la ventana de seleccionar modo
            select_mode()
        else:
            E2.config(fg = 'red')
    else:
        answer = mss.askokcancel(title='Usuario no encontrado', message='No se encontró el usuario ¿Deseas registrar un usuario nuevo?', icon = mss.QUESTION)
            
        # Registramos al nuevo usuario
        if answer:
            user()
        else:
            E1.delete(0,END)
            E2.delete(0,END)
    
            
    
def user():
    global vn_init, E1, E2, E3, vn_user
    
    # Cerramos la ventana
    try:
        usuario = ""
        password1 = ""
        vn.destroy()
    except:
        usuario = E1.get()
        password1 = E2.get()
        vn_init.destroy()
    
    # Creamos una nueva ventana
    vn_user = Tk()
    vn_user.geometry("300x400") # Definir tamaño de la ventana
    vn_user.title("Proyecto videojuego") # Titulo de la ventana
    vn_user.config(bg=color_bg)
    
    # Labels
    L1 = Label(vn_user, text="PyMonster 2022", bg="#eeeff2")
    L2 = Label(vn_user, text="Usuario", bg="#eeeff2")
    L3 = Label(vn_user, text="Contraseña", bg="#eeeff2")
    L4 = Label(vn_user, text="Re - Contraseña", bg="#eeeff2")
    
    # Coordenadas labels
    L1.place(x=90, y=20)
    L2.place(x=110, y=70)
    L3.place(x=100, y=160)
    L4.place(x=90, y=250)
    
    # Entry
    E1 = Entry(vn_user)
    E2 = Entry(vn_user)
    E3 = Entry(vn_user)
    
    # Coordenadas entry
    E1.place(x=50, y=100)
    E2.place(x=50, y=190)
    E3.place(x=50, y=280)
    
    E1.insert(0,usuario)
    E2.insert(0,password1)
    
    # Boton de inicio de sesion
    B2 = Button(vn_user, text="Registrar", command=registrar)
    B2.place(x=120, y=330)

    vn_user.mainloop()
    
    print("usuario nuevo")

def registrar():
    global E1, E2, E3
    print("registrando")
    
    if E2.get() == E3.get():
        usuario = path_users + E1.get()+".csv"
        select_train["password"] = E2.get()
        select_train["usuario"] = usuario
        
        if os.path.exists(usuario):
            print("El usuario ya existe")
            E1.config(fg = 'red')
            E2.config(fg = 'black')
            E3.config(fg = 'black')
        else:
            write_csv(usuario, E2.get(), 0, 0)
            # Pasamos a la ventana de seleccionar modo
            select_mode()
    else:
        E1.config(fg = 'black')
        E2.config(fg = 'red')
        E3.config(fg = 'red')

def write_csv(usuario, password, id_personaje, nivel):
    with open(usuario,'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Contraseña","Personaje","Nivel"])
        writer.writerow([password,id_personaje,nivel])
    select_train["nivel"] = nivel
    select_train["id_personaje"] = id_personaje

def select_mode():
    global vn_init, vn_user, vn_mode, vn_c
    
    # Cerramos la ventana
    try:
        vn_init.destroy()
    except:
        try :
            vn_user.destroy()
        except:
            vn_c.destroy()
    
    # Creamos una nueva ventana
    vn_mode = Tk()
    vn_mode.geometry("300x300") # Definir tamaño de la ventana
    vn_mode.title("Select mode") # Titulo de la ventana
    vn_mode.config(bg=color_bg)
    
    # Boton de inicio de sesion
    B1 = Button(vn_mode, text="Modo entrenamiento", command=entrenamiento)
    B2 = Button(vn_mode, text="Modo historia", command=historia)
    B1.place(x=80, y=80)
    B2.place(x=100, y=170)
    
    B1.config(width="15", height="3")
    B2.config(width="10", height="3")

    vn_mode.mainloop()

def historia():
    print("Modo historia")
    select_train["historia"] = True
    
    if select_train["nivel"] > 0:
        # Preguntamos si ya podemos comenzar el combate
        answer = mss.askyesnocancel(title='Modo historia', message='¿Quieres continuar el combate desde el nivel ' + str(select_train["nivel"]) + '?', icon = mss.QUESTION)
        
        # Si no se desea continuar
        if answer == False:
            write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], 0)
            print("Se regresa hasta el menú de selección de modo historia o entrenamiento, del archivo de csv se eliminan los valores del nivel, más no los datos de registro, se puede volver a seleccionar personaje jugable.")
            select_train["historia"] = False
            
        elif answer == True:
            # Si continuamos
            # Seleccionamos los personajes
            list_personajes = list(dict_personajes.keys())
            print(select_train["id_personaje"])
            print(list_personajes[select_train["id_personaje"]])
            select_train["personaje"] = list_personajes[select_train["id_personaje"]]
            select_train["contra"] = list_personajes[select_train["nivel"]]
            # iniciamos el combate
            combate(select_train["personaje"],select_train["contra"])
            
        print(answer)
    else:
        print("Seleccionamos personaje para iniciar.")
        list_personajes = list(dict_personajes.keys())
        select_train["contra"] = list_personajes[select_train["nivel"]]
        entrenamiento()

def entrenamiento():
    global vn_mode, vn_p, B1, B2, B3, B4, B5, B6, B7
    print("Modo entrenamiento")
    try:
        vn_mode.destroy()
    except:
        vn_c.destroy()
    
    # Creamos una nueva ventana
    vn_p = Tk()
    vn_p.geometry("500x500") # Definir tamaño de la ventana
    vn_p.title("Seleccionar Personaje") # Titulo de la ventana
    vn_p.config(bg=color_bg)
    
    # Labels
    L1 = Label(vn_p, text="Aquarder", bg=color_bg)
    L2 = Label(vn_p, text="Electder", bg=color_bg)
    L3 = Label(vn_p, text="Firesor", bg=color_bg)
    L4 = Label(vn_p, text="Mousebug", bg=color_bg)
    L5 = Label(vn_p, text="Splant", bg=color_bg)
    L6 = Label(vn_p, text="Rockdog", bg=color_bg)
    
    # Coordenadas labels
    L1.place(x=50, y=10)
    L2.place(x=220, y=10)
    L3.place(x=380, y=10)
    L4.place(x=50, y=230)
    L5.place(x=230, y=230)
    L6.place(x=380, y=230)
    
    #Generar la imagen para Tk de cada personaje
    im1 = ImageTk.PhotoImage(Im_1)
    im2 = ImageTk.PhotoImage(Im_2)
    im3 = ImageTk.PhotoImage(Im_3)
    im4 = ImageTk.PhotoImage(Im_4)
    im5 = ImageTk.PhotoImage(Im_5)
    im6 = ImageTk.PhotoImage(Im_6)
    
    # Boton de personaje
    B1 = Button(vn_p, image=im1, command=personaje1)
    B1.place(x=10, y=40)
    B2 = Button(vn_p, image=im2, command=personaje2)
    B2.place(x=170, y=40)
    B3 = Button(vn_p, image=im3, command=personaje3)
    B3.place(x=330, y=40)
    B4 = Button(vn_p, image=im4, command=personaje4)
    B4.place(x=10, y=260)
    B5 = Button(vn_p, image=im5, command=personaje5)
    B5.place(x=170, y=260)
    B6 = Button(vn_p, image=im6, command=personaje6)
    B6.place(x=330, y=260)
    
    # Boton de detalles
    B12 = Button(vn_p, text="Detalle", command=lambda:detalles("Aquarder"))
    B12.place(x=60, y=195)
    B22 = Button(vn_p, text="Detalle", command=lambda:detalles("Electder"))
    B22.place(x=230, y=195)
    B32 = Button(vn_p, text="Detalle", command=lambda:detalles("Firesor"))
    B32.place(x=390, y=195)
    B42 = Button(vn_p, text="Detalle", command=lambda:detalles("Mousebug"))
    B42.place(x=60, y=415)
    B52 = Button(vn_p, text="Detalle", command=lambda:detalles("Splant"))
    B52.place(x=230, y=415)
    B62 = Button(vn_p, text="Detalle", command=lambda:detalles("Rockdog"))
    B62.place(x=390, y=415)
    
    B7 = Button(vn_p, text="INICIAR", command=pre_combate, state='disabled')
    B7.place(x=210, y=450)
    B7.config(width="10", height="2")
    
    vn_p.mainloop()

def detalles(gamer):
    print("Visualizamos los detalles: ")
    
    # Creamos una nueva ventana
    vn_d = Tk()
    vn_d.geometry("400x360") # Definir tamaño de la ventana
    vn_d.title(gamer) # Titulo de la ventana
    vn_d.config(bg=color_bg)
    
    # Abrimos las imagenes
    Im_d = Image.open(dict_personajes[gamer]["path_image"])
    #Modificamos la imagen a un tamaño predeterminado
    newsize = (100,100)
    Im_d = Im_d.resize(newsize)
    #Generar la imagen para Tk de cada personaje
    im_d = ImageTk.PhotoImage(Im_d, master=vn_d )
    # Visualizamos personaje
    L0_d = Label(vn_d, image=im_d, bg=color_bg)
    L0_d.place(x=150, y=10)
    
                                                        
    # Mensaje para el ganador
    L1_d = Label(vn_d, text=gamer+": Tipo "+dict_personajes[gamer]["tipo"], bg=color_bg)
    L1_d.place(x=120, y=115)
    L2_d = Label(vn_d, text="Ventaja con: " +
                    ", ".join(dict_personajes[gamer]["caracteristicas"]["ventaja"]), bg=color_bg)
    L2_d.place(x=100, y=150)
    L3_d = Label(vn_d, text="Desventaja con: " +
                    ", ".join(dict_personajes[gamer]["caracteristicas"]["desventaja"]), bg=color_bg)
    L3_d.place(x=80, y=170)
    L4_d = Label(vn_d, text="Normal con: " +
                    ", ".join(dict_personajes[gamer]["caracteristicas"]["normal"]), bg=color_bg)
    L4_d.place(x=90, y=190)

    L4_d = Label(vn_d, text="Habilidad\t|norm|At vent|At desv| pot norm| pot vent| pot desv|", bg=color_bg)
    L4_d.place(x=2, y=230)
    hab = list(dict_personajes[gamer]["habilidades"].keys())
    L5_d = Label(vn_d, text=hab[0]+"\t|  "+
            str(dict_personajes[gamer]["habilidades"][hab[0]]["normal"])+" pt|     "+
            str(dict_personajes[gamer]["habilidades"][hab[0]]["ventaja"])+" pt|      "+
            str(dict_personajes[gamer]["habilidades"][hab[0]]["desventaja"])+" pt|         "+
            str(dict_personajes[gamer]["habilidades"][hab[0]]["pot_normal"])+" pt|         "+
            str(dict_personajes[gamer]["habilidades"][hab[0]]["pot_ventaja"])+" pt|         "+
            str(dict_personajes[gamer]["habilidades"][hab[0]]["pot_desventaja"])+" pt|"
                            , bg=color_bg)
    L5_d.place(x=2, y=250)
    L5_d = Label(vn_d, text=hab[1]+"\t|  "+
            str(dict_personajes[gamer]["habilidades"][hab[1]]["normal"])+" pt|"
                            , bg=color_bg)
    L5_d.place(x=2, y=270)
    L5_d = Label(vn_d, text=hab[2]+"\t|  "+
            str(dict_personajes[gamer]["habilidades"][hab[2]]["normal"])+" pt|"
                            , bg=color_bg)
    L5_d.place(x=2, y=290)
    L5_d = Label(vn_d, text=hab[3]+"  | Potenciador de campo, 1 vez cada 3 turnos."
                            , bg=color_bg)
    L5_d.place(x=2, y=310)
    L6_d = Label(vn_d, text="\t| tiene una duración de 2 turnos.", bg=color_bg)
    L6_d.place(x=2, y=330)
    
    vn_d.mainloop()
    
def personaje1():
    global B1, B2, B3, B4, B5, B6, B7
    B = B1
    personaje = "Aquarder"
    print("seleccionado ", personaje)
    
    if "personaje" in select_train:
        select_train["contra"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="blue", state='active')
        B1.config(state='disabled')
        B2.config(state='disabled')
        B3.config(state='disabled')
        B4.config(state='disabled')
        B5.config(state='disabled')
        B6.config(state='disabled')
        B7.config(state='normal')
    else:
        select_train["personaje"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="red", state='active')
        
        if select_train["historia"]:
            list_personajes = list(dict_personajes.keys())
            select_train["id_personaje"] = list_personajes.index(select_train["personaje"])
            
            print("Guardando información del nivel: ", select_train["nivel"])
            write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], select_train["nivel"])
            # iniciamos el combate
            combate(select_train["personaje"],select_train["contra"])
        else:
            # Mostramos mensaje
            mss.showinfo(message="Selecciona tu contrincante", title="Contrincante")

def personaje2():
    global B1, B2, B3, B4, B5, B6, B7
    B = B2
    personaje = "Electder"
    print("seleccionado ", personaje)
    
    if "personaje" in select_train:
        select_train["contra"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="blue", state='active')
        B1.config(state='disabled')
        B2.config(state='disabled')
        B3.config(state='disabled')
        B4.config(state='disabled')
        B5.config(state='disabled')
        B6.config(state='disabled')
        B7.config(state='normal')
    else:
        select_train["personaje"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="red", state='active')
        
        if select_train["historia"]:
            list_personajes = list(dict_personajes.keys())
            select_train["id_personaje"] = list_personajes.index(select_train["personaje"])
            
            print("Guardando información del nivel: ", select_train["nivel"])
            write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], select_train["nivel"])
            # iniciamos el combate
            combate(select_train["personaje"],select_train["contra"])
        else:
            # Mostramos mensaje
            mss.showinfo(message="Selecciona tu contrincante", title="Contrincante")
            
def personaje3():
    global B1, B2, B3, B4, B5, B6, B7
    B = B3
    personaje = "Firesor"
    print("seleccionado ", personaje)
    
    if "personaje" in select_train:
        select_train["contra"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="blue", state='active')
        B1.config(state='disabled')
        B2.config(state='disabled')
        B3.config(state='disabled')
        B4.config(state='disabled')
        B5.config(state='disabled')
        B6.config(state='disabled')
        B7.config(state='normal')
    else:
        select_train["personaje"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="red", state='active')
        
        if select_train["historia"]:
            list_personajes = list(dict_personajes.keys())
            select_train["id_personaje"] = list_personajes.index(select_train["personaje"])
            
            print("Guardando información del nivel: ", select_train["nivel"])
            write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], select_train["nivel"])
            # iniciamos el combate
            combate(select_train["personaje"],select_train["contra"])
        else:
            # Mostramos mensaje
            mss.showinfo(message="Selecciona tu contrincante", title="Contrincante")
            
def personaje4():
    global B1, B2, B3, B4, B5, B6, B7
    B = B4
    personaje = "Mousebug"
    print("seleccionado ", personaje)
    
    if "personaje" in select_train:
        select_train["contra"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="blue", state='active')
        B1.config(state='disabled')
        B2.config(state='disabled')
        B3.config(state='disabled')
        B4.config(state='disabled')
        B5.config(state='disabled')
        B6.config(state='disabled')
        B7.config(state='normal')
    else:
        select_train["personaje"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="red", state='active')
        
        if select_train["historia"]:
            list_personajes = list(dict_personajes.keys())
            select_train["id_personaje"] = list_personajes.index(select_train["personaje"])
            
            print("Guardando información del nivel: ", select_train["nivel"])
            write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], select_train["nivel"])
            # iniciamos el combate
            combate(select_train["personaje"],select_train["contra"])
        else:
            # Mostramos mensaje
            mss.showinfo(message="Selecciona tu contrincante", title="Contrincante")
            


def personaje5():
    global B1, B2, B3, B4, B5, B6, B7
    B = B5
    personaje = "Splant"
    print("seleccionado ", personaje)
    
    if "personaje" in select_train:
        select_train["contra"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="blue", state='active')
        B1.config(state='disabled')
        B2.config(state='disabled')
        B3.config(state='disabled')
        B4.config(state='disabled')
        B5.config(state='disabled')
        B6.config(state='disabled')
        B7.config(state='normal')
    else:
        select_train["personaje"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="red", state='active')
        
        if select_train["historia"]:
            list_personajes = list(dict_personajes.keys())
            select_train["id_personaje"] = list_personajes.index(select_train["personaje"])
            
            print("Guardando información del nivel: ", select_train["nivel"])
            write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], select_train["nivel"])
            # iniciamos el combate
            combate(select_train["personaje"],select_train["contra"])
        else:
            # Mostramos mensaje
            mss.showinfo(message="Selecciona tu contrincante", title="Contrincante")
            


def personaje6():
    global B1, B2, B3, B4, B5, B6, B7
    B = B6
    personaje = "Rockdog"
    print("seleccionado ", personaje)
    
    if "personaje" in select_train:
        select_train["contra"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="blue", state='active')
        B1.config(state='disabled')
        B2.config(state='disabled')
        B3.config(state='disabled')
        B4.config(state='disabled')
        B5.config(state='disabled')
        B6.config(state='disabled')
        B7.config(state='normal')
    else:
        select_train["personaje"] = personaje
        # Cambiamos el color si ya esta seleccionado
        B.config(bg="red", state='active')
        
        if select_train["historia"]:
            list_personajes = list(dict_personajes.keys())
            select_train["id_personaje"] = list_personajes.index(select_train["personaje"])
            
            print("Guardando información del nivel: ", select_train["nivel"])
            write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], select_train["nivel"])
            # iniciamos el combate
            combate(select_train["personaje"],select_train["contra"])
        else:
            # Mostramos mensaje
            mss.showinfo(message="Selecciona tu contrincante", title="Contrincante")
            

        
def pre_combate():
    global vn_p, B1, B2, B3, B4, B5, B6, B7
    
    # Preguntamos si ya podemos comenzar el combate
    answer = mss.askokcancel(title='Comenzamos', message='¿Listo?', icon = mss.QUESTION)
    if answer:
        # Cambiamos a la ventana de juego
        print("iniciamos juego: ")
        print(select_train["personaje"], " vs ", select_train["contra"])
        combate(select_train["personaje"],select_train["contra"])
    else:
        # Limpiamos el tablero de seleccion
        print("no comenzamos")
        del select_train["personaje"], select_train["contra"]
        # Volvemos a activar los botones para seleccionar nuevos personajes
        B1.config(bg=color_bg, state='normal')
        B2.config(bg=color_bg, state='normal')
        B3.config(bg=color_bg, state='normal')
        B4.config(bg=color_bg, state='normal')
        B5.config(bg=color_bg, state='normal')
        B6.config(bg=color_bg, state='normal')
        B7.config(bg=color_bg, state='disabled')
        
def combate(gamer1, gamer2):
    global vn_mode, vn_p, vn_c, L1, L2, B5, gamer2_hab, gamer2_ventaja
    try:
        vn_p.destroy()
    except:
        try:
            vn_mode.destroy()
        except:
            vn_c.destroy()
    
    print("Combate: "+gamer1+" vs "+gamer2)

    # Creamos una nueva ventana
    vn_c = Tk()
    vn_c.geometry("500x400") # Definir tamaño de la ventana
    vn_c.title("Combate") # Titulo de la ventana
    vn_c.config(bg=color_bg)
    
    #Generar la imagen para Tk de cada personaje
    im1 = ImageTk.PhotoImage(dict_personajes[gamer1]["imagen"])
    im2 = ImageTk.PhotoImage(dict_personajes[gamer2]["imagen"])
    
    # Obtnemos la información de los personajes seleccionados
    gamer1_hab, gamer1_ventaja = comparar(gamer1, gamer2)
    gamer2_hab, gamer2_ventaja = comparar(gamer2, gamer1)
        
    # Botones de ataque
    B1 = Button(vn_c, text=gamer1_hab[0],
            command=lambda:ataque("1","2", gamer1, gamer1_hab[0], gamer1_ventaja, gamer2))
    B2 = Button(vn_c, text=gamer1_hab[1],
            command=lambda:ataque("1","2", gamer1, gamer1_hab[1], gamer1_ventaja, gamer2))
    B3 = Button(vn_c, text=gamer1_hab[2],
            command=lambda:ataque("1","2", gamer1, gamer1_hab[2], gamer1_ventaja, gamer2))
    B4 = Button(vn_c, text=gamer1_hab[3],
            command=lambda:ataque("1","2", gamer1, gamer1_hab[3], gamer1_ventaja, gamer2))
    B1.place(x=10, y=40)
    B2.place(x=10, y=80)
    B3.place(x=10, y=120)
    B4.place(x=10, y=160)
    B1.config(width="15", height="2")
    B2.config(width="15", height="2")
    B3.config(width="15", height="2")
    B4.config(width="15", height="2")
    
    # Visualizamos personaje
    L3 = Label(vn_c, image=im1, bg=color_bg)
    L3.place(x=150, y=40)
    L4 = Label(vn_c, image=im2, bg=color_bg)
    L4.place(x=330, y=40)

    # Nombre de los personaje
    L5 = Label(vn_c, text=gamer1, bg=color_bg)
    L5.place(x=190, y=230)
    L6 = Label(vn_c, text=gamer2, bg=color_bg)
    L6.place(x=360, y=230)
    
    # Puntos de vida
    L1 = Label(vn_c, text=str(select_train["HP1"])+" Hp", bg=color_bg)
    L1.place(x=190, y=260)
    L2 = Label(vn_c, text=str(select_train["HP2"])+" Hp", bg=color_bg)
    L2.place(x=360, y=260)
    
    # Decidimos quien inicia el juego
    turno = random.randint(1,2)
    print("El turnos es de: ", turno)
    if turno==2:
        # Cuadro de dialogo para los resultados
        B5 = Button(vn_c, text="Primer movimiento del CPU\n¡¡Cuidado!!", state='disabled', width="52", height="5")
        B5.place(x=10, y=300)
        vn_c.update()
        time.sleep(2)
        id_atck = random.randint(0,3)
        ataque("2","1", gamer2, gamer2_hab[id_atck], gamer2_ventaja, gamer1)
    else:
        # Cuadro de dialogo para los resultados
        B5 = Button(vn_c, text="Primer movimiento es tuyo\n¡¡Piensa bien!!", state='disabled', width="52", height="5")
        B5.place(x=10, y=300)
    
    vn_c.mainloop()
    
def comparar(gamer1, gamer2):
    # Obtnemos la información de los personajes seleccionados
    gamer1_hab = list(dict_personajes[gamer1]["habilidades"].keys())
    gamer1_tipo = dict_personajes[gamer1]["tipo"]
    gamer2_tipo = dict_personajes[gamer2]["tipo"]
    
    if gamer2_tipo in dict_personajes[gamer1]["caracteristicas"]["normal"]:
        gamer1_ventaja = "normal"
    elif gamer2_tipo in dict_personajes[gamer1]["caracteristicas"]["ventaja"]:
        gamer1_ventaja = "ventaja"
    elif gamer2_tipo in dict_personajes[gamer1]["caracteristicas"]["desventaja"]:
        gamer1_ventaja = "desventaja"
    
    print("Comparacion: ", gamer1_tipo, gamer1_ventaja, gamer2_tipo)
    return(gamer1_hab, gamer1_ventaja)

def ventana_ganador(gamer):
    vn_c.destroy()
        
    # Creamos una nueva ventana
    vn_win = Tk()
    vn_win.geometry("200x200") # Definir tamaño de la ventana
    vn_win.title("Game Over") # Titulo de la ventana
    vn_win.config(bg=color_bg)

    # Abrimos las imagenes
    Im_win = Image.open(path_utils+"gameover.png")
    #Modificamos la imagen a un tamaño predeterminado
    newsize = (150,150)
    Im_Win = Im_win.resize(newsize)
    #Generar la imagen para Tk de cada personaje
    im_win = ImageTk.PhotoImage(Im_Win)
    # Visualizamos personaje
    L2_win = Label(vn_win, image=im_win, bg=color_bg)
    L2_win.place(x=25, y=10)

    # Mensaje para el ganador
    L1_win = Label(vn_win, text="¡¡Felicidades Ganaste!!", bg=color_bg)
    L1_win.place(x=27, y=170)
    vn_win.mainloop()

def ataque(id1, id2, gamer, atck, ventaja, oponente):
    global vn_c, L1, L2, B5, gamer2_hab, gamer2_ventaja
    
    # Verificamos si el ataque tiene algun punto extra
    if ventaja in dict_personajes[gamer]["habilidades"][atck]:
        # Verificamos si se ha utilizado un potenciador
        if select_train["band_pot"+id1] and ('pot_'+ventaja in dict_personajes[gamer]["habilidades"][atck]):
            points = dict_personajes[gamer]["habilidades"][atck]['pot_'+ventaja]
        else:
            # En el caso sin potenciador activado
            points = dict_personajes[gamer]["habilidades"][atck][ventaja]
    # Si el ataque no tiene puntuacion de ventaja o desventaja
    else:
        points = dict_personajes[gamer]["habilidades"][atck]["normal"]
    
    select_train["HP"+id2] -= points
    if select_train["HP"+id2] <= 0:
        B5.config(text = "¡¡" + gamer + " es el ganador!!")
        # Actualizamos la ventana
        print("puntos de ganador: ", max(select_train["HP1"],0))
        print("puntos de ganador: ", max(select_train["HP2"],0))
        L1.config(text=str(max(select_train["HP1"],0))+" Hp")
        L2.config(text=str(max(select_train["HP2"],0))+" Hp")
        vn_c.update()
        
        time.sleep(2)
        band_ganador = 1 if select_train["HP1"]>select_train["HP2"] else 0
        
        # Limpiamos las variables para volver a selecionar los personajes
        select_train["HP1"] = 25
        select_train["HP2"] = 25
        select_train["turno1"] = 0
        select_train["turno_min1"] = 0
        select_train["turno_max1"] = 0
        select_train["band_pot1"] = False
        select_train["turno2"] = 0
        select_train["turno_min2"] = 0
        select_train["turno_max2"] = 0
        select_train["band_pot2"] = False
        del select_train["contra"], select_train["personaje"]
        
        if select_train["historia"]:
            # Si tenemos todavia combatientes disponibles
            if select_train["nivel"] < 5:
                # Si ganamos continuamos a la siguiente pelea
                if band_ganador:
                    select_train["nivel"] += 1 # Actualizamos el nivel
                    print("Guardando información del nivel: ", select_train["nivel"])
                    write_csv(select_train["usuario"], select_train["password"], select_train["id_personaje"], select_train["nivel"])
                    
                    # Seleccionamos los personajes
                    list_personajes = list(dict_personajes.keys())
                    select_train["personaje"] = list_personajes[select_train["id_personaje"]]
                    select_train["contra"] = list_personajes[select_train["nivel"]]
                    # iniciamos el combate
                    combate(select_train["personaje"],select_train["contra"])
                # Si perdemos regresamos al menu de seleccion historia y entrenamiento
                else:
                    print("perdiste te regresamos al menu")
                    select_train["historia"] = False
                    select_mode()
            # Si ya fue  el ultimo combatiente
            else:
                print("Juego finalizado....")
                if band_ganador:
                    print("Ganaste tu!!!")
                    # Eliminar el archivo
                    os.remove(select_train["usuario"])
                    ventana_ganador(gamer)
                else:
                    print("Gano el oponente... \Regresando al menu.")
                    select_train["historia"] = False
                    # Regresamos al menu de seleccion
                    select_mode()
        else:
            entrenamiento()
        return
        
    # Verificamos si el potenciador fue utilizado
    comment = ""
    if (dict_personajes[gamer]["habilidades"][atck]["tiempo"]>0)and(select_train["turno"+id1]==0):
        select_train["turno"+id1] += 1
        select_train["turno_min"+id1] = dict_personajes[gamer]["habilidades"][atck]["pausa"]
        select_train["turno_max"+id1] = dict_personajes[gamer]["habilidades"][atck]["tiempo"]
        select_train["band_pot"+id1] = True
        comment += "\nQuedan " + str(select_train["turno_max"+id1]) + " movimientos"
    else:
        # Verificamos si el potenciador sigue activo
        if select_train["band_pot"+id1] or (select_train["turno"+id1] != 0):
            if dict_personajes[gamer]["habilidades"][atck]["tiempo"]>0:
                comment += "\n¡¡"+atck+" no disponible por el momento!!"
            else:
                if select_train["band_pot"+id1]:
                    if "pot_ventaja" in dict_personajes[gamer]["habilidades"][atck]:
                        comment += " potenciado"
                    else:
                        comment += "\nEl potenciador no tiene efecto"
                
            if select_train["turno"+id1]==select_train["turno_max"+id1]:
                comment += "\nFin del potenciador"
                select_train["band_pot"+id1] = False
                # Aumentamos el contador del turno
                select_train["turno"+id1] += 1
            elif select_train["turno"+id1]==select_train["turno_min"+id1]:
                comment += "\nEl potenciador acaba de cambiar a disponible"
                select_train["turno"+id1] = 0
            else:
                # Aumentamos el contador del turno
                comment += "\nQuedan " + str(select_train["turno_max"+id1]-select_train["turno"+id1]) + " movimientos"
                select_train["turno"+id1] += 1
                
    # Texto para indicar el siguiente turno
    turno = "\n¡¡Tu turno!!" if id1 == "2" else ""
    
    # Actualizamos la ventana
    L1.config(text=str(select_train["HP1"])+" Hp")
    L2.config(text=str(select_train["HP2"])+" Hp")
    B5.config(text=gamer+" a utilizado "+atck+comment+turno)
    vn_c.update()
    
    # Ejecutamos el movimiento del oponente
    if id1 == "1":
        time.sleep(1)
        ataque("2","1", oponente, gamer2_hab[random.randint(0,3)], gamer2_ventaja, gamer)
        
#-----------------------

# Titulo del videojuego
L1 = Label(vn, text="PyMonster 2022", bg="#eeeff2")
L1.place(x=90, y=20)
#title.place(x=200, y=20)

# Boton de inicio de sesion
B1 = Button(vn, text="Iniciar sesión", command=iniciar)
B1.place(x=101, y=90)
B1.config(width="10", height="3")

# Boton de inicio de sesion
B2 = Button(vn, text="Usuario nuevo", command=user)
B2.place(x=80, y=180)
B2.config(width="15", height="3")

vn.mainloop()
