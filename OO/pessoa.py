class Pessoa: #criação de objetos
    def __init__(self, *filhos, nome = None, idade = 25): #criando atributos de dados
        self.idade = idade
        self.nome = nome #campo existe mas sem valor atribuido
        self.filhos = list(filhos)

    def cumprimentar(self): #utilizando metodos (esta sempre atrelado a um objeto)
        return f'Olá, {id(self)}.'


if __name__ == '__main__':
    renan = Pessoa(nome= 'Renan')
    silva = Pessoa(renan, nome ='Silva')
    print(Pessoa.cumprimentar(silva))
    print(id(silva))
    print(silva.cumprimentar())
    print(silva.nome)
    print(silva.idade)
    for filho in silva.filhos:
        print(filho.nome)
    silva.sobrenome = 'Faria'
    del silva.filhos
    print(silva.__dict__)
    print(renan.__dict__)
