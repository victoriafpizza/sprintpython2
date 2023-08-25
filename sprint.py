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
                    print("Bem-vindo, " + usuario + "!")
                    break
        else:
            print("Não é cliente da reUse?! Escolha a opção de cadastro!\nLembre-se, para descartar o lixo não é preciso ser cadastrado no sistema! Você só precisa despejá-lo no outro lado da lixeira :)")
            continue  # Volta ao início do loop para tentar novamente

