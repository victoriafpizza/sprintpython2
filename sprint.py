
print(f"Bem-vindo a reUse. \n  Por favor insira seu PIN .")
pin = int(input())

print("Insira seu nome, para um atendimento personalizado")
nome = input()

if pin == 123456 :
    print(f"Bem vindo {nome}, por favor selecione qual material você gostaria de descartar\n [1] Papel \n [2] Metal \n [3] Plástico \n [4] Vidro")
else :
    print("Não é cliente da reUse?! Se cadastre através do QR CODE abaixo!")

print("quantos quilos voce reciclou?")
kgsReciclados = int(input())

continua = "sim"
while continua.lower == "sim" : 
    print("Por favor selecione qual material você gostaria de descartar\n [1] Papel \n [2] Metal \n [3] Plástico \n [4] Vidro")

    print("deseja continuar reciclando? (responda sim ou nao)")
    continua = input()

    subtotal = total = 0

#variaveis para ajudar no calculo dos premios

 match reciclagem :
     case 1:
        pontuacao = 10 * kgsReciclados
         msgfinal +=f"voce reciclou {kgsReciclados}, \n sua pontuação para premios é: {pontuacao}"
     case 2:
         pontuacao = 20 * kgsReciclados
         msgfinal +=f"voce reciclou {kgsReciclados}, \n sua pontuação para premios é {pontuacao}"
     case 3 :
         pontuacao = 30 * kgsReciclados
         msgfinal +=f"voce reciclou {kgsReciclados}, \n sua pontuação para premios é {pontuacao}"
     case 4 : 
         pontuacao = 40 * kgsReciclados
         msgfinal +=f"voce reciclou {kgsReciclados}, \n sua pontuação para premios é {pontuacao}"
     case 5 : 
         pontuacao = 50 * kgsReciclados
         msgfinal +=f"voce reciclou {kgsReciclados}, \n sua pontuação para premios é {pontuacao}"
     case _ :       
         print(" por favor insira quantos quilos voce reciclou!")

print(f"seu total de quilos reciclados é {kgsReciclados} o seu total de pontos é {pontuacao}")

if pontuacao > 100 :
    print("voce tem direito a ...")
elif pontuacao > 200 :
    print("voce tem direito a ...")
elif pontuacao > 300 :
    print("voce tem direito a ...")
elif pontuacao > 400 :
    print("voce tem direito a ...")
elif pontuacao > 500 :
    print("voce tem direito a ...")
else :
    print("verifique seus dados, e continue reciclando com a Cyber Wave!")

print("deseja continuar comprando? \n (responda sim ou não)")
continua = input()

print(f"{nome}, foi um prazer atende-lo. Volte em breve!")

msgfinal = f"Sua pontuação final é {pontuacao}, volte em breve {nome}"

print(msgfinal)