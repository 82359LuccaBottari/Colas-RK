import random
import math
import main
# Definición de la clase
class Llegada:
    # El método __init__ es el constructor de la clase
    def __init__(self, media, nombre, prox_llegada):
        self.nombre = nombre
        self.prox_llegada = prox_llegada
        self.media = media
        
    
    # Otros métodos de la clase
    
    
    def generar_prox_Llegada(self, horaActual):
        t_entre_llegadas = main.generarNumeroExponencial(self.media)
        self.prox_llegada = main.truncate(horaActual + t_entre_llegadas, 2)
        


    
