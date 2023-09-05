IBM challenge
Sprint II - Computational Thinking with Python

Decidimos que as funcionalidades implementadas girariam em torno da ODS (Objetivos de Desenvolvimento Sustentável) 11.6 Até 2030, reduzir o impacto ambiental negativo per capita das cidades, inclusive prestando especial atenção à qualidade do ar, gestão de resíduos municipais e outros. Nesse sentido daremos um foco maior a gestão de residuos municipais, com programas centralizados em reciclagem.
Atravez da produção de lixeiras inteligentes juntamente à um software que registra a quantidade total de componentes reciclados pelo indivíduo, e a partir disso gera recompensas de empresas parceiras. Assim como os “elos” de reciclagem que evoluem e vão formando uma reputação, e fazem os usuários terem mais interesse em contribuir
__________________________________________________________________________________________________________________________________________________

Notas sobre o programa (Por emma, para o grupo, vai ser totalmente descartado antes de ser entregue)

1 - Estabelecendo os dados
    Todas as informações que vamos precisar para que o programa consiga funcionar 
    
    1.1 Usuário - O nome do usuário, informado ao sistenma na hora do cadastro.
    1.2 Pin - Principal fonte de identificação, único para cada usuário - pode ser pré definindo pelo usuario admnistrador ou no protocolo normal - no caso vai ser gerado aleatóriamente via sorteio (import random)
    1.3 Email - Informado ao sistema atraves do cadastro, utilizado para a comunicação com o cliente (*Vamos armazenar o dado no programa mas não necessáriamente vamos utilizar praticamente ele - até porque não entramos ainda no tópico na matéria*)
    1.4 Número de telefone celular - informado ao sistema na hora do cadastro, tambémm utilizado para a comunicação com o cliente. 
    NOTA. Vale deixar claro que a implementação de ambos email e celular no cadastro fomenta a oportunidade perfeita para utilizar o regex
    1.5 Dados - Um nested dictionary que vai conter as prinicipais funções do programa, até porque lá vai ter a maior quantidade de informações possíveis sobre o usuário, sendo elas:
        1.5.1 {reciclagem_kg} Kg de reciclagem - A quantidade total de kg reciclados pelo usuário ate o momento de consulta.
        1.5.2 {pontos} Pontos - A quantidade total de pontos do usuário até a hora da consulta, eles são definidos através dos KG reciclados multiplicados a cotação de pontos - que mais pra frente vai ser descrito corretamente.
    1.6 Cotação de pontos - Em formato de dicionário, vai armazenar a quantidade de pontos equivaleentes a cada 

