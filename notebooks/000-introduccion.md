# Introducción a la programación competitiva

Resumen de los conceptos fundamentales para iniciarse en la programación competitiva, especificamente utilizando **Python**.

## Sistema de evaluación (el juez)

El sistema de evaluación, también conocido como "juez", es el entorno que se encarga de ejecutar las soluciones enviadas por los concursantes. Su veredicto puede ser uno de los siguientes:

- **Accepted (AC)**: La solución es correcta, cumple con todos los casos de prueba.

- **Wrong Answer (WA)**: La solución es incorrecta, no cumple con al menos uno de los casos de prueba.

- **Time Limit Exceeded (TLE)**: La solución excede el tiempo máximo permitido.

- **Memory Limit Exceeded (MLE)**: La solución excede el límite de memoria permitido.

- **Runtime Error (RE)**: La solución falla durante la ejecución de al menos un caso de prueba.

- **Compilation Error (CE)**: La solución no compila, por ejemplo, por errores de sintaxis.

> [!note]
> Todos los veredictos son bastante autoexplicativos, excepto **Runtime Error (RE)**, que requiere un poco más de análisis, ya que puede ocurrir por múltiples razones:
>
> - Acceder a una posición fuera del rango de un arreglo
> - Superar el límite de recursión
> - Dividir por cero
> - Cualquier otra operación que genere una excepción en Python

## Complejidad de tiempo y notación Big O ($\mathcal{O}$)

La complejidad de tiempo permite estimar de forma abstracta el crecimiento del número de operaciones que realiza un algoritmo a medida que aumenta el tamaño de la entrada ($N$), independientemente de la máquina donde se ejecute.

> [!note]
> La regla principal para trabajar con complejidades es **despreciar constantes y términos de menor orden**.
>
> $$
> 3N^2 + 5N + 10 \Rightarrow \mathcal{O}(N^2)
> $$

### Cantidad de operaciones y límites de tiempo

Como regla general, se considera que un programa puede realizar **$10^8$ operaciones por segundo** en promedio.

> [!tip]
> Ciertas optimizaciones pueden permitir que un programa realice más operaciones, pero lo recomendable es pensar algoritmos que no superen este límite para evitar problemas de **Time Limit Exceeded (TLE)**.

### Tabla de complejidades comunes y límites típicos de $N$

| Complejidad | Límite típico de $N$ | Algoritmos / Ejemplos de aplicación |
| :---: | :---: | :--- |
| **$\mathcal{O}(1)$** | $10^{18}$ | Fórmulas matemáticas cerradas, acceso directo en listas/vectores. |
| **$\mathcal{O}(\log N)$** | $10^{18}$ | Búsqueda binaria, exponenciación binaria. |
| **$\mathcal{O}(N)$** | $10^8$ | Recorrido simple con un bucle, two pointers. |
| **$\mathcal{O}(N \log N)$** | $10^6$ | Ordenamiento, estructuras como Segment Tree. |
| **$\mathcal{O}(N^2)$** | $5000$ | Bucles anidados simples, programación dinámica básica. |
| **$\mathcal{O}(N^3)$** | $500$ | Multiplicación de matrices, algoritmos de caminos mínimos como Floyd-Warshall. |
| **$\mathcal{O}(2^N)$** | $20$ | Generación de subconjuntos, backtracking, fuerza bruta. |
| **$\mathcal{O}(N!)$** | $10$ | Generación de todas las permutaciones de un arreglo. |

## Entrada y salida de datos en Python

En programación competitiva, procesar volúmenes grandes de datos mediante las funciones nativas estándar `input()` y `print()` puede introducir consumo de tiempo innecesario.

### Lectura rápida de datos

Para evitar la lentitud de `input()` cuando hay miles de líneas de entrada, se recomienda utilizar directamente la entrada estándar del sistema mediante `sys.stdin.readline`.

```python
import sys

input = sys.stdin.readline

n = int(input())  # un entero por línea
x, y, z = map(int, input().split())  # cantidad fija de enteros en una sola línea
nums = list(map(int, input().split()))  # lista de enteros en una sola línea
```

> [!warning]
> A diferencia de `input()`, `sys.stdin.readline()` **no elimina el salto de línea al final**. Al castear a `int` o `float`, esto no es un problema, pero si se desea obtener un string limpio, es necesario utilizar `.strip()`.

### Escritura rápida de datos

Para imprimir la salida de forma rápida, se recomienda construir el resultado como una lista de strings e imprimir todo unido por saltos de línea con `' \n'.join(...)` o utilizar `sys.stdout.write`.

```python
import sys

answers = [...]

print('\n'.join(map(str, answers)))  # imprimir cada elemento en una línea

for a in answers:
    sys.stdout.write(a + "\n")  # alternativa con sys.stdout.write
```

> [!warning]
> A diferencia de `print()`, `sys.stdout.write()` **no agrega un salto de línea automáticamente**, por lo que es necesario incluirlo explícitamente si se desea.

## Problemas interactivos

En un **problema interactivo**, la entrada y salida se maneja de forma diferente. El programa realiza consultas (*queries*) a la salida estándar, y el juez responde a través de la entrada estándar en tiempo real.

> [!important]
> Lo más importante en un problema interactivo es siempre vaciar el buffer de salida (flush) después de cada consulta.
>
> ```python
> import sys
> 
> print(query, flush=True)
> 
> # alternativa con sys.stdout
> sys.stdout.write(query + "\n")
> sys.stdout.flush()
> ```

## Template recomendado

Es la plantilla con la que se recomienda iniciar a programar cualquier solución: [template.py](../template.py).

### Función `main` o *entrypoint*

Utilizar una función `main()` para escribir el programa principal, en vez de escribirlo directamente en el nivel superior, no solo es una buena práctica, sino que también es **más eficiente que utilizar variables globales**.

### Función `solve`

Es muy común que un problema tenga `t` casos de prueba. Utilizar una función `solve()` permite aislar la lógica de cada uno, y además, permite **retornar anticipadamente** con un `return`.

```python
def solve(x: int) -> bool:
    ...


def main() -> None:
    ...
    for _ in range(test_cases):
        ...
        success: bool = solve(x)
        answers.append("YES" if success else "NO")

    print("\n".join(answers))


if __name__ == "__main__":
    main()
```
