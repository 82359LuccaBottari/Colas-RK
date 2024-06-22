from tkinter import *
from tkinter import ttk
from main import *

#
def Mensaje_Error(mensaje, titulo, resultado):
    raiz2 = Tk()
    raiz2.title(titulo)
    raiz2.geometry("400x50")

    raiz2.resizable(width=False, height=False)
    if resultado == True:
        back2 = "green3"
    else:
        back2 = "red2"
    raiz2.configure(background=back2)
    nombreMensaje=Label(raiz2, text=mensaje, font=("Arial bold", 13), background=back2)
    nombreMensaje.pack()

def llamar_TP():
    caja_cph = cuadrocaja_cph.get()
    at_personalizada_cph = cuadroat_personalizada_cph.get()
    tarj_credito_cph = cuadrotarj_credito_cph.get()
    plazo_fijo_cph = cuadroplazo_fijo_cph.get()
    prestamos_cph = cuadroprestamos_cph.get()
    cantidad_cajeros_cph = cuadrocantidad_cajeros_cph.get()
    linea_desde = cuadrolinea_desde.get()
    linea_hasta = cuadrolinea_hasta.get()
    tiempo_simulacion = cuadrotiempo_simulacion.get()
    tasa_servicio_caja = cuadro_tasa_servicio_caja.get()
    while True:
        if int(caja_cph) >= 0 \
                and int(at_personalizada_cph) > 0 \
                and int(tarj_credito_cph) > 0 \
                and int(plazo_fijo_cph) >= 0 \
                and int(prestamos_cph) >= 0 \
                and int(cantidad_cajeros_cph) > 0 \
                and int(linea_desde) >= 0 \
                and int(linea_hasta) >= 0 \
                and int(tasa_servicio_caja) >= 0\
                and int(tiempo_simulacion) >= 0:
            iniciar_simulacion(int(caja_cph), int(at_personalizada_cph), int(tarj_credito_cph),
                    int(plazo_fijo_cph), int(prestamos_cph), int(cantidad_cajeros_cph), int(tiempo_simulacion), int(linea_desde), int(linea_hasta), int(tasa_servicio_caja)) # Aca llama al iniciar_simulacion
            break
        else:
            Mensaje_Error("INGRESO INCORRECTO", "¡¡ERROR!!", False)
            return


raiz = Tk()
raiz.title("Grupo F - Ejercicio 4 - Lineas de Espera")
raiz.state('zoomed')  # Esta línea maximiza la ventana
ventana = Frame(raiz)
ventana.pack()
raiz.configure(background="#F7D358")
raiz.resizable(width=False, height=False)
back = "#FE9A2E"
ventana.configure(background=back)

nombrecaja_cph=Label(ventana, text="Tasa llegada clientes para Caja (Clientes x hora):", font=("Arial bold", 13), background=back, anchor='e')
nombrecaja_cph.grid(row=1, column=0, sticky="e")
cuadrocaja_cph=Entry(ventana, font=("Arial bold", 13))
cuadrocaja_cph.grid(row=1,column=1)

nombretarj_credito_cph=Label(ventana, text="Tasa llegada clientes para Tarjetas Credito (Clientes x hora):", font=("Arial bold", 13), background=back, anchor='e')
nombretarj_credito_cph.grid(row=2, column=0, sticky="e")
cuadrotarj_credito_cph=Entry(ventana, font=("Arial bold", 13))
cuadrotarj_credito_cph.grid(row=2,column=1)

nombreat_personalizada_cph=Label(ventana, text="Tasa llegada clientes para Atencion Personalizada (Clientes x hora):", font=("Arial bold", 13), background=back, anchor='e')
nombreat_personalizada_cph.grid(row=3, column=0, sticky="e")
cuadroat_personalizada_cph=Entry(ventana, font=("Arial bold", 13))
cuadroat_personalizada_cph.grid(row=3,column=1)

nombreplazo_fijo_cph=Label(ventana, text="Tasa llegada clientes para Plazo Fijo (Clientes x hora):", font=("Arial bold", 13), background=back, anchor='e')
nombreplazo_fijo_cph.grid(row=4, column=0, sticky="e")
cuadroplazo_fijo_cph=Entry(ventana, font=("Arial bold", 13))
cuadroplazo_fijo_cph.grid(row=4,column=1)

nombreprestamos_cph=Label(ventana, text="Tasa llegada clientes para Prestamos (Clientes x hora):", font=("Arial bold", 13), background=back, anchor='e')
nombreprestamos_cph.grid(row=5, column=0, sticky="e")
cuadroprestamos_cph=Entry(ventana, font=("Arial bold", 13))
cuadroprestamos_cph.grid(row=5,column=1)

nombrecantidad_cajeros_cph=Label(ventana, text="Cantidad de cajeros atendiendo:", font=("Arial bold", 13), background=back, anchor='e')
nombrecantidad_cajeros_cph.grid(row=6, column=0, sticky="e")
cuadrocantidad_cajeros_cph=Entry(ventana, font=("Arial bold", 13))
cuadrocantidad_cajeros_cph.grid(row=6,column=1)

nombretiempo_simulacion=Label(ventana, text="Duracion de la simulacion:", font=("Arial bold", 13), background=back, anchor='e')
nombretiempo_simulacion.grid(row=7, column=0, sticky="e")
cuadrotiempo_simulacion=Entry(ventana, font=("Arial bold", 13))
cuadrotiempo_simulacion.grid(row=7, column=1)

nombrelinea_desde=Label(ventana, text="Linea de inicio impresion:", font=("Arial bold", 13), background=back, anchor='e')
nombrelinea_desde.grid(row=8, column=0, sticky="e")
cuadrolinea_desde=Entry(ventana, font=("Arial bold", 13))
cuadrolinea_desde.grid(row=8,column=1)

nombrelinea_hasta=Label(ventana, text="Linea de fin de impresion:", font=("Arial bold", 13), background=back, anchor='e')
nombrelinea_hasta.grid(row=9, column=0, sticky="e")
cuadrolinea_hasta=Entry(ventana, font=("Arial bold", 13))
cuadrolinea_hasta.grid(row=9,column=1)

nombre_tasa_servicio_caja=Label(ventana, text="Tasa de servicio de las cajas:", font=("Arial bold", 13), background=back, anchor='e')
nombre_tasa_servicio_caja.grid(row=10, column=0, sticky="e")
cuadro_tasa_servicio_caja=Entry(ventana, font=("Arial bold", 13))
cuadro_tasa_servicio_caja.grid(row=10,column=1)

boton = Button(ventana, text="Aceptar", font=6, command=llamar_TP, width=8, background="#F5DA81")
boton.grid(row=11, column=1)


raiz.mainloop()