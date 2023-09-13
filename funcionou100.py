import random
import re

# Dicionário com a cotação de materiais
cotacao_pontos = {
    "material/Kg" : {
        "Papel" : 20,
        "Plástico" : 25,
        "Vidro" : 15,
        "Metal" : 10,
        "Eletrônicos" : 30
    },
}

# Função gerando pin aleatório
def gerar_pin_aleatorio():
    pin = ''.join(str(random.randint(0, 9)) for _ in range(5))
    return pin

# Funções para validar email e celular
def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(padrao_email, email) is not None
def validar_numero_celular(numero):
    padrao_celular = r'^\d{2}9\d{8}$'
    return re.match(padrao_celular, numero) is not None

# Função de cadastro
# Função de cadastro
def cadastro():
    try:
        while True:
            print("****************")
            print("Área de cadastro")
            print("****************")

            pin = gerar_pin_aleatorio()
            pin_arquivo = f'd:/sprint_python3/users/{pin}.txt'
            with open(pin_arquivo, 'w', encoding='utf-8') as arquivo:
                print("Digite o seu nome:")
                nome = input()
                arquivo.write(f"Nome: {nome}\n")

                print("Digite o seu email:")
                email = input()
                if not validar_email(email):
                    print("Email inválido. "
                          "Por favor, insira um email válido.")
                    continue  # Volta ao início do loop interno

                arquivo.write(f"Senha: {email}\n")

                print("Digite o seu celular:")
                celular = input()
                if not validar_numero_celular(celular):
                    print(
                        "Número de telefone celular inválido. "
                        "Por favor, insira um número válido no "
                        "formato XX9XXXXXXXX.")
                    continue  # Volta ao início do loop interno

                arquivo.write(f"Celular: {celular}\n")
            arquivo.close()

            # Confirmando dados
            while True:
                validar_arquivo = open(f'd:/sprint_python3/users/{pin}.txt', 'r', encoding='utf-8')

                print(f"{validar_arquivo.read()}\nConfirma informações? (S/N)")
                resposta = input().strip().lower()
                if resposta == 's':
                    break  # Sai do loop interno
                else:
                    print("Redirecionando para refazer o cadastro")
                    break  # Sai do loop interno

            print("Cadastro concluído com sucesso!")
            break  # Sai do loop externo

    except FileNotFoundError:
        print("Caminho e/ou arquivo inexistente")


# Programa
while True:
    cadastro()
    resposta = input("Deseja cadastrar outro usuário? (S/N): ").strip().lower()
    if resposta != 's':
        break