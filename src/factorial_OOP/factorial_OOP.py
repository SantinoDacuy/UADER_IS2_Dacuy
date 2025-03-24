#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* Cálculo de factorial usando Programación Orientada a Objetos            *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    """
    Clase para calcular factoriales en un rango específico
    """
    def __init__(self):
        """
        Constructor de la clase Factorial
        """
        pass

    def factorial_individual(self, num):
        """
        Calcula el factorial de un número individual
        
        Args:
            num (int): Número para calcular su factorial
        
        Returns:
            int: Factorial del número
        """
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min_val, max_val):
        """
        Calcula los factoriales en un rango específico
        
        Args:
            min_val (int): Valor mínimo del rango
            max_val (int): Valor máximo del rango
        """
        print(f"Calculando factoriales desde {min_val} hasta {max_val}")
        for num in range(min_val, max_val + 1):
            print(f"Factorial {num}! es {self.factorial_individual(num)}")

def main():
    """
    Función principal para manejar la entrada de argumentos
    """
    # Verificar argumentos
    if len(sys.argv) < 3:
        # Si no se proporcionan suficientes argumentos, solicitar entrada
        min_val = int(input("Ingrese el valor mínimo del rango: "))
        max_val = int(input("Ingrese el valor máximo del rango: "))
    else:
        # Tomar argumentos de la línea de comandos
        min_val = int(sys.argv[1])
        max_val = int(sys.argv[2])

    # Crear instancia de Factorial y ejecutar
    factorial_calc = Factorial()
    factorial_calc.run(min_val, max_val)

if __name__ == "__main__":
    main()