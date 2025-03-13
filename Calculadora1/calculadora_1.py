#!/usr/bin/env python3

"""
Título de práctica: breve descripción

Descripción extendida del programa

Autor: ElAutor <el@correo>
Fecha: 2025-02-01
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.


def calculator():
    """Calculadora básica con operaciones aritméticas."""
    try:
        a = float(input("> Ingrese el operando A:\n< "))
        b = float(input("> Ingrese el operando B:\n< "))

        print("> Cual operación se va a realizar?")
        print("> Escriba 1 para suma, ")
        print(">         2 para resta, ")
        print(">         3 para multiplicación ")
        print(">       y 4 para división.")

        opcion = int(input("< "))

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
        else:
            print("> Opción inválida.")
            return

        print(f"> El resultado es: {resultado}")

    except ValueError:
        print("> Error: Entrada inválida. Asegúrese de ingresar números válidos.")


def run():
    """Punto de entrada del script"""
    # Llamar a la calculadora
    calculator()


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
