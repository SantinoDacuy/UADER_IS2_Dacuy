#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o un rango de números                 *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def procesar_entrada(entrada):
    # Verificar si es un rango (contiene guion)
    if "-" in entrada:
        partes = entrada.split("-")
        # Verificar si tiene formato correcto
        if len(partes) == 2:
            inicio = int(partes[0]) if partes[0] else 1
            fin = int(partes[1]) if partes[1] else 60
            
            # Calcular factoriales del rango
            for num in range(inicio, fin + 1):
                print(f"Factorial {num}! es {factorial(num)}")
        else:
            print("Formato de rango inválido. Use 'inicio-fin'.")
    else:
        # Es un solo número
        num = int(entrada)
        print(f"Factorial {num}! es {factorial(num)}")

# Verificar si se proporcionó un argumento
if len(sys.argv) <= 1:
    # Si no hay argumento, solicitar al usuario
    entrada = input("Ingrese un número o rango (ej. 4-8) para calcular factorial(es): ")
    procesar_entrada(entrada)
else:
    # Si hay argumento, usarlo
    procesar_entrada(sys.argv[1])