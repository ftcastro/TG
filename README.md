# TG
TG - from PyCharm


INTRODUÇÃO 
O grande crescimento das regiões urbanas gera uma demanda cada vez maior por soluções públicas capazes de atender com eficácia um número cada vez maior de pessoas.
Um dos pontos críticos das grandes metrópoles é certamente o transporte público. Em cidades saturadas de automóveis é cada vez mais necessária a mudança do modelo de transporte, para que seja capaz de ser uma alternativa viável ao transporte individual.
Metrôs, ônibus, táxis e muitas outras formas de transporte são utilizadas de forma coordenada a tornar as cidades verdadeiros organismos complexos, com diversos sistemas trabalhando em perfeita harmonia.
A quebra dessa harmonia pode causar diversos problemas aos usuários e até à cidade como um todo. Deste modo, são necessárias ferramentas de auditoria e monitoramento dos meios de transporte a fim de que eventuais ocorrências sejam detectadas e tratadas o quanto antes.
Com este panorama em mente mostrou-se necessário um sistema de auditoria de transporte público, que, através de um sistema de câmeras instaladas em pontos estratégicos das linhas de ônibus, realiza um monitoramento constante acerca dos horários de passagem dos ônibus em diversos locais da cidade, desse modo, verificando a pontualidade e a disponibilidade das linhas de ônibus que cobrem a cidade.
2.1	MOTIVAÇÃO
O aperfeiçoamento do controle dos transportes públicos passa inexoravelmente pela automação. Portanto, o desenvolvimento de um sistema prático, simples e confiável mostra-se uma alternativa viável para a solução de diversas questões relacionadas ao monitoramento de horários de ônibus, algo que gera conforto para os passageiros, que podem ter certeza de ter um sistema corretamente fiscalizado, confiabilidade e economia para as empresas que podem utilizar seus recursos técnicos e humanos de maneira mais eficiente, automatizando tarefas desgastantes e permitindo que seus colaboradores desempenhem funções onde o esforço humano é mais essencial.
2.1	OBJETIVOS
Nesta seção é descrito o objetivo do trabalho, detalhando os principais pontos explorados para atingir o resultado final.
2.1.1	OBJETIVO GERAL
Este trabalho tem como objetivo geral a implantação de um sistema de auditoria completamente independente nos meios de transporte público, seja entre cidades, seja urbano, através da eficácia da vigilância eletrônica e com baixo custo de implementação.
2.1	OBJETIVOS ESPECÍFICOS
Instalar um conjunto de câmeras distribuídas em pontos estratégicos da FATEC para filmar o trânsito de modo a detectar as placas dos veículos que circulam pela via. Uma vez que um veículo com a placa cadastrada no sistema passa pela câmera, o sistema compara a hora em que o veículo passou pelo local e o horário em que ele habitualmente passa naquele mesmo local a fim de aferir a pontualidade do ônibus. Em caso de atraso, o mesmo é informado para a equipe de controle a fim de que o problema seja corrigido. Se após um período pré-determinado de tempo o veículo com a placa esperada não passa pelo ponto pré-determinado, a falha também é informada para a equipe de controle.
2.1.1	ABORDAGEM METODOLÓGICA
O sistema foi desenvolvido de modo a funcionar em conjunto com uma câmera filmadora, estrategicamente posicionada para capturar as placas dos ônibus que passarem em um ponto pré-determinado. Uma vez que a placa do veículo é capturada, o frame é processado através do software de visão computacional OpenCV em um sistema desenvolvido em Python.

Uma vez que a placa do veículo é identificada, a mesma será comparada com as placas já cadastradas em um banco de dados MySQL e o horário da passagem do ônibus será comparado com os horários cadastrados no banco de dados. De acordo com o resultado da comparação será possível aferir se o ônibus está passando no horário correto, adiantado ou atrasado.
