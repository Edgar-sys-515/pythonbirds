class Pessoa:
    olhos = 2  # atributo de classe == default

    def __init__(self, *filho, nome=None, idade=39):
        self.filho = list(filho)
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}"


    @staticmethod
    def metodo_estatico():
        return 23 + 44

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f"{cls} Olhos {cls.olhos}"


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()  # super () vai se referir a classe pai
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    # edgar = Pessoa(nome="Edgar")
    edgar = Mutante(nome="Edgar")
    # emanoel = Pessoa(edgar, nome="Emanoel")
    emanoel = Homem(nome="Emanoel")
    print(Pessoa.cumprimentar(edgar))
    print(edgar.cumprimentar())

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
    # Pessoa.olhos = 5  # mudando o atributo da classe inteira
    print(Pessoa.olhos)  # atributo de classe
    print(edgar.olhos)  # atributo de classe
    emanoel.olhos = 1  # atributo de objeto
    print(emanoel.olhos)  # virou atributo de objeto
    print(id(emanoel.olhos), id(edgar.olhos), id(Pessoa.olhos))  # id ficou diferente em emanoel.olhos
    # Pessoa.olhos = 5
    print(Pessoa.metodo_estatico(), edgar.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())
    print(edgar.nome_e_atributos_de_classe())
    print(emanoel.nome_e_atributos_de_classe(), ",", emanoel.olhos)
    pessoa = Pessoa("Anonimo", nome="Sem")
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(edgar, Homem))
    print(isinstance(edgar, Pessoa))
    print(edgar.olhos)
    print(emanoel.olhos)
    print(edgar.cumprimentar())
    print(emanoel.cumprimentar())

