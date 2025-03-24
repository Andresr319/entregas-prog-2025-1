#!/usr/bin/env python3

"""
Título de práctica: breve descripción

Descripción extendida del programa

Autor: ElAutor <andres>
Fecha: 2025-03-10

"""

def es_numero(valor):
    """Verifica si el valor ingresado es un número válido (permite decimales)."""
    return valor.replace('.', '', 1).isdigit() or (valor.startswith('-') and valor[1:].replace('.', '', 1).isdigit())

def calculator():
    """Calculadora básica con operaciones aritméticas sin try-except."""
    
    a = input("> Ingrese el operando A:\n< ")
    while not es_numero(a):
        print("> Error: Entrada inválida. Asegúrese de ingresar un número válido.")
        a = input("< ")

    b = input("> Ingrese el operando B:\n< ")
    while not es_numero(b):
        print("> Error: Entrada inválida. Asegúrese de ingresar un número válido.")
        b = input("< ")

    a, b = float(a), float(b)

    print("> ¿Qué operación desea realizar?")
    print("> Escriba 1 para suma, ")
    print(">         2 para resta, ")
    print(">         3 para multiplicación ")
    print(">       y 4 para división.")

    opcion = input("< ")
    while opcion not in ('1', '2', '3', '4'):
        print("> Opción inválida. Intente de nuevo.")
        opcion = input("< ")

    opcion = int(opcion)

    if opcion == 1:
        resultado = a + b
    elif opcion == 2:
        resultado = a - b
    elif opcion == 3:
        resultado = a * b
    elif opcion == 4:
        if b != 0:
            resultado = a / b
        else:
            print("> Error: No se puede dividir por cero.")
            return

    print(f"> El resultado es: {resultado}")

def run():
    """Punto de entrada del script"""
    calculator()


if __name__ == "__main__":
    run()
