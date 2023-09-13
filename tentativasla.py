# n deu certo o cadstro criou 7374873294 pastas


# Importando módulos
import os #módulo para identificar os arquivos na pasta
import random #módulo de serteio para gerar novos PINS e etc
import re #módulo para confimar a entrada de email/celular corretos


######################
# Funções principais #
######################


# Função gerando PIN aleatório para o cadastro
def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin

# Função para validar o formato do email usando regex
def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(padrao_email, email) is not None

# Função para validar o formato do número de telefone celular usando regex
def validar_numero_celular(numero):
    padrao_celular = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    return re.match(padrao_celular, numero) is not None

# Função de cadastro
def cadastro():
    # Declarando var com a função do PIN
    pin_gerado = gerar_pin_aleatorio()

    # Definindo o caminho e nome do arquivo que será gerado
    nome_arquivo = f'D:/sprint_python3/users/{pin_gerado}.txt'

    try:
        with open(nome_arquivo, 'x', encoding='utf-8') as arquivo:
            print("Digite seu nome:")
            nome_user = input()
            arquivo.write(f"Nome: {nome_user}\n")

        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            print("Digite seu e-mail:")
            email_user = input()
            if not validar_email(email_user):  # Defina validar_email() corretamente
                print("Email inválido. Por favor, insira um email válido.")
                return
            arquivo.write(f"Email: {email_user}\n")

        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            print("Digite seu telefone celular:")
            celular_user = input()
            if not validar_numero_celular(celular_user):
                print("Número de telefone celular inválido. Por favor, insira um número válido no formato (XX) 9XXXX-XXXX.")
                return
            arquivo.write(f"Telefone celular: {celular_user}\n")

        print("Cadastro concluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



######################
# Programa principal #
######################

# Fazendo menu principal

nav_menu_inicial = True

while nav_menu_inicial is True:
    # Desejando boas vindas ao usuário
    print("*************************")
    print("*** Bem Vindo a reUse ***")
    print("*************************")

    cadastro()