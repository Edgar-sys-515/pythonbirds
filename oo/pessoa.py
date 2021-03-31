class Pessoa:
    def __init__(self, nome=None, idade=39):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return "Olá"


if __name__ == '__main__':
    p = Pessoa("Ed")
    # print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())

    Edgar = Pessoa()
    # print(Pessoa.cumprimentar(Edgar))
    print(Edgar.cumprimentar())
    # print(Edgar.nome)
    # p.nome = "EDGAR"
    print(p.nome)
    print(p.idade)
