class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':

    p = Pessoa(nome='filho de bruno')
    p2 = Pessoa(p, nome='bruno torres')

    for f in p2.filhos:
        print(f.__dict__)