import random

# Definindo usuários
usuarios = {
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

# Criando aa função de validação de usuário
def validacao_usuario() :
    while True:
        print("Por favor insira seu PIN.")
        pin = input()  # Lê o PIN como string

        if pin in usuarios.values():
            for usuario, dados in usuarios.items():
                if dados["Pin"] == pin:
                    print(f"Bem-vindo, {usuario}!")
                    break
        else:
            print("Não é cliente da reUse?! Escolha a opção de cadastro!\nLembre-se, para descartar o lixo não é preciso ser cadastrado no sistema! Você só precisa despejá-lo no outro lado da lixeira :)")
            continue  # Volta ao início do loop para tentar novamente

def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin


def criar_usuario():
    print("Seja bem Vindo!\nPor Favor, insira seu nome:")
    nome_usuario = str(input())
    print(f"Ok ")
    # Fazer um sorteio p\ gerar o pin (com 5 num)
    pin_aleatorio = gerar_pin_aleatorio()
    
    print(f"Bem vindx {nome_usuario}!\n o seu pin será: {pin_aleatorio}, guarde ele com carinho :)")

# Desejando boas vindas ao usuário
print("*************************")
print("****Bem Vindo a reUse****")
print("*************************")

# Exibindo o menu inicial


print("Escolha uma opção:\n(1) Login\n(2) SignIn")
escolha_menu_inicial = int(input())

if escolha_menu_inicial == 1 :
    print(validacao_usuario)
else : 
    print(criar_usuario)
