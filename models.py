class Animal:
    def __init__(self, nome, brinco, raca, idade):
        self.nome = nome
        self.brinco = brinco
        self.raca = raca
        self.idade = idade


class Pesagem:
    def __init__(self, animal_id, peso, data):
        self.animal_id = animal_id
        self.peso = peso
        self.data = data