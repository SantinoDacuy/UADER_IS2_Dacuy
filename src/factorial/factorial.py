#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o un rango de números                 *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    """
    Calcula el factorial de un número dado
    Args:
        num: número entero para calcular su factorial
    Returns:
        El factorial del número o 0 si es negativo
    """
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
    """
    Procesa la entrada del usuario y calcula factorial(es)
    Args:
        entrada: string que puede ser un número o un rango (ej. 4-8, -10, 5-)
    """
    # Verificar si es un rango (contiene guion)
    if "-" in entrada:
        partes = entrada.split("-")
        # Caso: -hasta (ej. -10)
        if partes[0] == "":
            fin = int(partes[1])
            inicio = 1
            print(f"Calculando factoriales desde {inicio} hasta {fin}")
            for num in range(inicio, fin + 1):
                print(f"Factorial {num}! es {factorial(num)}")
        # Caso: desde- (ej. 5-)
        elif partes[1] == "":
            inicio = int(partes[0])
            fin = 60
            print(f"Calculando factoriales desde {inicio} hasta {fin}")
            for num in range(inicio, fin + 1):
                print(f"Factorial {num}! es {factorial(num)}")
        # Caso: desde-hasta (ej. 4-8)
        else:
            inicio = int(partes[0])
            fin = int(partes[1])
            print(f"Calculando factoriales desde {inicio} hasta {fin}")
            for num in range(inicio, fin + 1):
                print(f"Factorial {num}! es {factorial(num)}")
    else:
        # Es un solo número
        num = int(entrada)
        print(f"Factorial {num}! es {factorial(num)}")

# Verificar si se proporcionó un argumento
if len(sys.argv) <= 1:
    # Si no hay argumento, solicitar al usuario
    entrada = input("Ingrese un número o rango (ej. 4-8, -10, 5-) para calcular factorial(es): ")
    procesar_entrada(entrada)
else:
    # Si hay argumento, usarlo
    procesar_entrada(sys.argv[1])