from app_menu import *
from vet import*


#menu
menu()

#escolha do menu
opcao=int(input("Digite sua escolha \n -->"))

#opcao de cadastro
while opcao != 4:
    if opcao == 1:
        ls()
        print("Cadastre seu Pet.")
        cadastrar_pet()
        ls()
    
    elif opcao == 2:
        ls()
        print('Lista de Pets cadastrados.')

    elif opcao == 3:
        ls()
        print('Atualização de Pets cadastrados.')

    #opcao de saida
    elif opcao == 4:
        print('Até mais, volte sempre!')
        ls()

    else:
        print("Opção inválida!")
        ls()

    menu()


