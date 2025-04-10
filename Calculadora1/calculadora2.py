#!/usr/bin/env python3

"""
Título de práctica: Calculadora en Python

Descripción: Calculadora básica con operaciones matemáticas simples.

Autor: Andres
Fecha: 2025-04-08
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error"

def potenciacion(a, b):
    return a ** b

def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error"

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error"

def obtener_numero(mensaje):
    valor = input(mensaje)
    if valor == "":
        print("> Operación cancelada")
        return None
    if valor.replace(".", "").isdigit():
        return float(valor)
    else:
        print("> Solo se permiten números.")
        return None

def run():
    print("¡Hola programador!")

    Salir = "si"
    while Salir == "si":
        print("> Escriba 1 para suma, \n>         2 para resta, \n>         3 para multiplicación \n>         4 para división.\n>         5 para potenciación.\n>         6 para división entera.\n>         7 para módulo.\n>         8 para salir.")
        opcion = input("< ")

        if opcion == '8':
            print("> Gracias!")
            break

        if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4' or opcion == '5' or opcion == '6' or opcion == '7':
            num1 = obtener_numero("> Ingrese el operando A:\n< ")
            if num1 is None:
                continue

            num2 = obtener_numero("> Ingrese el operando B:\n< ")
            if num2 is None:
                continue

            if opcion == '1':
                print("> El resultado de la suma es:", suma(num1, num2))
            if opcion == '2':
                print("> El resultado de la resta es:", resta(num1, num2))
            if opcion == '3':
                print("> El resultado de la multiplicación es:", multiplicacion(num1, num2))
            if opcion == '4':
                print("> El resultado de la división es:", division(num1, num2))
            if opcion == '5':
                print("> El resultado de la potenciación es:", potenciacion(num1, num2))
            if opcion == '6':
                print("> El resultado de la división entera es:", division_entera(num1, num2))
            if opcion == '7':
                print("> El resultado del módulo es:", modulo(num1, num2))
        else:
            print("> Opción no válida.")

        Salir = input("> ¿Desea hacer otra operación? (sí/no): ").lower()

if __name__ == "__main__":
    run()
