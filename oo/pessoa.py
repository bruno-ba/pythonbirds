class Pessoa:
    def __init__(self, nome=None):
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('bruno torres')
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Bruno'
    print(p.nome)