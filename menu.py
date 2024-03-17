import os

class Menu:

    def menu(self):
        print ("·.★·.·´¯`·.·★ 🅻🅾🅹🅸🅽🅷🅰 🅱🅰🅲🅰🅽🅸🅽🅷🅰 ★·.·´¯`·.·★.·")
        print ("________________________________________________________")
        opcao = (int(input("1- Vitrine | 2- Cadastrar produtos | 3- remover produtos | 4- sair")))
        if opcao == 1:
            print('cadastrar')
            # mostra todos os produtos DISPONIVEIS
        elif opcao == 2:
            print ("vamos cadastrar seus produtos")
            # cadastrar()
        elif opcao == 3:
            print ("Vamos descadastrar seus produtos")
            # desativar()
        elif opcao == 4:
            print ("saindo")
            os.system('clear') or None
        else :
            print ("Opcao invalida")
            os.system('clear') or None
