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
            print("Não é cliente da reUse?! Se cadastre através do QR CODE abaixo!\nLembre-se, para descartar o lixo não é preciso ser cadastrado no sistema! Você só precisa despejá-lo no outro lado da lixeira :)")
            continue  # Volta ao início do loop para tentar novamente










#Parei aq 
# Armazenando a opção de continuar
continua = "sim"

# Exibindo as opções e seus conteúdos
while continua.lower() == "sim":
    # exibindo opções
    print(f"Bem vindo {nome}, O que você deseja consultar?\n [1] \t extrato de pontos \n [2] \t Saques antigos \n [3] \t Cotação de material")

    opcao = int(input()) 

    match opcao :
        case 1:
            print(f"Parabéns {nome}, você ja aculmulou XXXX pontos com a reciclagem\nExtrato:\ndd/mm/aaaa\tXXxp\ndd/mm/aaaa\tXXxp\ndd/mm/aaaa\tXXxp")
        case 2:
            print(f"{nome}, você já ganhou R$XXXX, apenas reciclando!\nExtrato:\ndd/mm/aaaa\tR$XX\ndd/mm/aaaa\tR$XX\ndd/mm/aaaa\tR$XX\nContinue reciclando para ganhar mais e assim resgatar mais cupons e prêmios")
        case 3 :
            print(f"{nome}, Até hoje você já reciclou xxxxkg de lixo\nSendo eles:\nxxkg\tde metal\nxxkg\tde papel\nxxkg\tde plástico\nxxkg\tde vidro\nContinue progredindo, o nosso planeta agradeçe!")
        case _ :       
            print("Por favor, digite uma das opções!")

    # Continuando ou não
    print("Deseja fazer outra operação?\nResponda Sim ou não.")
    continua = input()

# mensagem final 
print("Obrigado por preservar o meio-ambiente conosco, volte sempre!")
