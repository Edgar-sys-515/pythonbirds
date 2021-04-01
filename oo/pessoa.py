class Pessoa:
    olhos = 2  # atributo de classe == default
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

    emanoel.sobrenome = "Mendes"  # criando atributo dinamicamente
    print(emanoel.sobrenome)
    # print(edgar.sobrenome) vai dar erro de edgar nao possuir objeto sobrenome
    del emanoel.filho  # removendo atributo dinamicamente
    print(emanoel.__dict__)  # dict mostra todos os atributos
    print(edgar.__dict__)
    Pessoa.olhos = 5  # mudando o atributo da classe inteira
    print(Pessoa.olhos)  # atributo de classe
    print(edgar.olhos)  # atributo de classe
    emanoel.olhos = 1  # atributo de objeto
    print(emanoel.olhos)  # virou atributo de objeto
    print(id(emanoel.olhos), id(edgar.olhos), id(Pessoa.olhos))  # id ficou diferente em emanoel.olhos
    Pessoa.olhos = 5
