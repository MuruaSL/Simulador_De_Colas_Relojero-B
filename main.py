# =========================================================
# TP SIMULACION - RELOJERIA
# VERSION CON 2 FILAS (ACTUAL / ANTERIOR)
# =========================================================

import random
import math
import pandas as pd
import os

os.makedirs("resultados", exist_ok=True)

# =========================================================
# FUNCIONES RANDOM
# =========================================================

def uniforme(a, b):
    rnd = random.random()
    valor = a + rnd * (b - a)
    return rnd, round(valor, 2)


def generar_tipo_cliente():
    rnd = random.random()
    if rnd < 0.45:
        tipo = "Compra"
    elif rnd < 0.70:
        tipo = "Entrega"
    else:
        tipo = "Retiro"
    return rnd, tipo


def decidir_cafe():
    rnd = random.random()
    return rnd, rnd < 0.10


# =========================================================
# PARAMETROS
# =========================================================

max_iteraciones = int(input("Ingrese maximo iteraciones: "))
tiempo_simulacion = int(input("Ingrese tiempo simulacion: "))
mostrar_desde = int(input("Mostrar desde fila: "))
cantidad_mostrar = int(input("Cantidad filas a mostrar: "))


# =========================================================
# VARIABLES DE SIMULACION
# =========================================================

fila = 1
reloj = 0


# =========================================================
# EVENTOS FUTUROS
# =========================================================

prox_llegada = 0
prox_fin_atencion = math.inf
prox_fin_reparacion = math.inf
prox_fin_cafe = math.inf


# =========================================================
# ESTADOS
# =========================================================

estado_ayudante = "Libre"
estado_relojero = "Libre"


# =========================================================
# COLAS
# =========================================================

cola_ayudante = []
cola_reparacion = []


# =========================================================
# VARIABLES DEL SISTEMA
# =========================================================

relojes_reparados = 3
cliente_actual = None


# =========================================================
# ACUMULADORES
# =========================================================

ac_ocupacion_ayudante = 0
ac_ocupacion_relojero = 0
cont_retiros = 0
cont_retiros_fallidos = 0
cont_cafes = 0


# =========================================================
# VARIABLES RANDOM AUXILIARES
# =========================================================

rnd_llegada = "-"
rnd_tipo = "-"
rnd_atencion = "-"
rnd_reparacion = "-"
rnd_cafe = "-"
tiempo_entre_llegadas_mostrar = "-"
tipo_cliente_mostrar = "-"
tiempo_atencion_mostrar = "-"
tiempo_reparacion_mostrar = "-"
decision_cafe_mostrar = "-"


# =========================================================
# PRIMERA LLEGADA (generada ANTES de la fila inicial)
# =========================================================

rnd_llegada, tiempo_entre_llegadas = uniforme(13, 17)
tiempo_entre_llegadas_mostrar = tiempo_entre_llegadas
prox_llegada = reloj + tiempo_entre_llegadas


# =========================================================
# LISTA DE FILAS MOSTRADAS
# =========================================================

filas_mostradas = []

fila_inicial = {
    "Fila": 0,
    "Reloj": 0,
    "Evento": "Inicializacion",
    "RND Llegada": rnd_llegada,
    "Tiempo Entre Llegadas": tiempo_entre_llegadas,
    "RND Tipo": "-",
    "Tipo Cliente": "-",
    "RND Atencion": "-",
    "Tiempo Atencion": "-",
    "RND Reparacion": "-",
    "Tiempo Reparacion": "-",
    "RND Cafe": "-",
    "Decision Cafe": "-",
    "Estado Ayudante": estado_ayudante,
    "Estado Relojero": estado_relojero,
    "Cliente Actual": "-",
    "Cola Ayudante": 0,
    "Cola Reparacion": 0,
    "Relojes Reparados": relojes_reparados,
    "Prox Llegada": round(prox_llegada, 2),
    "Fin Atencion": "-",
    "Fin Reparacion": "-",
    "Fin Cafe": "-",
    "Ac Ocup Ayudante": 0,
    "Ac Ocup Relojero": 0,
    "Cont Retiros": 0,
    "Cont Retiros Fallidos": 0,
    "Cont Cafes": 0
}

if mostrar_desde == 0:
    filas_mostradas.append(fila_inicial)


# =========================================================
# FUNCION AUXILIAR
# =========================================================

def iniciar_reparacion():
    global estado_relojero
    global prox_fin_reparacion
    global rnd_reparacion
    global tiempo_reparacion_mostrar

    estado_relojero = "Ocupado"
    rnd_reparacion, tiempo_reparacion = uniforme(18, 22)
    tiempo_reparacion_mostrar = tiempo_reparacion
    prox_fin_reparacion = reloj + tiempo_reparacion


# =========================================================
# MOTOR PRINCIPAL
# =========================================================

while reloj < tiempo_simulacion and fila < max_iteraciones:

    # =====================================================
    # BUSCAR PROXIMO EVENTO
    # =====================================================

    eventos = {
        "LlegadaCliente": prox_llegada,
        "FinAtencion": prox_fin_atencion,
        "FinReparacion": prox_fin_reparacion,
        "FinCafe": prox_fin_cafe
    }

    evento = min(eventos, key=eventos.get)

    reloj_anterior = reloj
    reloj = eventos[evento]

    # =====================================================
    # ACTUALIZAR OCUPACIONES
    # =====================================================

    delta = reloj - reloj_anterior

    if estado_ayudante == "Ocupado":
        ac_ocupacion_ayudante += delta

    if estado_relojero == "Ocupado":
        ac_ocupacion_relojero += delta

    # =====================================================
    # RESETEAR RANDOMS
    # =====================================================

    rnd_tipo = "-"
    rnd_atencion = "-"
    rnd_reparacion = "-"
    rnd_cafe = "-"
    tiempo_entre_llegadas_mostrar = "-"
    tipo_cliente_mostrar = "-"
    tiempo_atencion_mostrar = "-"
    tiempo_reparacion_mostrar = "-"
    decision_cafe_mostrar = "-"

    # =====================================================
    # EVENTO: LLEGADA CLIENTE
    # =====================================================

    if evento == "LlegadaCliente":

        # -----------------------------------------
        # GENERAR PROXIMA LLEGADA
        # -----------------------------------------

        rnd_llegada, tiempo_entre_llegadas = uniforme(13, 17)
        tiempo_entre_llegadas_mostrar = tiempo_entre_llegadas
        prox_llegada = reloj + tiempo_entre_llegadas

        # -----------------------------------------
        # TIPO CLIENTE
        # -----------------------------------------

        rnd_tipo, tipo_cliente = generar_tipo_cliente()
        tipo_cliente_mostrar = tipo_cliente

        # -----------------------------------------
        # AYUDANTE LIBRE
        # -----------------------------------------

        if estado_ayudante == "Libre":
            estado_ayudante = "Ocupado"
            cliente_actual = tipo_cliente

            if tipo_cliente == "Compra":
                rnd_atencion, tiempo_atencion = uniforme(6, 10)
                tiempo_atencion_mostrar = tiempo_atencion
            else:
                tiempo_atencion = 3
                tiempo_atencion_mostrar = 3

            prox_fin_atencion = reloj + tiempo_atencion
        else:
            cola_ayudante.append(tipo_cliente)

    # =====================================================
    # EVENTO: FIN ATENCION
    # =====================================================

    elif evento == "FinAtencion":

        # -----------------------------------------
        # ENTREGA RELOJ
        # -----------------------------------------

        if cliente_actual == "Entrega":
            cola_reparacion.append("Reloj")
            if estado_relojero == "Libre":
                cola_reparacion.pop(0)
                iniciar_reparacion()

        # -----------------------------------------
        # RETIRO
        # -----------------------------------------

        elif cliente_actual == "Retiro":
            cont_retiros += 1
            if relojes_reparados > 0:
                relojes_reparados -= 1
            else:
                cont_retiros_fallidos += 1

        # -----------------------------------------
        # SIGUIENTE CLIENTE
        # -----------------------------------------

        if len(cola_ayudante) > 0:
            siguiente_cliente = cola_ayudante.pop(0)
            cliente_actual = siguiente_cliente
            estado_ayudante = "Ocupado"

            if siguiente_cliente == "Compra":
                rnd_atencion, tiempo_atencion = uniforme(6, 10)
                tiempo_atencion_mostrar = tiempo_atencion
            else:
                tiempo_atencion = 3
                tiempo_atencion_mostrar = 3

            prox_fin_atencion = reloj + tiempo_atencion
        else:
            estado_ayudante = "Libre"
            cliente_actual = None
            prox_fin_atencion = math.inf

    # =====================================================
    # EVENTO: FIN REPARACION
    # =====================================================

    elif evento == "FinReparacion":

        relojes_reparados += 1
        prox_fin_reparacion = math.inf

        # -----------------------------------------
        # DECIDIR CAFE
        # -----------------------------------------

        rnd_cafe, toma_cafe = decidir_cafe()
        if toma_cafe:
            decision_cafe_mostrar = "Toma Cafe"
        else:
            decision_cafe_mostrar = "No Toma Cafe"

        if toma_cafe:
            cont_cafes += 1
            estado_relojero = "Cafe"
            prox_fin_cafe = reloj + 5
        else:
            if len(cola_reparacion) > 0:
                cola_reparacion.pop(0)
                iniciar_reparacion()
            else:
                estado_relojero = "Libre"

    # =====================================================
    # EVENTO: FIN CAFE
    # =====================================================

    elif evento == "FinCafe":
        prox_fin_cafe = math.inf
        if len(cola_reparacion) > 0:
            cola_reparacion.pop(0)
            iniciar_reparacion()
        else:
            estado_relojero = "Libre"

    # =====================================================
    # ARMAR FILA VECTOR
    # =====================================================

    fila_vector = {
        "Fila": fila,
        "Reloj": round(reloj, 2),
        "Evento": evento,
        "RND Llegada": rnd_llegada,
        "Tiempo Entre Llegadas": tiempo_entre_llegadas_mostrar,
        "RND Tipo": rnd_tipo,
        "Tipo Cliente": tipo_cliente_mostrar,
        "RND Atencion": rnd_atencion,
        "Tiempo Atencion": tiempo_atencion_mostrar,
        "RND Reparacion": rnd_reparacion,
        "Tiempo Reparacion": tiempo_reparacion_mostrar,
        "RND Cafe": rnd_cafe,
        "Decision Cafe": decision_cafe_mostrar,
        "Estado Ayudante": estado_ayudante,
        "Estado Relojero": estado_relojero,
        "Cliente Actual": cliente_actual,
        "Cola Ayudante": len(cola_ayudante),
        "Cola Reparacion": len(cola_reparacion),
        "Relojes Reparados": relojes_reparados,
        "Prox Llegada": round(prox_llegada, 2),
        "Fin Atencion": round(prox_fin_atencion, 2) if prox_fin_atencion != math.inf else "-",
        "Fin Reparacion": round(prox_fin_reparacion, 2) if prox_fin_reparacion != math.inf else "-",
        "Fin Cafe": round(prox_fin_cafe, 2) if prox_fin_cafe != math.inf else "-",
        "Ac Ocup Ayudante": round(ac_ocupacion_ayudante, 2),
        "Ac Ocup Relojero": round(ac_ocupacion_relojero, 2),
        "Cont Retiros": cont_retiros,
        "Cont Retiros Fallidos": cont_retiros_fallidos,
        "Cont Cafes": cont_cafes
    }

    # =====================================================
    # GUARDAR SOLO FILAS NECESARIAS
    # =====================================================

    if fila >= mostrar_desde and fila < (mostrar_desde + cantidad_mostrar):
        filas_mostradas.append(fila_vector)

    fila += 1


# =========================================================
# AGREGAR ULTIMA FILA
# =========================================================

if len(filas_mostradas) == 0 or filas_mostradas[-1] != fila_vector:
    filas_mostradas.append(fila_vector)


# =========================================================
# ANALISIS FINAL
# =========================================================

if cont_retiros > 0:
    prob_retiro_fallido = cont_retiros_fallidos / cont_retiros
else:
    prob_retiro_fallido = 0

if reloj > 0:
    ocupacion_ayudante = ac_ocupacion_ayudante / reloj
    ocupacion_relojero = ac_ocupacion_relojero / reloj
else:
    ocupacion_ayudante = 0
    ocupacion_relojero = 0

if reloj > 0:
    dias = reloj / 480
    promedio_cafes = cont_cafes / dias
else:
    promedio_cafes = 0


# =========================================================
# RESULTADOS
# =========================================================

print("\n====================================")
print("RESULTADOS FINALES")
print("====================================")
print(f"\nTiempo simulado: {round(reloj,2)}")
print(f"\nProbabilidad retiro fallido: {round(prob_retiro_fallido,4)}")
print(f"\nOcupacion ayudante: {round(ocupacion_ayudante,4)}")
print(f"\nOcupacion relojero: {round(ocupacion_relojero,4)}")
print(f"\nPromedio cafes por dia: {round(promedio_cafes,4)}")


# =========================================================
# EXPORTAR EXCEL
# =========================================================

df = pd.DataFrame(filas_mostradas)
df.to_excel("resultados/simulacion.xlsx", index=False)
print("\nExcel generado correctamente.")