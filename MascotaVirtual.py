import random

from mascota import imagen

class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 0
        self.hambre = 0
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_feliz = imagen.feliz
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado


    def alimentar(self):
        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
            self.felicidad = 0
        
        if self.hambre == 0:
            print(self.imagen_disgustado)
            print(self.nombre," ya está llena, no puede comer más")
        else:
            self.hambre -= random.randint(10, 15)
            print(self.imagen_feliz)
            print(self.nombre, "le gustó mucho su comida y está lista para seguir")



    def jugar(self):
        
        if self.hambre > 70:
            print(self.imagen_disgustado)
            print(self.nombre, "Tiene mucho hambre para jugar ahora")
        else:
            self.felicidad += random.randint(10, 25)
        
            if self.felicidad > 100:
                self.felicidad = 100
        
            self.hambre += random.randint(10, 15)
            if self.hambre > 100:
                self.hambre = 100

            print(self.imagen_feliz)
            print(self.nombre, "se está divirtiendo")
        



    def estado_animo(self):
        # nivel de felicidad de la mascota.
        if self.felicidad >= 70:
            print(self.nombre, "esta contenta y lista para seguir")
        elif self.felicidad >= 30:
            print(self.nombre, "está aburrida")
        else:
            print(self.nombre, "está muy triste, deberían jugar un rato")

        #nivel de hambre de la mascota.
        if self.hambre <= 30:
            print(self.nombre, "Está satisfecha")
        elif self.hambre > 60:
            print(self.nombre, "está hambrienta, debería comer algo")
        else:
            print(self.nombre, "Tiene mucho hambre")


    def presentacion(self):
         print(
             f"\n╔════════════════════════════════════╗\n║     Te presento a tu mascota!      ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}"
         )

    def despedida(self):
         print(
             f"\n╔════════════════════════════════════╗\n║             Nos vemos!             ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║        Jueguemos otro día!         ║\n╚════════════════════════════════════╝\n"
         )

    
interfaz_inicio = "\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n"
interfaz_juego = "\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Estado de Ánimo                ║\n║ 4 - Salir                          ║\n╚════════════════════════════════════╝\n"

print(interfaz_inicio)

nombre = input("Elige un nombre para tu mascota: ")
mascota = MascotaVirtual(nombre)
mascota.presentacion()

while True:
    print(interfaz_juego)
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        mascota.alimentar()
    elif opcion == 2:
        mascota.jugar()
    elif opcion == 3:
        mascota.estado_animo()
    elif opcion == 4:
        mascota.despedida()
        break