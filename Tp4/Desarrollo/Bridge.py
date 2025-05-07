class TrenLaminador:
    def producir(self, largo):
        pass


class Tren5m(TrenLaminador):
    def producir(self, largo):
        print(f"Produciendo lámina de {largo} metros con Tren Laminador de 5m")


class Tren10m(TrenLaminador):
    def producir(self, largo):
        print(f"Produciendo lámina de {largo} metros con Tren Laminador de 10m")


class Lamina:
    def __init__(self, espesor, ancho, largo, tren):
        self.espesor = espesor
        self.ancho = ancho
        self.largo = largo
        self.tren = tren

    def producir(self):
        print(f"Lámina: {self.espesor}'' x {self.ancho}m x {self.largo}m")
        self.tren.producir(self.largo)


# MAIN
if __name__ == "__main__":
    lamina1 = Lamina(0.5, 1.5, 5, Tren5m())
    lamina2 = Lamina(0.5, 1.5, 10, Tren10m())

    lamina1.producir()
    lamina2.producir()
