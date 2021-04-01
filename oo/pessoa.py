class Pessoa:
    def __init__(self, *filho, nome=None, idade=39):
        self.filho = list(filho)
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return "Olá"


if __name__ == '__main__':
    edgar = Pessoa(nome="Edgar")
    emanoel = Pessoa(edgar, nome="Emanoel")

    # print(Pessoa.cumprimentar(p))
    # print(edgar.cumprimentar())

    # Edgar = Pessoa()
    # print(Pessoa.cumprimentar(Edgar))
    # print(Edgar.cumprimentar())
    # print(Edgar.nome)
    # p.nome = "EDGAR"
    # print(Edgar.nome)
    # print(Edgar.idade)

    print(edgar.nome)
    print(emanoel.nome)

    for filhos in emanoel.filho:
        print(filhos.nome)


