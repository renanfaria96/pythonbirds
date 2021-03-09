class Pessoa: #criação de objetos
    def __init__(self, nome = None, idade = 25): #criando atributos de dados
        self.idade = idade
        self.nome = nome #campo existe mas sem valor atribuido

    def cumprimentar(self): #utilizando metodos (esta sempre atrelado a um objeto)
        return f'Olá, {id(self)}.'


if __name__ == '__main__':
    p = Pessoa('Silva')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renan' #alterar o valor do atributo
    print(p.nome)
    print(p.idade)
