class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco

        else:
            print("não é permitido valor negativo!")

produto1 = Produto("prego", 1.5, 200)

novopreco = float(input("digite o novo preço do produto: "))
produto1.set_preco(novopreco)

print(f"preço do {produto1.get_nome()}: {produto1.get_preco()}")
    