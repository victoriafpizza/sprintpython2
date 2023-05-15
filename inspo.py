import random 

sorteio = random.randint(1,5)

if sorteio == 1 : nomefunc = "astrogildo"
elif sorteio == 2 : nomefunc = "berisvaldo"
elif sorteio == 3 : nomefunc = "Gumercindo"
elif sorteio == 4 : nomefunc = "Pafuncia"
else : nomefunc = "tiburcio" 

print(f"Bem-vindo a Vinheria Agnelo. \n O funcionario {nomefunc} vai acompanha-la nessa compra.")

print("informe seu nome")
nome = input()
print("informe seu cep")
cep = input()
print("iforme seu ano de nascimento")
anonasc = int(input())

idade = 2023 - anonasc
if idade < 18 : 
    print(f"{nome} não é permitida a venda para menores de 18 anos")
else :
    print("continua aqui")

#variaveis para ajudar nos calculos 

subtotal = total = 0 
msgfinal = f"dados da compra: \n Atendido por {nomefunc}\n Cliente: {nome}\n Itens da Compra \t Valor \tQuantidade \tSubtotal\n"

continua = "sim"
while continua.lower == "sim" : 
    print("escolha um dos vinhos d lista \n (1) vinho suave tinto \t R$ 15.00 \n (2)vinho seco tinto \t R$ 25.00\n (3) vinho branco suave \t R$ 35.00 \n (4) vinho seco branco \t 30.00 \n (5) vinho sem alcool \t R$ 40.00 \n")

    print("deseja continuar a compra? (responda sim ou nao)")
    continua = input()

    subtotal = total = 0

msgfinal = f"Dados da compra: \n Atendido por:{nomefunc} \n itens da compra: \t valor: \t quantidade \t sutotal \t"

continua = "sim"

while continua.lower() == "sim":
    rint(f"esolha um dos vinhos da lista (1) vinho suave tinto \t R$ 15.00 \n (2)vinho seco tinto \t R$ 25.00\n (3) vinho branco suave \t R$ 35.00 \n (4) vinho seco branco \t 30.00 \n (5) vinho sem alcool \t R$ 40.00 \n")

vinho = int(input())
print("em qual qualtidade deseja adquirir este vinho?")
quantidade = int(input())

match vinho :
    case 1:
        subtotal = 15 * quantidade
        msgfinal +=f"vinho suave tinto \t R$ 15.00 \t {quantidade}\t R$ {subtotal:2f}\n"
    case 2:
        subtotal = 25 * quantidade
        msgfinal +=f"vinho seco tinto \t R$ 25.00 \t {quantidade}\t R$ {subtotal:2f}\n"
    case 3 :
        subtotal = 35 * quantidade
        msgfinal +=f"vinho suave branco \t R$ 35.00 \t {quantidade}\t R$ {subtotal:2f}\n"
    case 4 : 
        subtotal = 30 * quantidade
        msgfinal +=f"vinho seco branco \t R$ 35.00 \t {quantidade}\t R$ {subtotal:2f}\n"
    case 5 : 
        subtotal = 40 * quantidade
        msgfinal +=f"suco de uva \t R$ 40.00 \t {quantidade}\t R$ {subtotal:2f}\n"
    case _ :
        print(" por favor, escolha uma das opções da lista")

total += subtotal

print("deseja continuar comprando? \n (responda sim ou não)")
continua = input()

msgfinal = f"Dados dA COMPRA: \n"

print(msgfinal)

print(f"totla da compra: R$ {total:.2f}")

frete = total / 2

if total < 200 :
    print("valor do frete")
else : 
    print("FRETE GRATIS")

print(f"{nome}, foi um prazer atende-lo. Volte em breve!")