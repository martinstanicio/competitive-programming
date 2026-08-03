# Estrategias de equipo

Los eventos de programación competitiva suelen durar cinco horas, que parece mucho tiempo, pero en la práctica nunca es suficiente. Sin embargo, el equipo está formado por tres integrantes, lo que nos da **15 horas-humano** para resolver los problemas. Por eso es importante ponerse de acuerdo y aplicar ciertas estrategias para aprovechar al máximo el tiempo.

## Objetivo a tener en mente

El ganador de la competencia es el equipo que resuelva más problemas en el menor tiempo posible. Por eso, siempre hay que tener presente que el objetivo es **maximizar la cantidad de problemas resueltos**, no necesariamente resolver el más difícil.

En todo momento, se debe priorizar el **problema más fácil**, que es aquel que se estima que requiere **menos tiempo para ser aceptado en ese instante**.

> [!important]
> Podemos tener un problema muy complejo, pero que solo nos falten 5 minutos de escribir código para que sea aceptado.
>
> Bajo nuestro criterio, ese es el problema más fácil, y por lo tanto el que debemos **resolver primero**.

## La tablita

La tablita es una herramienta fundamental para el equipo. Es una hoja donde se anotan todos los problemas, y toda la información relevante sobre ellos. Cada equipo puede tener sus propias convenciones, pero lo importante es que **todos los integrantes puedan leerla y entenderla**.

Algunas ideas para armar la tablita:

- **Identificador del problema:** La letra del enunciado, y una palabra o frase breve que lo identifique, que puede ser el mismo título del problema, o algo más descriptivo como _el problema del auto_.

- **Estado del problema:** Se puede representar con rayitas, por ejemplo, una rayita si fue leído, dos rayitas si fue entendido, tres rayitas si se está pensando en la solución, y cuatro rayitas si se está programando. Los problemas resueltos deben ser tachados.

- **Dificultad y tiempo estimado:** Estimativo de la dificultad (fácil, medio, difícil) y el tiempo que se cree que llevará resolverlo. Esto ayuda a priorizar los problemas más fáciles. Con la práctica, el equipo se vuelve más preciso en estas estimaciones.

- **Solución:** Breve descripción de la idea que se cree que resolverá el problema, como _usar DFS y contar componentes conexas_. Puede que la solución final sea diferente, y es otra cosa que el equipo será mejor estimando con la práctica.

- **Hora de inicio:** Anotar la hora en que se empieza a trabajar en un problema, para detectar si le estamos dedicando demasiado tiempo y conviene cambiar de problema.

> [!tip]
> Se recomienda asignar un responsable de la tablita, que se encargue de actualizarla con el progreso del equipo.

## Primera hora de competencia

Durante la primera etapa del evento, es importante completar la tablita con todos los problemas, para que el equipo pueda priorizar y decidir en qué problemas trabajar. Se recomienda que **cada integrante lea un tercio de los problemas** y complete su parte de la tablita.

Los primeros problemas probablemente se resuelvan en poco tiempo, y no requieran más de una persona para resolver cada uno. Este puede ser el único momento de la competencia en el que haya una cola de problemas resueltos, pero esperando a ser programados.

Es importante que todos los integrantes sepan **plasmar soluciones en papel** de forma clara, para que el programador designado pueda implementarlas sin interrumpir al resto del equipo, que debe pasar a **resolver otros problemas**.

> [!warning]
> Aunque al principio de la competencia es mejor dividir la lectura de los problemas, a medida que se resuelven los problemas más fáciles, es recomendable que todos los integrantes lean todos los problemas, o al menos sepan de qué trata cada uno.

## Uso del scoreboard

Durante la competencia, es posible ver el scoreboard, que muestra cuándo y qué problemas resolvieron los demás equipos. Los **problemas más resueltos** suelen ser los más fáciles, y es un buen indicador de qué problemas conviene priorizar.

> [!caution]
> El scoreboard se pausa durante la última hora de competencia.

## Roles y dinámica de trabajo

No es necesario que los tres integrantes del equipo programen, sino que normalmente se asignan **dos programadores**.

Quien no programa se encarga exclusivamente de analizar problemas y pensar soluciones, y también puede ser el **responsable de la tablita**.

> [!warning]
> Dentro de lo posible, evitar interrumpir a quien esté programando, para reducir la probabilidad de errores por falta de concentración.

## Reuniones de equipo

Realizar reuniones periódicas para analizar el progreso y definir la estrategia que se busca seguir. Especialmente durante la **última hora**, cuando se pausa el scoreboard, ya que no tendremos tanto tiempo para resolver problemas, y nunca hay que olvidar que el objetivo es **maximizar la cantidad** de problemas resueltos.

## Pair Programming

Es una técnica en la que dos programadores trabajan juntos en una sola computadora. Uno escribe el código mientras el otro revisa y asiste. Dos cabezas sobre un mismo problema ayudan a reducir errores.

## Impresión de soluciones

En cualquier momento de la competencia, es posible solicitar la impresión de un problema resuelto, para que el equipo pueda **debuggear en papel** sin ocupar la computadora.

> [!note]
> Algunos equipos imprimen el 100% de las soluciones inmediatamente después de enviarlas, sin esperar la respuesta del jurado, para no perder tiempo esperando en caso de que haya que debuggear.

## Reglas estrictas de trabajo

- **La computadora es solo para escribir:** Si estando en el teclado empezás a replantearte la implementación o a pensar el algoritmo, **hay que levantarse y volver al papel**.

- **Cada integrante debe leer el enunciado por su cuenta.** No hay que explicárselo verbalmente a un compañero para evitar transmitirle una interpretación errónea.

- **Desbloqueo de problemas:** Si un problema no sale, le pedimos a un compañero que piense una solución **sin contarle nuestra idea previa**, para que aporte una perspectiva fresca y sin sesgos.

- **Código limpio desde el inicio:** Nunca escribir código feo para ganar tiempo. Arreglar un programa rechazado con malas prácticas consume mucho más tiempo y energía.

## Checklist pre-envío

Serie de pasos a seguir antes de realizar **cualquier envío**. Fundamental para evitar errores tontos que nos hagan perder tiempo y puntos.

- **Eliminar rastros de debugging:** Revisar todos los `print` del programa, que puedan hacer que el output sea incorrecto.

- **Revisar casos borde:** Ejecutar el programa con casos de prueba que utilicen valores límite, como el mínimo y máximo de cada variable de entrada, casos vacíos, condiciones que puedan generar división por cero, puntos alineados en problemas de geometría, etc.

- **Revisar índices en vectores y strings:** Los datos de entrada suelen estar indexados desde 1. Asegurarse de que se reste 1 al ingresar los datos, y que se sume 1 al imprimirlos, si fuera necesario.

- **Seleccionar compilador/interprete y versión correctos:** Principalmente si el equipo trabaja con varios lenguajes de programación, siempre verificar que se esté usando el compilador o intérprete correcto antes de enviar.
