import os
from vet import*

vet_animals = Veterinaria (' Veterinaria')


# Menu principal
def menu():
    print("=== Cadastro de Animais ===")
    print("1. Cadastrar Pet")
    print("2. Listar Pets")
    print("3. Atualizar Pet")
    print("4. Sair")

# Pausar e limpar tela
def ls():
    os.system("pause")
    os.system("cls")

# Função para cadastrar um pet
def cadastrar_pet():
    nome = input("Nome do pet: ")
    especie = input("Espécie (Cachorro, Gato ou Peixe): ").capitalize()
    if especie not in ['Cachorro', 'Gato', 'Peixe']:
        print("Espécie inválida.")
        return

    vet_animals.cadastrar_pet(pets)
    peso = float(input("Peso: "))
    raca = input("Raça: ")
    idade = int(input("Idade: "))
    cor = input("Cor: ")
    nome_dono = input("Nome do dono: ")
    telefone_dono = input("Telefone do dono: ")

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
    print("Pet cadastrado com sucesso!")

def listar_pets():
    for chave, valor in vet_animals.listar().items():
        print(f'ID: {chave}\t Nome: {valor.getNome()}')