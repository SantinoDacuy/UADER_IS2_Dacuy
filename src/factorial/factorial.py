#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
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

def process_range(range_str):
    # Procesar cadena de rango (por ejemplo "4-8")
    if "-" in range_str:
        parts = range_str.split("-")
        if len(parts) == 2:
            try:
                min_val = int(parts[0])
                max_val = int(parts[1])
                return min_val, max_val
            except ValueError:
                print("Formato de rango inválido. Usando valor predeterminado.")
    
    # Si no es un rango válido, convertir a un solo número
    try:
        num = int(range_str)
        return num, num
    except ValueError:
        print("Valor inválido. Usando valor predeterminado.")
        return 1, 1

# Verificar si se proporcionó un argumento
if len(sys.argv) <= 1:
    # Si no hay argumento, solicitar al usuario
    range_input = input("Ingrese un número o rango (ej. 4-8) para calcular factorial(es): ")
    min_num, max_num = process_range(range_input)
else:
    # Si hay argumento, usarlo
    min_num, max_num = process_range(sys.argv[1])

# Calcular y mostrar factoriales para el rango especificado
for num in range(min_num, max_num + 1):
    print(f"Factorial {num}! es {factorial(num)}")