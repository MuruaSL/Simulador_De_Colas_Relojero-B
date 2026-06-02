# Simulador_De_Colas_Relojero-B
# Simulador Relojería "B" - Guía Rápida

## 🎯 Qué hace el simulador

Simula una relojería con **ayudante** (atiende clientes) y **relojero** (repara relojes). Usa **eventos discretos** (el tiempo avanza de un evento al próximo, no en intervalos fijos).

---

## 📊 Métricas que calcula

| Métrica | Fórmula |
|---------|---------|
| Probabilidad retiro fallido | `retiros_fallidos / retiros_totales` |
| Ocupación ayudante | `tiempo_ayudante_ocupado / tiempo_total` |
| Ocupación relojero | `tiempo_relojero_reparando / tiempo_total` |
| Promedio cafés/día | `cafés / (tiempo_total / 480)` |

> 480 minutos = 8 horas (1 día laboral)

---

## ⚙️ Cómo funciona el código

### Loop principal (cada iteración = un evento)

```python
1. Buscar próximo evento (Llegada / FinAtencion / FinReparacion / FinCafe)
2. Avanzar el reloj hasta ese momento
3. Acumular tiempo de ocupación de los servidores
4. Ejecutar el evento
5. Guardar el vector de estado (fila del Excel)
Qué hace cada evento

Evento	Acciones
Llegada	Genera próxima llegada U(13,17). Si ayudante libre → atiende; si no → encola.
FinAtencion	Si era Entrega → agrega reloj a reparación. Si era Retiro → intenta restar 1 de relojes_reparados. Atiende próximo cliente o deja libre al ayudante.
FinReparacion	Suma 1 a relojes_reparados. 10% probabilidad de café (5 min); si no, repara próximo reloj.
FinCafe	Termina pausa. Si hay relojes en cola → repara; si no → relojero libre.
Variables clave

relojes_reparados = stock de relojes listos para retiro (arranca en 3)
cola_ayudante = clientes esperando (FIFO)
cola_reparacion = relojes esperando reparación (FIFO)
🎲 Variables aleatorias

Qué se genera	Distribución
Tiempo entre llegadas	U(13, 17)
Tipo de cliente	45% Compra / 25% Entrega / 30% Retiro
Duración de compra	U(6, 10)
Duración entrega/retiro	3 minutos (fijo)
Duración reparación	U(18, 22)
¿Toma café?	10% sí / 90% no
Duración café	5 minutos (fijo)
🖥️ Estructura de archivos

Archivo	Función
main.py	Motor de simulación (lógica de eventos)
gui.py	Interfaz gráfica (PyQt6)
resultados/simulacion.xlsx	Excel con el vector de estado
🚀 Cómo ejecutar

bash
python gui.py          # Interfaz gráfica (recomendado)
python main.py         # Consola
❓ Preguntas típicas del oral (respuestas cortas)

¿Por qué eventos discretos?
Más eficiente: solo evaluamos cuando algo cambia.

¿Qué pasa si un retiro no tiene reloj?
Se cuenta como retiro_fallido → cliente se va sin nada.

¿Cómo se acumula la ocupación?
delta = tiempo_actual - tiempo_anterior. Si el servidor estaba ocupado, se suma delta a su acumulador.

¿Por qué math.inf?
Para que los eventos no programados nunca sean elegidos como el próximo.

¿Por qué no hay trazabilidad cliente-reloj?
Definición de cátedra: cualquier cliente puede retirar cualquier reloj disponible.

¿Se puede reproducir la simulación?
Sí, agregando random.seed(42) al inicio de main.py.

📋 Resumen del vector de estado (columnas del Excel)

Columna	Qué contiene
Fila	N° de evento
Reloj	Tiempo actual
Evento	Llegada / FinAtencion / FinReparacion / FinCafe
Tipo Cliente	Compra / Entrega / Retiro
Estado Ayudante	Libre / Ocupado
Estado Relojero	Libre / Ocupado / Cafe
Cola Ayudante	Clientes esperando
Cola Reparacion	Relojes por reparar
Relojes Reparados	Stock para retiro
RND x	Números aleatorios usados
Tiempo x	Valores generados
Ac Ocup...	Tiempo acumulado ocupado
Contadores	Retiros, fallidos, cafés
✅ Checklist de cumplimiento

Simulación por eventos discretos
Uniformes: llegadas (13-17), compras (6-10), reparaciones (18-22)
Probabilidades: 45/25/30 para tipos de cliente
Café: 10% / 5 minutos
3 relojes iniciales
Probabilidad retiro fallido
Ocupación ayudante y relojero
Promedio cafés/día
Exportación a Excel
Interfaz gráfica