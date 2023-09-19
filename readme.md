# Reto

A continuacion estan los ejercicios del punto #3 del reto

## Formas de transponer matriz

##1

```python
matriz1 = [
    [23, 43, 23],
    [42, 54, 61],
    [70, 82, 93]
]

transpuesta1 = [[fila[i] for fila in matriz1] for i in range(len(matriz1[0]))]
print(transpuesta1)

```

## 2

```python
matriz1 = [
    [43, 12, 53],
    [42, 43, 71],
    [21, 67, 82]
]

transpuesta2 = list(map(list, zip(*matriz1)))
print(transpuesta2)
```

## 3

```python
import numpy as np
matriz1 = [
    [55, 76, 73],
    [75, 56, 19],
    [21, 67, 20]
]


matriz_np = np.array(matriz1)
transpuesta3 = matriz_np.T
print(transpuesta3)

```

## Funciones recursiva y ciclo
En el area de las funciones busque la libreria timeit libreria la cual nos sirve medir el tiempo de ejecucion, con dicha libreria se probo 10 veces el mismo ejercicio bajo las mismas condiciones y se muestra que el ciclo for es un 30% mas eficiente que la función recursiva.


## Ciclo

```python
import timeit

def factorial_ciclo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


start_time = timeit.default_timer()
end_time = 0
factorial_ciclo(100)
end_time = timeit.default_timer()

print("----------------")
print("----------------")
print(end_time-start_time)
```
## Recursiva

```python
import timeit


def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

start_time = timeit.default_timer()
end_time = 0
factorial_recursivo(100)
end_time = timeit.default_timer()

print("----------------")
print("----------------")
print(end_time-start_time)
 ```
