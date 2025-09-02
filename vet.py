class Animal:
    def __init__(self, nome, peso, especie, idade, cor, nome_dono, telefone_dono):
        self.__nome = nome
        self.__peso = peso
        self.__especie = especie
        self.__idade = idade
        self.__cor = cor
        self.__nome_dono = nome_dono
        self.__telefone_dono = telefone_dono
        self.__armazenamento = {}
        self.__id = 0

    def cadastrar_pet():
        # Criando o dicionário do pet
        pet = {
            "nome": nome,
            "especie": especie,
            "peso": peso,
            "raca": raca,
            "idade": idade,
            "cor": cor,
            "nome_dono": nome_dono,
            "telefone_dono": telefone_dono
        }

        pets.append(pet)
        
        self.__id += 1
        self.__armazenamento[self.__id] = pet

#template cachorro
class Cachorro(Animal):
    def __init__(self, raca):
        self.__raca = raca

#template gato
class Gato(Animal): 
    def __init__(self, raca):
        self.__raca = raca

#template peixe
class Peixe(Animal):
    def __init__(self):
