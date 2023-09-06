IBM challenge
Sprint II - Computational Thinking with Python

Decidimos que as funcionalidades implementadas girariam em torno da ODS (Objetivos de Desenvolvimento Sustentável) 11.6 Até 2030, reduzir o impacto ambiental negativo per capita das cidades, inclusive prestando especial atenção à qualidade do ar, gestão de resíduos municipais e outros. Nesse sentido daremos um foco maior a gestão de residuos municipais, com programas centralizados em reciclagem.
Atravez da produção de lixeiras inteligentes juntamente à um software que registra a quantidade total de componentes reciclados pelo indivíduo, e a partir disso gera recompensas de empresas parceiras. Assim como os “elos” de reciclagem que evoluem e vão formando uma reputação, e fazem os usuários terem mais interesse em contribuir
__________________________________________________________________________________________________________________________________________________

Notas sobre o programa (Por emma, para o grupo, vai ser totalmente descartado antes de ser entregue)

* Padrões principais
> Após cada operação, o usuário deve confirmar antes de finaliza-la (E essa operação vai estar armazenada em uma função)

1 - Estabelecendo os dados
    Todas as informações que vamos precisar para que o programa consiga funcionar 
    
    1.1 Usuário - O nome do usuário, informado ao sistenma na hora do cadastro.
    1.2 Pin - Principal fonte de identificação e com 5 números armazenados como string, único para cada usuário - pode ser pré definindo pelo usuario admnistrador ou no protocolo normal - no caso vai ser gerado aleatóriamente via sorteio (import random)
    1.3 Email - Informado ao sistema atraves do cadastro, utilizado para a comunicação com o cliente (*Vamos armazenar o dado no programa mas não necessáriamente vamos utilizar praticamente ele - até porque não entramos ainda no tópico na matéria*)
    1.4 Número de telefone celular - informado ao sistema na hora do cadastro, também utilizado para a comunicação com o cliente. 
    NOTA. Vale deixar claro que a implementação de ambos email e celular no cadastro fomenta a oportunidade perfeita para utilizar o regex
    1.5 Dados - Um nested dictionary que vai conter as prinicipais funções do programa, até porque lá vai ter a maior quantidade de informações possíveis sobre o usuário, sendo elas:
        1.5.1 {reciclagem_kg} Kg de reciclagem - A quantidade total de kg reciclados pelo usuário ate o momento de consulta.
        1.5.2 {pontos} Pontos - A quantidade total de pontos do usuário até a hora da consulta, eles são definidos através dos KG reciclados multiplicados a cotação de pontos - que mais pra frente vai ser descrito corretamente.
    1.6 Cotação de pontos - Em formato de dicionário, vai armazenar a quantidade de pontos equivalentes de cada materia pela cotação material/kg (no caso em referência a ao equilavlente de pontos a cada kg despejado). A cotação de pontos pode ser exibida ao usuário.


2 - Estabelecendo as principais funções
    Em forma de menu, separadoos em camadas 

    2.1 {nav_menu_inicial} Menu inicial - Onde o usuário pode escolher duas opções, sendo elas:
        2.1.1 Entrar - informando seu PIN e os 4 útimos números do telefone, caso confirmados o usuário tem acesso ao menu secundário.
            > Possíveis erros e suas soluções:
                a. PIN ou Número incorretos: A possibilidade de até 3 tentativas, caso ocorra mais umma vez o acesso é bloqueado sendo apenas possível de reativálo pelo usuário administrado.
                b. Dados informados não existentes: Redirecionamento para a página de cadastro.
        2.1.2 Cadastrar-se - O usuários pode se cadastrar informando, ordenadamente:
            > Nome 
            > Email 
            > Telefone celular
            Ressaltando. O pin é automaticamente gerado na função de cadastro (Com 5 números)
            Após o cadastro o PIN é exibido ao usuário. A ação "cadastrar-se" deve ser confirmada pelo usuário, nela deve ser exibido todos os dados para que eles sejam confirmados.
    2.2 {nav_menu_secundario} Menu secundário e personalizado para o usuári0, ele vai ser o galho principal para a consulta de dados pessoais.  
        2.2.1 Cotação de pontos atual por KG e cada material, além da cotação de pontos por dinheiro - O usuário tem acesso total á cotação de pontos atual.
        2.2.2 Extrato de pontos / Total de pontos atuais - o usuário recebe o histórico de entrada e saida de pontos, e a situação de pontos atuaias do usuário.
        2.2.3 Informações - O usuário tem acesso a todos os seus dados cadastrados no sistema.
        2.2.4 "Sacar Pontos" - O usuário pode sacar seus pontos via pix.
        *****NOTA. Essa parte específica do programa é apenaas um simulação da restirada de pontos, que não necessáriamente vai acontecer desta forma.
        2.2.5 Reciclar - Em forma de menu, vai ser a simulaçao do usuário reciclando, e assim a entrada de dados. Assim como sacar pontos n~~ao necessáriamente pode fazer pare do sistema original. 
    2.3 Menu reciclar (2.2.5)
        2.3.1 Escolha do material - O usuáros vai digitaar a opção correspondente ao material a ser reciclado
            > Logo após a esolha vai confirmar a operação



