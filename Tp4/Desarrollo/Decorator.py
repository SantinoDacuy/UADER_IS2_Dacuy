class Numero:
    def imprimir(self):
        pass


class NumeroBase(Numero):
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        return self.valor


class SumaDos(Numero):
    def __init__(self, componente):
        self.componente = componente

    def imprimir(self):
        return self.componente.imprimir() + 2


class MultiplicaDos(Numero):
    def __init__(self, componente):
        self.componente = componente

    def imprimir(self):
        return self.componente.imprimir() * 2


class DivideTres(Numero):
    def __init__(self, componente):
        self.componente = componente

    def imprimir(self):
        return self.componente.imprimir() / 3


# MAIN
if __name__ == "__main__":
    numero = NumeroBase(9)
    print("Valor base:", numero.imprimir())

    decorado = DivideTres(MultiplicaDos(SumaDos(numero)))
    print("Decorado ( +2 → *2 → /3 ):", decorado.imprimir())
