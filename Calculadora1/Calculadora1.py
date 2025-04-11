#!/usr/bin/env python3

"""
Título de práctica: Calculadora básica

Este programa realiza operaciones aritméticas simples
(suma, resta, multiplicación y división) entre dos números
ingresados por el usuario.

Autor: ElAutor <andres>
Fecha: 2025-03-10
"""

import unittest


def es_numero(valor):
    """Valida si el valor ingresado es un número (decimal o negativo)."""
    return (
        valor.replace('.', '', 1).isdigit()
        or (
            valor.startswith('-')
            and valor[1:].replace('.', '', 1).isdigit()
        )
    )


def operar(a, b, opcion):
    """Realiza la operación indicada: 1=suma, 2=resta, 3=mult, 4=div."""
    if opcion == 1:
        return a + b
    elif opcion == 2:
        return a - b
    elif opcion == 3:
        return a * b
    elif opcion == 4:
        if b != 0:
            return a / b
        return "Error: División por cero."
    return "Error: Opción inválida."


def calculator():
    """Calculadora con entrada de datos desde consola."""
    a = input("> Ingrese el operando A:\n< ")
    while not es_numero(a):
        print("> Error: Ingrese un número válido.")
        a = input("< ")

    b = input("> Ingrese el operando B:\n< ")
    while not es_numero(b):
        print("> Error: Ingrese un número válido.")
        b = input("< ")

    a, b = float(a), float(b)

    print("> ¿Qué operación desea realizar?")
    print("> 1: Suma\n> 2: Resta\n> 3: Multiplicación\n> 4: División")

    opcion = input("< ")
    while opcion not in ('1', '2', '3', '4'):
        print("> Opción inválida. Intente de nuevo.")
        opcion = input("< ")

    opcion = int(opcion)
    resultado = operar(a, b, opcion)
    print(f"> El resultado es: {resultado}")


def run():
    """Punto de entrada del programa."""
    calculator()


class TestCalculadora(unittest.TestCase):
    def test_operaciones(self):
        self.assertEqual(operar(2, 3, 1), 5)
        self.assertEqual(operar(5, 2, 2), 3)
        self.assertEqual(operar(4, 3, 3), 12)
        self.assertEqual(operar(10, 2, 4), 5)
        self.assertEqual(operar(5, 0, 4), "Error: División por cero.")
        self.assertEqual(operar(1, 1, 9), "Error: Opción inválida.")


if __name__ == "__main__":
    run()
    # Para ejecutar los tests: descomenta la siguiente línea
    # unittest.main()
