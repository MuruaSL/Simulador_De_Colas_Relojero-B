import random
import math

tiempo_simulacion = 1000
iteraciones_simulacion = 100

llegada_clientes_min = 13
llegada_clientes_max = 17
cliente_probabilidad_compra = 0.45
cliente_probabilidad_entrega = 0.25
cliente_probabilidad_retiro = 0.30

tiempo_atencion_compra_min = 4
tiempo_atencion_compra_max = 10
tiempo_atencion_entrega = 3
tiempo_atencion_retiro = 3

tiempo_reparacion_relojero_min = 18
tiempo_reparacion_relojero_max = 22
probabilidad_tomar_cafe = 0.1
tiempo_tomar_cafe = 5


class Simulacion(object):

    def __init__(self):
        self.tiempo_simulacion = tiempo_simulacion
        self.iteraciones_simulacion = iteraciones_simulacion
        self.llegada_clientes_min = llegada_clientes_min
        self.llegada_clientes_max = llegada_clientes_max
        self.cliente_probabilidad_compra = cliente_probabilidad_compra
        self.cliente_probabilidad_entrega = cliente_probabilidad_entrega
        self.cliente_probabilidad_retiro = cliente_probabilidad_retiro
        self.tiempo_atencion_compra_min = tiempo_atencion_compra_min
        self.tiempo_atencion_compra_max = tiempo_atencion_compra_max
        self.tiempo_atencion_entrega = tiempo_atencion_entrega
        self.tiempo_atencion_retiro = tiempo_atencion_retiro
        self.tiempo_reparacion_relojero_min = tiempo_reparacion_relojero_min
        self.tiempo_reparacion_relojero_max = tiempo_reparacion_relojero_max
        self.probabilidad_tomar_cafe = probabilidad_tomar_cafe
        self.tiempo_tomar_cafe = tiempo_tomar_cafe

    @property.setter
    def setTiempoSimulacion(self, tiempo):
        if tiempo > 0:
            self.tiempo_simulacion = tiempo
    @property.setter
    def setIteracionesSimulacion(self, iteraciones):
        if iteraciones > 0:
            self.iteraciones_simulacion = iteraciones

    @property.setter
    def setLlegadaClientesMin(self, tiempo):
        if tiempo > 0:
            self.llegada_clientes_min = tiempo
    @property.setter
    def setLlegadaClientesMax(self, tiempo):
        if tiempo > 0:
            self.llegada_clientes_max = tiempo
    @property.setter
    def setClienteProbabilidadCompra(self, probabilidad):
        if probabilidad >= 0 and probabilidad <= 1:
            self.cliente_probabilidad_compra = probabilidad
    @property.setter
    def setClienteProbabilidadEntrega(self, probabilidad):
        if probabilidad >= 0 and probabilidad <= 1:
            self.cliente_probabilidad_entrega = probabilidad
    @property.setter
    def setClienteProbabilidadRetiro(self, probabilidad):
        if probabilidad >= 0 and probabilidad <= 1:
            self.cliente_probabilidad_retiro = probabilidad
    @property.setter
    def setTiempoAtencionCompraMin(self, tiempo):
        if tiempo > 0:
            self.tiempo_atencion_compra_min = tiempo
    @property.setter
    def setTiempoAtencionCompraMax(self, tiempo):
        if tiempo > 0:
            self.tiempo_atencion_compra_max = tiempo
    @property.setter
    def setTiempoAtencionEntrega(self, tiempo):
        if tiempo > 0:
            self.tiempo_atencion_entrega = tiempo
    @property.setter
    def setTiempoAtencionRetiro(self, tiempo):
        if tiempo > 0:
            self.tiempo_atencion_retiro = tiempo
    @property.setter
    def setTiempoReparacionRelojeroMin(self, tiempo):
        if tiempo > 0:
            self.tiempo_reparacion_relojero_min = tiempo
    @property.setter
    def setTiempoReparacionRelojeroMax(self, tiempo):
        if tiempo > 0:
            self.tiempo_reparacion_relojero_max = tiempo
    @property.setter
    def setProbabilidadTomarCafe(self, probabilidad):
        if probabilidad >= 0 and probabilidad <= 1:
            self.probabilidad_tomar_cafe = probabilidad
    @property.setter
    def setTiempoTomarCafe(self, tiempo):
        if tiempo > 0:
            self.tiempo_tomar_cafe = tiempo

    def definirCondicionInicial():
        #TODO
        pass

    def iniciar_simulacion(self):
        for i in range(self.iteraciones_simulacion):
            tiempo_actual = 0
            definirCondicionInicial()
            while tiempo_actual < self.tiempo_simulacion:
                
                pass
