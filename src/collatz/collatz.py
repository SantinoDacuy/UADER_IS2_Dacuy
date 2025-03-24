#!/usr/bin/python
import matplotlib.pyplot as plt

def collatz_iteraciones(n):
    """
    Calcula el número de iteraciones para que una secuencia de Collatz converja
    
    Args:
        n (int): Número inicial de la secuencia
    
    Returns:
        int: Número de iteraciones hasta converger
    """
    iteraciones = 0
    numero_original = n
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    
    return iteraciones

def graficar_collatz():
    """
    Genera un gráfico de la secuencia de Collatz para números entre 1 y 10000
    """
    numeros_inicio = []
    iteraciones_lista = []
    
    for numero in range(1, 10001):
        iteraciones = collatz_iteraciones(numero)
        numeros_inicio.append(numero)
        iteraciones_lista.append(iteraciones)
    
    plt.figure(figsize=(15, 8))
    plt.scatter(iteraciones_lista, numeros_inicio, alpha=0.5, s=10)
    plt.title('Iteraciones de la Conjetura de Collatz (1-10000)')
    plt.xlabel('Número de Iteraciones')
    plt.ylabel('Número de Inicio')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    """
    Función principal para ejecutar el programa
    """
    graficar_collatz()

if __name__ == "__main__":
    main()