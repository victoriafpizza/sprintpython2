# Importando bibliotecas
import random
import re

# Definindo usuários
usuarios = {
    "ADM" : {
        "Pin" : "11111"
    }, 
    "Emanuelle" : {
        "Pin" : "97973"
    },
    "Victória" : {
        "Pin" : "97986"
    }, 
    "Enzo" : {
        "Pin" : "10253"
    },
    "Murilo" : {
        "Pin" : "54321"
    },
    "Ricardo" : {
        "Pin" : "12345"
    },
    "" : {
        "Pin" : ""
    }
}

# Definindo funções que serão utilizadas no programa

# Gerando pins aleatórios para usuários novos
def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin


######################
# Programa principal #
######################

# Exibindo o menu inicial primário, em formato de loop

nav_menu_inicial = True

while nav_menu_inicial: 
    # Desejando boas vindas ao usuário
    print("*************************")
    print("****Bem Vindo a reUse****")
    print("*************************")
    # Menu inicial
    print("Escolha uma opção:\n(1) LogIn\n(2) SignIn")
    escolha_menu_inicial = int(input())

    if escolha_menu_inicial == 1 :
        print("Por favor insira seu PIN de 5 números.")
        pin = input()
        if pin in usuarios.values():
            print(f"Olá {usuarios}")
            break
        else:
            print("Não é cliente da reUse?! Escolha a opção de cadastro!\nLembre-se, para descartar o lixo não é preciso ser cadastrado no sistema! Você só precisa despejá-lo no outro lado da lixeira :)")
            nav_menu_inicial = True
    elif escolha_menu_inicial == 2 :

        print("Por Favor, insira seu nome:")
        nome_usuario = input()
        if re.search("\d",nome_usuario) :
            erro = "Nomes não podem conter números."
            raise ValueError
        # Fazendo um sorteio p\ gerar o pin (com 5 num)
        pin_aleatorio = gerar_pin_aleatorio()
        
        # Atualizando o dicionário usuários com os novos dados gerados
        usuarios[nome_usuario] = {
            "Pin": pin_aleatorio
        }

        # Exibindo novo usuário e exibindo o pin gerado
        print(f"Bem vindx {nome_usuario}!\n o seu pin será: {pin_aleatorio}. Lembre-se, ele é unico, guarde ele com carinho :)")
    else : 
        if escolha_menu_inicial >= 3 :
            print("Por favor, escolha uma opção válida")

    