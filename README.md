# Simulador_De_Colas_Relojero-B
Objetivos del trabajo
Analizar el funcionamiento de un sistema de reparación y retiro de relojes.
Modelar el sistema mediante simulación por eventos discretos.
Construir el vector de estado correspondiente.
Implementar un aplicativo capaz de simular el comportamiento del sistema.
Obtener métricas de desempeño tales como:
Probabilidad de retiro fallido.
Porcentaje de ocupación del ayudante.
Porcentaje de ocupación del relojero.
Cantidad promedio de cafés consumidos por día por el relojero.
Enunciado del TP 4:
Relojería B
En un negocio de arreglo y venta de relojes hay un relojero y su ayudante.
El ayudante tiene como tarea atender a las personas que entran en el negocio (llegan respetando una distribución uniforme entre 13 y 17 minutos), ya sea para comprar (45%), para entregar relojes para reparar (25%) o para retirar relojes reparados (30%).
Si el cliente quiere comprar, el tiempo de la venta es de 6 a 10 minutos uniformemente distribuidos. Si el cliente viene a retirar o entregar relojes, se demora en la atención del mismo, 3 minutos.
El relojero se encarga de la reparación de los relojes, demorando en esta tarea U(18 ; 22) minutos. Al finalizar su tarea el 10% de las veces el relojero se toma un cafecito que demora 5 minutos.
Inicialmente hay 3 relojes en espera de ser retirados.
Determine la probabilidad de que un cliente llegue a retirar un reloj y que el mismo no esté reparado aún.
Determine el porcentaje de ocupación del ayudante y del relojero.
Cantidad promedio de cafecitos por día que toma el relojero.


1. Identificación de Objetos
1.1 Ayudante
Tipo: Permanente (Servidor)
Atributos:
Atributo
Valores posibles
Estado
Desocupado, Atendiendo

Descripción: Es el encargado de atender a los clientes que llegan a la relojería. Realiza las operaciones de venta, recepción de relojes para reparación y entrega de relojes reparados.

1.2 Relojero
Tipo: Permanente (Servidor)
Atributos:
Atributo
Valores posibles
Estado
Desocupado, Reparando, Tomando café

Descripción: Es el encargado de reparar los relojes recibidos. Al finalizar una reparación puede decidir tomar un café con una probabilidad del 10%.

1.3 Cliente
Tipo: Temporal
Atributos:
Atributo
Valores posibles
Estado
Esperando atención, Comprando, Entregando reloj, Retirando reloj

Descripción: Representa a cada cliente que llega al sistema. Durante su atención puede realizar una compra, entregar un reloj para reparación o retirar un reloj previamente ingresado (aunque por diseño de la simulación, no hay trazabilidad entre relojes y clientes).

1.4 Reloj
Tipo: Temporal
Atributos:
Atributo
Valores posibles
Estado
Esperando ser retirado, Siendo reparado

Descripción: Representa cada reloj ingresado al sistema para su reparación.


2. Determinación de Eventos
Los eventos que provocan cambios de estado en el sistema son:
Llegada de cliente
Ocurre cuando un nuevo cliente ingresa a la relojería. Si el ayudante se encuentra libre comienza su atención; caso contrario, el cliente espera en la cola correspondiente.
Fin de atención
Ocurre cuando el ayudante finaliza la atención de un cliente. Dependiendo del tipo de operación realizada pueden generarse nuevos relojes para reparar, retirarse relojes reparados o simplemente finalizar la compra.
Fin de reparación de reloj
Ocurre cuando el relojero concluye la reparación de un reloj. El reloj pasa a estar esperando en la cola, disponible para su posterior retiro.
Decidir tomar café
Evento que ocurre inmediatamente después de finalizar una reparación de reloj. Con probabilidad 0,10 el relojero comienza una pausa para tomar café.
Fin de café
Ocurre cuando termina la pausa de cinco minutos del relojero. A partir de ese momento puede volver a tomar relojes pendientes de reparación.

3. Colas Existentes en el Sistema
Cola de clientes esperando atención
Disciplina: FIFO (First In First Out)
Contenido: Clientes que llegan mientras el ayudante se encuentra ocupado.
Capacidad: Ilimitada.

Cola de relojes por reparar
Disciplina: FIFO (First In First Out)
Contenido: Relojes entregados por los clientes que aún no han sido tomados por el relojero.
Capacidad: Ilimitada.

Cola de relojes reparados para retirar
Disciplina: FIFO (First In First Out)
Contenido: Relojes cuya reparación finalizó y se encuentran disponibles para ser retirados 
Capacidad: Ilimitada.


4. Variables Aleatorias
Tiempo entre llegadas de clientes
Distribución Uniforme entre 13 y 17 minutos.
Variable aleatoria:
X ~ U(13,17)
Generación:
X = 13 + RND × (17 - 13)
X = 13 + 4 × RND

Tipo de atención solicitada por el cliente
Distribución discreta:
Acción
Probabilidad
Compra
0,45
Entrega reloj para reparación
0,25
Retiro de reloj
0,30

Generación:
Sea RND un número aleatorio uniforme entre 0 y 1:
Si 0 ≤ RND < 0,45 → Compra.
Si 0,45 ≤ RND < 0,70 → Entrega reloj.
Si 0,70 ≤ RND ≤ 1,00 → Retiro de reloj.


Tiempo de atención del ayudante para una compra
Distribución Uniforme entre 6 y 10 minutos.
Variable aleatoria:
X ~ U(6,10)
Generación:
X = 6 + RND × (10 - 6)
X = 6 + 4 × RND

Tiempo de atención para entregar o retirar un reloj
Tiempo constante.
Valor:
X = 3 minutos

Tiempo de reparación de un reloj
Distribución Uniforme entre 18 y 22 minutos.
Variable aleatoria:
X ~ U(18,22)
Generación:
X = 18 + RND × (22 - 18)
X = 18 + 4 × RND


Decisión de tomar café
Probabilidad de tomar café:
P = 0,10
Generación:
Si RND < 0,10 → Toma café.
Si RND ≥ 0,10 → No toma café.

Tiempo de café
Tiempo constante.
Valor:
X = 5 minutos
