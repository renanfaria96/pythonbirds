class Pessoa: #criação de objetos
    olhos = 2 #como olhos sempre serão 2, não é necessário colocar no def init
    #cria o atributo defaut (atributo de classe). o valor é o mesmo para todos os objetos
    def __init__(self, *filhos, nome = None, idade = 25): #criando atributos de dados
        self.idade = idade
        self.nome = nome #campo existe mas sem valor atribuido
        self.filhos = list(filhos)

    def cumprimentar(self): #utilizando metodos (esta sempre atrelado a um objeto)
        return f'Olá, meu nome é {self.nome}.'

    @staticmethod #decorator. metodo estatico funciona como uma função atrelada a classe pessoa. independe do objeto.
    def metodo_estatico():
        return 42

    @classmethod #outro decorator. #para acessar dados da própria classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar() #super acessa os elementos da classe py de homem
        return f'{cumprimentar_da_classe} Aperto de mão'

class Mutante(Pessoa):
    olhos = 3 #sobrescrita de atributos de dados


if __name__ == '__main__':
    renan = Mutante(nome= 'Renan')
    silva = Homem(renan, nome ='Silva')
    print(Pessoa.cumprimentar(silva))
    print(id(silva))
    print(silva.cumprimentar())
    print(silva.nome)
    print(silva.idade)
    for filho in silva.filhos:
        print(filho.nome)
    silva.sobrenome = 'Faria'
    del silva.filhos
    silva.olhos = 1 #ele passa a fazer parte do __dict__ do objeto silva, alterado de 2 para 1
    del silva.olhos #apaga o atributo do objeto e não o da classe, então ele vai de 1 para 3
    print(silva.__dict__)
    print(renan.__dict__)
    #Pessoa.olhos = 3 #isso fará q a classe pessoa passe de 2 para 3. mas o silva continua com 1
    #print(Pessoa.nome) #não faz sentido fazer isso pq não especificou qual pessoa
    print(Pessoa.olhos) #isso faz sentido, pq toda pessoa tem 2 olhos. atributo de classe pode ser acessado pela classe
    print(silva.olhos)
    print(renan.olhos) #é possivel acessar o atributo de classe não só pela classe mas tbm pelos objetos
    print(id(Pessoa.olhos), id(renan.olhos), id(silva.olhos))
    print(Pessoa.metodo_estatico(), silva.metodo_estatico()) #se o atributo não for encontrado no objeto, o python procura na classe
    print(Pessoa.nome_e_atributos_de_classe(), silva.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renan, Pessoa))
    print(isinstance(renan, Homem))
    print(renan.olhos)
    print(renan.cumprimentar())
    print(silva.cumprimentar())