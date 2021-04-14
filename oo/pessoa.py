class Pessoa:
    olhos = 2

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

    print(Pessoa.olhos)
    print(p.olhos)
    print(p2.olhos)
    p.olhos = 1
    print(id(Pessoa.olhos), id(p2.olhos))
    Pessoa.olhos = 3
    print(p.__dict__)
    print(p2.__dict__)
    print(p2.olhos)
    del p.olhos
    print(p.olhos)