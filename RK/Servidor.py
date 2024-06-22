class Servidor:
    # El método __init__ es el constructor de la clase
    def __init__(self, nro ,estado):
        self.nro = nro
        self.estado = estado
        self.tiempo_ocio = 0
    

    def getEstado(self):
        return self.estado
    

    def setEstadoLibre(self):
        self.estado = 'libre'

    def estoyLibre(self):
        if self.estado == "libre": return True
        else: return False

    def setEstadoOcupado(self):
        self.estado = 'ocupado'
    
    def estoyOcupado(self):
        if self.estado == "ocupado": return True
        else: return False

    def acumular_ocio(self, tiempo_pasado):
        self.tiempo_ocio += tiempo_pasado

    def get_tiempo_ocio(self):
        return self.tiempo_ocio
    


        