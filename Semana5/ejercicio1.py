"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):

    lista = []
    for i in range(1, n + 1):
        lista = lista + [i]  
    return lista

def contar_recursivo(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    else:
        # Concatenamos la lista de los anteriores con el número actual en una lista nueva
        return contar_recursivo(n - 1) + [n]