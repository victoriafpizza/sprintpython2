import random
import re
import os

# Pasta onde os arquivos dos usuários serão armazenados
PASTA_USUARIOS = 'usuarios/'

# Função para validar o formato do email usando regex
def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(padrao_email, email) is not None

# Função para validar o formato do número de telefone celular usando regex
def validar_numero_celular(numero):
    padrao_celular = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    return re.match(padrao_celular, numero) is not None

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Informe seu nome: ")
    email = input("Informe seu email: ")
    telefone = input("Informe seu número de telefone celular (no formato (XX) 9XXXX-XXXX): ")

    if not validar_email(email):
        print("Email inválido. Por favor, insira um email válido.")
        return
    if not validar_numero_celular(telefone):
        print("Número de telefone celular inválido. Por favor, insira um número válido no formato (XX) 9XXXX-XXXX.")
        return

    pin = ''.join(random.choice('0123456789') for _ in range(5))

    usuario = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'pin': pin,
        'reciclagem_kg': 0,
        'pontos': 0,
    }

    # Crie um arquivo de texto com base no PIN do usuário
    arquivo_usuario = os.path.join(PASTA_USUARIOS, f"{pin}.txt")
    with open(arquivo_usuario, 'w') as arquivo:
        arquivo.write(f"Nome: {usuario['nome']}\n")
        arquivo.write(f"Email: {usuario['email']}\n")
        arquivo.write(f"Telefone: {usuario['telefone']}\n")
        arquivo.write(f"PIN: {usuario['pin']}\n")
        arquivo.write(f"Reciclagem (kg): {usuario['reciclagem_kg']}\n")
        arquivo.write(f"Pontos: {usuario['pontos']}\n")

    print(f"Seu PIN de acesso é: {pin}")

# Função para carregar os dados de um usuário a partir de um arquivo de texto
def carregar_usuario(pin):
    arquivo_usuario = os.path.join(PASTA_USUARIOS, f"{pin}.txt")
    if os.path.exists(arquivo_usuario):
        with open(arquivo_usuario, 'r') as arquivo:
            linhas = arquivo.readlines()
            dados_usuario = {}
            for linha in linhas:
                campo, valor = linha.strip().split(': ')
                dados_usuario[campo.lower()] = valor
            return dados_usuario
    else:
        return None

# Implemente as demais funções e menus conforme descrito no documento original

# Função principal
def main():
    # Certifique-se de criar a pasta de usuários se ela não existir
    if not os.path.exists(PASTA_USUARIOS):
        os.makedirs(PASTA_USUARIOS)

    print("Bem-vindo ao programa de reciclagem!")
    while True:
        print("Menu Principal:")
        print("1 - Entrar")
        print("2 - Cadastrar-se")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            pin = input("Informe seu PIN: ")
            usuario = carregar_usuario(pin)
            if usuario:
                # Implemente a funcionalidade de login aqui
                pass
            else:
                print("Usuário não encontrado.")
        elif escolha == '2':
            cadastrar_usuario()
        elif escolha == '3':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
