class Letra:
    def __init__(self, caracter):
        self.caracter = caracter

    def mostrar(self, posicion):
        print(f"Letra '{self.caracter}' en posición {posicion}")


class FlyweightFactory:
    def __init__(self):
        self._letras = {}

    def obtener_letra(self, caracter):
        if caracter not in self._letras:
            self._letras[caracter] = Letra(caracter)
        return self._letras[caracter]


# MAIN
if __name__ == "__main__":
    texto = "hola hola"
    factory = FlyweightFactory()

    for idx, c in enumerate(texto):
        letra = factory.obtener_letra(c)
        letra.mostrar(idx)
