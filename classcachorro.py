class Cachorro:
    def _init_(self, nome, raça, comida):
        self.nome = nome
        self.raça = raça
        self.comida = comida
        self.feliz = False
        self.acordado = False
        self.energia = 100

    def acordar (self):
        self.acordado = True
        print(f"{self.nome} está acordado!") 

    def dormir (self):
        self.acordado = False
        print(f"{self.nome} está dormindo!") 

    def comer (self):
        if self.acordado:
            self.comida -= 1
            print(f"{self.nome}comeu!") 
        else:
            print(f"{self.nome} está dormindo e não pode comer!") 

        
    def latir (self):
        if self.acordado:
            print(f"{self.nome}está latindo: AU AU AU")
        else:
            print(f"{self.nome}está dormindo e não está latindo") 

    def brincar (self):
        if self.acordado:
            self.feliz = True 
            self.energia -= 20
            print(f"{self.nome}está brincando e está feliz")
            self.energia <= 0
            print(f"{self.nome}está sem energia e não pode brincar")
        else:
            print(f"{self.nome} está dormindo e não pode brincar!") 

            self.energia <= 0
            print(f"{self.nome}está sem energia e não pode brincar")

    def energia (self):
        self.dormir
        print(f"{self.nome} agora está com energia depois do seu soninho")

cachorro1 = Cachorro("mel", "pastor alemão", 6)
cachorro1.brincar()
cachorro1.comer()
cachorro1.acordar()
cachorro1.dormir()
print(cachorro1.energia)