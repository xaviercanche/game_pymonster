from tkinter import *
from PIL import ImageTk, Image

path_personajes = "personajes/"

#----
# Abrimos las imagenes
Im1 = Image.open(path_personajes+"aquarder.png")
Im2 = Image.open(path_personajes+"electder.png")
Im3 = Image.open(path_personajes+"Firesor.png")
Im4 = Image.open(path_personajes+"mousebug.png")
Im5 = Image.open(path_personajes+"splant.png")
Im6 = Image.open(path_personajes+"rockdog.png")

    
#Modificamos la imagen a un tamaño predeterminado
newsize = (150,150)
Im_1 = Im1.resize(newsize)
Im_2 = Im2.resize(newsize)
Im_3 = Im3.resize(newsize)
Im_4 = Im4.resize(newsize)
Im_5 = Im5.resize(newsize)
Im_6 = Im6.resize(newsize)

# Guardamos la informacion de cada personaje en un diccionario
dict_personajes = {
            "Aquarder": {
                            "tipo":"agua",
                            "imagen":Im_1,
                            "path_image":path_personajes+"aquarder.png",
                            "caracteristicas":{
                                                "normal":["agua","escarabajo"],
                                                "ventaja":["roca","fuego"],
                                                "desventaja":["electrico","planta"]
                                            },
                            "habilidades":{
                                            "Aqua-jet": {
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3,
                                                        "ventaja":5,
                                                        "desventaja":2,
                                                        "pot_normal":5,
                                                        "pot_ventaja":7,
                                                        "pot_desventaja":4
                                                        },
                                            "Cola férrea":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Cabezazo":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Lluvia":{
                                                        "tiempo":2,
                                                        "pausa":3,
                                                        "normal":0
                                                        }
                                        }
                        },
            "Electder":{
                            "tipo":"electrico",
                            "imagen":Im_2,
                            "path_image":path_personajes+"electder.png",
                            "caracteristicas":{
                                                "normal":["electrico","fuego"],
                                                "ventaja":["agua","escarabajo"],
                                                "desventaja":["roca","planta"]
                                            },
                            "habilidades":{
                                            "Trueno": {
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3,
                                                        "ventaja":5,
                                                        "desventaja":2,
                                                        "pot_normal":5,
                                                        "pot_ventaja":7,
                                                        "pot_desventaja":4
                                                        },
                                            "Arañazo":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3
                                                        },
                                            "Mordisco":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3
                                                        },
                                            "Campo magnético":{
                                                        "tiempo":2,
                                                        "pausa":3,
                                                        "normal":0
                                                        }
                                        }
                        },
            "Firesor":{
                            "tipo":"fuego",
                            "imagen":Im_3,
                            "path_image":path_personajes+"Firesor.png",
                            "caracteristicas":{
                                                "normal":["electrico","fuego"],
                                                "ventaja":["planta","escarabajo"],
                                                "desventaja":["agua","roca"]
                                            },
                            "habilidades":{
                                            "Llamarada": {
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3,
                                                        "ventaja":5,
                                                        "desventaja":2,
                                                        "pot_normal":5,
                                                        "pot_ventaja":7,
                                                        "pot_desventaja":4
                                                        },
                                            "Embestida":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Mordisco":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Día soleado":{
                                                        "tiempo":2,
                                                        "pausa":3,
                                                        "normal":0
                                                        }
                                        }
                        },
            "Mousebug":{
                            "tipo":"escarabajo",
                            "imagen":Im_4,
                            "path_image":path_personajes+"mousebug.png",
                            "caracteristicas":{
                                                "normal":["escarabajo","agua"],
                                                "ventaja":["planta","roca"],
                                                "desventaja":["fuego","electrico"]
                                            },
                            "habilidades":{
                                            "Picotazo": {
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3,
                                                        "ventaja":5,
                                                        "desventaja":2,
                                                        "pot_normal":5,
                                                        "pot_ventaja":7,
                                                        "pot_desventaja":4
                                                        },
                                            "Embestida":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Cabezazo":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Esporas":{
                                                        "tiempo":2,
                                                        "pausa":3,
                                                        "normal":0
                                                        }
                                        }
                        },
            "Splant":{
                            "tipo":"planta",
                            "imagen":Im_5,
                            "path_image":path_personajes+"rockdog.png",
                            "caracteristicas":{
                                                "normal":["planta"],
                                                "ventaja":["roca","agua","electrico"],
                                                "desventaja":["fuego","escarabajo"]
                                            },
                            "habilidades":{
                                            "Hola navaja": {
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3,
                                                        "ventaja":5,
                                                        "desventaja":2,
                                                        "pot_normal":5,
                                                        "pot_ventaja":7,
                                                        "pot_desventaja":4
                                                        },
                                            "Mordisco":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Cabezazo":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Rayo solar":{
                                                        "tiempo":2,
                                                        "pausa":3,
                                                        "normal":0
                                                        }
                                        }
                        },
            "Rockdog":{
                            "tipo":"roca",
                            "imagen":Im_6,
                            "path_image":path_personajes+"splant.png",
                            "caracteristicas":{
                                                "normal":["roca","escarabajo"],
                                                "ventaja":["fuego","electrico"],
                                                "desventaja":["agua","planta"]
                                            },
                            "habilidades":{
                                            "Roca afilado": {
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":3,
                                                        "ventaja":5,
                                                        "desventaja":2,
                                                        "pot_normal":5,
                                                        "pot_ventaja":7,
                                                        "pot_desventaja":4
                                                        },
                                            "Velocidad":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Cola ferrea":{
                                                        "tiempo":0,
                                                        "pausa":0,
                                                        "normal":2
                                                        },
                                            "Campo rocoso":{
                                                        "tiempo":2,
                                                        "pausa":3,
                                                        "normal":0
                                                        }
                                        }

                        },
            }

#----
