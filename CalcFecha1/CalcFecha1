#!/usr/bin/env python3

"""
Ejercicio 02: Manipulación básica de fechas con segundos y días.

Este script muestra la fecha actual y permite al usuario añadir
segundos o días a esa fecha.

Autor: Andres Rachen
Correo: Andressantiagopapamija@gmail.com
Fecha: 2025-05-05
"""

from datetime import datetime, timedelta


def manipular_fechas():
    """Menú para manipular fechas añadiendo segundos o días."""
    while True:
        fecha_actual = datetime.now()
        print(f"\n> Fecha actual: {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}")
        print("> Opciones:")
        print("> 1: Añadir segundos")
        print("> 2: Añadir días")
        print("> 3: Salir")

        opcion = input("< ")

        if opcion == "1":
            try:
                segundos = int(input("> Introduzca la cantidad de segundos: "))
                nueva_fecha = fecha_actual + timedelta(seconds=segundos)
                print(f"> Nueva fecha: {nueva_fecha.strftime('%Y-%m-%d %H:%M:%S')}")
            except ValueError:
                print("> Error: Por favor, ingrese un número entero válido.")

        elif opcion == "2":
            try:
                dias = int(input("> Introduzca la cantidad de días: "))
                nueva_fecha = fecha_actual + timedelta(days=dias)
                print(f"> Nueva fecha: {nueva_fecha.strftime('%Y-%m-%d %H:%M:%S')}")
            except ValueError:
                print("> Error: Por favor, ingrese un número entero válido.")

        elif opcion == "3":
            print("> ¡Gracias por usar el programa!")
            break

        else:
            print("> Opción no válida, intente de nuevo.")


if __name__ == "Andres":
    manipular_fechas()
