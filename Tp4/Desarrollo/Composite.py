class Componente:
    def mostrar(self, nivel=0):
        pass


class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("\t" * nivel + f"- Pieza: {self.nombre}")


class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("\t" * nivel + f"+ SubConjunto: {self.nombre}")
        for comp in self.componentes:
            comp.mostrar(nivel + 1)


# MAIN
if __name__ == "__main__":
    producto = SubConjunto("Producto Principal")

    for i in range(1, 4):
        subconj = SubConjunto(f"Subconjunto {i}")
        for j in range(1, 5):
            subconj.agregar(Pieza(f"Pieza {i}.{j}"))
        producto.agregar(subconj)

    # Agregado adicional
    extra = SubConjunto("Subconjunto Extra")
    for j in range(1, 5):
        extra.agregar(Pieza(f"Pieza Extra.{j}"))
    producto.agregar(extra)

    producto.mostrar()
