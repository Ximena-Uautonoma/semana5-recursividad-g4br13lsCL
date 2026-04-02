"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
resultado = 0
    for i in range(1, n + 1):
        resultado = resultado + i
    return resultado

def suma_recursiva(n):
if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n - 1)