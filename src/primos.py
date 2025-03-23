#!/usr/bin/python3
# Programa para encontrar y mostrar todos los números primos en un intervalo específico

# Definición del rango de números para buscar primos
lower = 1    # Límite inferior del rango
upper = 500  # Límite superior del rango

# Muestra un mensaje indicando el rango de búsqueda
print("Prime numbers between", lower, "and", upper, "are:")

# Itera a través de cada número en el rango especificado
for num in range(lower, upper + 1):
   # Verifica si el número es mayor que 1, ya que todos los números primos son mayores que 1
   # El número 1 no es primo por definición
   if num > 1:
       # Comprueba si el número es divisible por algún número entre 2 y (num-1)
       # Si es divisible por alguno, entonces no es primo
       for i in range(2, num):
           if (num % i) == 0:  # Si el residuo es 0, el número es divisible por i
               break  # Sale del bucle interno si encuentra un divisor
       else:
           # El bucle else se ejecuta si el bucle for completa todas las iteraciones sin encontrar un break
           # Esto significa que el número no es divisible por ningún número entre 2 y (num-1), por lo tanto es primo
           print(num)  # Imprime el número primo encontrado
