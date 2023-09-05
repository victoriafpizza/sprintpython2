# Importando bibliotecas
import random
import re


# Definindo a cotação dos pontos 
cotacao_pontos = {
    "material/Kg" : {
        "Papel" : 20,
        "Plástico" : 25,
        "Vidro" : 15,
        "Metal" : 10,
        "Eletrônicos" : 30
    },
}



# Definindo usuários
usuarios = {
    "ADM" : {
        "Pin" : "11111",
        "Identificação" : {
            "Email" : "admin@reuse.com",
            "Telefone" : "00 00000-0000"
        },
        "Dados" : {
            "reciclagem_kg" : {
                "Papel" : 0,
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            },
            "Pontos" : {
                "Papel" : 0, #cotação-pontos * reciclagem-kg
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            }
        },
    }, 

    "Emanuelle" : {
        "Pin" : "97973",
        "Dados" : {
            "reciclagem_kg" : {
                "Papel" : 0,
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            },
        },
    },

    "Victória" : {
        "Pin" : "97986",
        "Dados" : {
            "reciclagem_kg" : {
                "Papel" : 0,
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            },
        },
    }, 

    "Enzo" : {
        "Pin" : "10253",
        "Dados" : {
            "reciclagem_kg" : {
                "Papel" : 0,
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            },
        },
    },

    "Murilo" : {
        "Pin" : "54321",
        "Dados" : {
            "reciclagem_kg" : {
                "Papel" : 0,
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            },
        },
    },

    "Ricardo" : {
        "Pin" : "12345",
        "Dados" : {
            "reciclagem_kg" : {
                "Papel" : 0,
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            },
        },
    },

    "" : {
        "Pin" : "",
        "Dados" : {
            "reciclagem_kg" : {
                "Papel" : 0,
                "Plástico" : 0,
                "Vidro" : 0,
                "Metal" : 0,
                "Eletrônicos" : 0
            },
        },
    }
}

# Definindo funções que serão utilizadas no programa

# Gerando pins aleatórios para usuários novos
def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin

# Função para simular o dado (qtd de kg deposistados p/ utilizar na função(opcao_reciclar))
def sorteio_entrada_dados() :
    entrada_lixo = (float(random.randint(0,9)) for i in range(2))
    return entrada_lixo


# Função para reciclar
def opcao_reciclar() :
    print("Por Favor, escolha o material que deseja depositar:\n(1)\tPapel\n(2)\tPlástico\n(3)\tVidro\n(4)\tMetal\n(5)\tEletrônicos")
    escolha_reciclar = int(input())
    if escolha_reciclar == 1:
        print(f"Material escolhido:\tPapel\nPeso:\t{sorteio_entrada_dados}")

        # Confirmando a operação
        confirmar_op = True
        while confirmar_op:
            print("Confirmar operção\n(1)\tSim\n(2)\tNão")
            confirmar_op = int(input())
            if confirmar_op == 1:
                break
            elif confirmar_op == 2:
                continue


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
    print("Escolha uma opção:\n(1)\tEntrar\n(2)\tCadastrar-se")
    escolha_menu_inicial = int(input())

    if escolha_menu_inicial == 1 :
        print("Por favor insira seu PIN de 5 números.")
        pin = input()
        if pin in [dados["Pin"] for dados in usuarios.values()]:
            for usuario, dados in usuarios.items():
                if dados["Pin"] == pin:
                    print(f"Bem-vindo, {usuario}! Estamos felizes em receber de volta.")
                    break
        else:
            print("Não é cliente da reUse?! Escolha a opção de cadastro!\nLembre-se, para descartar o lixo não é preciso ser cadastrado no sistema! Você só precisa despejá-lo no outro lado da lixeira :)")
    elif escolha_menu_inicial == 2 :

        print("Por Favor, insira seu nome:")
        nome_usuario = input()
        if re.search("\d", nome_usuario):
            erro = "Nomes não podem conter números."
            raise ValueError
        # Fazendo um sorteio para gerar o PIN (com 5 dígitos)
        pin_aleatorio = gerar_pin_aleatorio()
        
        # Atualizando o dicionário de usuários com os novos dados gerados
        usuarios[nome_usuario] = {
            "Pin": pin_aleatorio
        }

        # Exibindo novo usuário e exibindo o PIN gerado
        print(f"Bem vindx {nome_usuario}!\nO seu PIN é: {pin_aleatorio}. Lembre-se, ele é único, guarde-o com carinho :)")
    else:
        if escolha_menu_inicial >= 3:
            print("Por favor, escolha uma opção válida") 

# Criando o menu secundário        
nav_menu_secundario = True
# Adicionando Loop no menu secundário
while nav_menu_secundario:
    print("Escolha uma opção:\n(1)\tReciclar\n(2)\tExtrato de pontos\n(3)\tCotação Atual de materiais\n(4)\tResgatar recompensas")
    escolha_menu_secundario = int(input())

    if escolha_menu_secundario == 1:
        print(opcao_reciclar)
    elif escolha_menu_secundario == 2 :
        print("Lerolero")
