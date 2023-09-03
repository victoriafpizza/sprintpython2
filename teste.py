import random


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







    