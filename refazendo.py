   
   # Despedaçando para completar no pycharm
   
     
   
    # Menu inicial
    print("Escolha uma opção:\n(1)\tEntrar\n(2)\tCadastrar-se")

    escolha_menu_inicial = int(input())

    if escolha_menu_inicial == 1:
        pasta = 'D:\sprint_python3\users'
        # Validação login
        print("Por favor insira seu PIN de 5 números.")
        pin = input()
        if pin in os.listdir(pasta):
            nav_menu_inicial = False
        else:
            print(
                "Não é cliente da reUse?! Escolha a opção de cadastro!\n"
                "Lembre-se, para descartar o lixo não é preciso ser cadastrado no sistema! "
                "Você só precisa despejá-lo no outro lado da lixeira :)")
            nav_menu_inicial = True
    elif escolha_menu_inicial == 2:
        # Função de cadastro
    else:
        if escolha_menu_inicial >= 3:
            print("Por favor, escolha uma opção válida")
        nav_menu_inicial == True