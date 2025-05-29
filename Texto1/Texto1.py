#!/usr/bin/env python3

"""
Ejercicio 02: Menú de manipulación de texto

Este script permite al usuario manipular una cadena de texto
de diferentes formas:
- Convertir a minúsculas
- Convertir a mayúsculas
- Invertir mayúsculas y minúsculas
- Capitalizar (primera letra en mayúscula)
- Titular (cada palabra inicia con mayúscula)
- Reemplazar espacios por guiones bajos

Autor: Tu Nombre <Andressantiagopapamija@gmail.com>
Fecha: 2025-05-05
"""


def run():
    """Punto de entrada del script"""
    # Solicitar al usuario una cadena de texto
    texto = input("< Ingrese una cadena de texto: ")

    while True:
        # Mostrar el menú de opciones
        print("\n> Opciones de manipulación de texto:")
        print("> 1: Convertir a minúsculas")
        print("> 2: Convertir a mayúsculas")
        print("> 3: Invertir mayúsculas y minúsculas")
        print("> 4: Capitalizar (primera letra en mayúscula)")
        print("> 5: Titular (cada palabra inicia con mayúscula)")
        print("> 6: Reemplazar espacios por guiones bajos")
        print("> 7: Salir")

        opcion = input("> Seleccione una opción: ")

        # Ejecutar la opción seleccionada
        if opcion == "1":
            print(f"> Resultado: {texto.lower()}")
        elif opcion == "2":
            print(f"> Resultado: {texto.upper()}")
        elif opcion == "3":
            print(f"> Resultado: {texto.swapcase()}")
        elif opcion == "4":
            print(f"> Resultado: {texto.capitalize()}")
        elif opcion == "5":
            print(f"> Resultado: {texto.title()}")
        elif opcion == "6":
            print(f"> Resultado: {texto.replace(' ', '_')}")
        elif opcion == "7":
            print("> ¡Gracias por usar el programa!")
            break
        else:
            print("> Opción no válida. Por favor, intente de nuevo.")


if __name__ == "Andres":
    run()
