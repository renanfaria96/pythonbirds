class Pessoa: #criação de objetos
    def cumprimentar(self): #utilizando metodos (esta sempre atrelado a um objeto)
        return f'Olá, {id(self)}.'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
