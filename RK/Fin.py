import main
import Servidor
# Definición de la clase
class Fin:
    # El método __init__ es el constructor de la clase
    def __init__(self, nombre,cantidad_servidores, rendimiento_medio):
        
        self.nombre = nombre
        self.v_prox_fin = []
        self.cantidad_servidores = cantidad_servidores
        self.rendimiento_medio = rendimiento_medio
        for i in range(cantidad_servidores):
            self.v_prox_fin.append(None)
        
        
    
    # Otros métodos de la clase
    
    
    def generar_prox_fin(self, horaActual, nroServidor):
        t_entre_fines = main.generarNumeroExponencial(self.rendimiento_medio)
        self.v_prox_fin[nroServidor] = main.truncate(horaActual + t_entre_fines, 2)
        
        
    def buscar_proximo_fin_servidor(self):
        tiempo_proximo = None
        indice = None
        for i in range(len(self.v_prox_fin)):
            if (self.v_prox_fin[i] == None): return (-1 , -1)
            if i == 0: 
                tiempo_proximo = self.v_prox_fin[i]
                indice = i
            else:
                if self.v_prox_fin[i] < tiempo_proximo : 
                    tiempo_proximo = self.v_prox_fin[i]
                    indice = i
        return (tiempo_proximo, indice)
    

