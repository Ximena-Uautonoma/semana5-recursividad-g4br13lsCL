"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
total = 0
    for monto in ventas:
        total = total + monto
    return total


def total_ventas_recursivo(ventas):
if not ventas: 
        return 0
    else:
        
        return ventas[0] + total_ventas_recursivo(ventas[1:])