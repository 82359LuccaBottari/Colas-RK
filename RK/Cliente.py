class Cliente:
    # El método __init__ es el constructor de la clase
    def __init__(self, estado, tiempo_inicio_espera):
        self.estado = estado
        self.tiempo_inicio_espera = tiempo_inicio_espera 
        self.tiempo_espera = None
        self.servidor_asignado = None
        self.tipo_servicio_demandado = -1
    
    def setEstadoSiendoAtendido(self, hora_actual):
        self.estado = 'siendoAtendido'
        self.tiempo_espera = hora_actual - self.tiempo_inicio_espera

    def setEstadoEnCola(self):
        self.estado = 'enCola'
    
    def asignar_servidor(self, servidor):
        self.servidor_asignado = servidor

    def get_tiempo_espera(self):
        return self.tiempo_espera

    

    


