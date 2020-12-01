INTRODUÇÃO 
O grande crescimento das regiões urbanas gera uma demanda cada vez maior por soluções públicas capazes de atender com eficácia um número cada vez maior de pessoas.
Um dos pontos críticos das grandes metrópoles é certamente o transporte público. Em cidades saturadas de automóveis é cada vez mais necessária a mudança do modelo de transporte, para que seja capaz de ser uma alternativa viável ao transporte individual.
Metrôs, ônibus, táxis e muitas outras formas de transporte são utilizadas de forma coordenada a tornar as cidades verdadeiros organismos complexos, com diversos sistemas trabalhando em perfeita harmonia.
A quebra dessa harmonia pode causar diversos problemas aos usuários e até à cidade como um todo. Deste modo, são necessárias ferramentas de auditoria e monitoramento dos meios de transporte a fim de que eventuais ocorrências sejam detectadas e tratadas o quanto antes.
Com este panorama em mente mostrou-se necessário um sistema de auditoria de transporte público, que, através de um sistema de câmeras instaladas em pontos estratégicos das linhas de ônibus, realiza um monitoramento constante acerca dos horários de passagem dos ônibus em diversos locais da cidade, desse modo, verificando a pontualidade e a disponibilidade das linhas de ônibus que cobrem a cidade.
O aperfeiçoamento do controle dos transportes públicos passa inexoravelmente pela automação. Portanto, o desenvolvimento de um sistema prático, simples e confiável mostra-se uma alternativa viável para a solução de diversas questões relacionadas ao monitoramento de horários de ônibus, algo que gera conforto para os passageiros, que podem ter certeza de ter um sistema corretamente fiscalizado, confiabilidade e economia para as empresas que podem utilizar seus recursos técnicos e humanos de maneira mais eficiente, automatizando tarefas desgastantes e permitindo que seus colaboradores desempenhem funções onde o esforço humano é mais essencial.
1.1	OBJETIVOS DO TRABALHO
O objetivo geral deste trabalho é a demonstração do funcionamento de um sistema de auditoria completamente independente para os meios de transporte público e controle de frota através da eficácia da vigilância eletrônica com baixo custo de implementação.

Para a consecução deste objetivo foram estabelecidos os objetivos específicos:

 - Realizar a integração de uma câmera filmadora ao sistema;
 - Realizar a leitura de caracteres via OCR utilizando a tecnologia OpenCV;
 - Modelar um banco de dados para o cadastro das placas dos veículos e seus horários esperados de passagem nos pontos de checagem e realizar a implementação no sistema.


1.2 	CONTEÚDO DO TRABALHO
	O presente trabalho está estruturado em XX Capítulos, cujo conteúdo é sucintamente apresentado a seguir:
	No capítulo 2...
	O capítulo N...
2	FUNDAMENTAÇÃO TÉCNICA
O sistema foi desenvolvido de modo a funcionar em conjunto com uma câmera filmadora, estrategicamente posicionada para capturar as placas dos ônibus que passarem em um ponto pré-determinado. Uma vez que a placa do veículo é capturada, o frame é processado através do software de visão computacional OpenCV em um sistema desenvolvido em Python.

Uma vez que a placa do veículo é identificada, a mesma será comparada com as placas já cadastradas em um banco de dados MySQL e o horário da passagem do ônibus será comparado com os horários cadastrados no banco de dados. De acordo com o resultado da comparação será possível aferir se o ônibus está passando no horário correto, adiantado ou atrasado.

Instalar um conjunto de câmeras distribuídas em pontos estratégicos da FATEC para filmar o trânsito de modo a detectar as placas dos veículos que circulam pela via. Uma vez que um veículo com a placa cadastrada no sistema passa pela câmera, o sistema compara a hora em que o veículo passou pelo local e o horário em que ele habitualmente passa naquele mesmo local a fim de aferir a pontualidade do ônibus. Em caso de atraso, o mesmo é informado para a equipe de controle a fim de que o problema seja corrigido. Se após um período pré-determinado de tempo o veículo com a placa esperada não passa pelo ponto pré-determinado, a falha também é informada para a equipe de controle.
2.1	Tecnologias Utilizadas
As tecnologias utilizadas para o desenvolvimento do trabalho são três:
(1)	Python;
(2)	OpenCV;
(3)	MySQL
2.1.1	PYTHON
Python é uma linguagem de programação de alto nível e de uso geral, interpretada, usada amplamente, otimizada para a legibilidade do código, permitindo que os programadores sintetizem comandos em poucas linhas de código.
Suporta diversos paradigmas de programação, tais como orientação a objetos, programação funcional ou procedural. Também possui uma vasta biblioteca, disponível para o desenvolvimento dos mais variados tipos de aplicações.
Apesar de ser considerada uma linguagem de programação de aprendizado mais fácil e didático, o Python é uma linguagem muito extensa e flexível, permitindo que grandes aplicações sejam desenvolvidas. Empresas como Google, Dropbox, D-Link e Corel. Neste último caso, o uso de Python é tão extenso que a automatização de tasks (scripts para a aplicação de múltiplos efeitos visuais em imagens) é feita inteiramente em Python, necessitando que o designer tenha noções testa linguagem de programação.
Todos esses fatores foram determinantes para a decisão do uso de Python no desenvolvimento deste trabalho.
2.1.2	OPENCV
OpenCV (Open Source Computer Vision Library) é um software de código aberto desenvolvido para desempenhar tarefas de visão computacional e aprendizado de máquina. Foi desenvolvido para fornecer uma infraestrutura comum para aplicações que necessitem de visão computacional e percepção computadorizada de elementos.
Possui mais de 2500 bibliotecas que incluem poderosos algoritmos para reconhecimento de faces, objetos, textos, padrões, classificação de expressões corporais humanas em vídeo, reconhecimento e acompanhamento de movimentos, extração e mapeamento de pontos em 3D de objetos diversos, entre outros.
Grandes companhias, tais como Google, Yahoo!, Microsoft, IBM, Sony, Honda, entre outras, utilizam o OpenCV no desenvolvimento de grandes projetos comerciais. Por ser gratuita e de fácil desenvolvimento, também é a escolha de diversas startups que desenvolvem aplicações ligadas à visão computacional.
O OpenCV possui interfaces para diversas linguagens de programação, tais como C, C++, Python e Java, além de seu desenvolvimento poder ser feito em ambientes Windows, Linux, Android e Mac OS.
Sua escolha para o desenvolvimento deste trabalho deve-se ao seu amplo uso no meio profissional, sua grande flexibilidade e disponibilidade de ferramentas de desenvolvimento.
2.1.3	MYSQL
O MySQL é um dos sistemas de bancos de dados relacionais mais populares da atualidade. É usado de maneira ampla em aplicações web em modelo cliente-servidor. Apesar de ser um banco de dados de código aberto, atualmente é uma propriedade da Oracle, empresa líder no ramo de bancos de dados.
Os modelos de bancos de dados relacionais trabalham com tuplas, que são listas finitas de elementos ordenados. Esses elementos são agrupados em relações, que é definida por E.F. Codd (pegar fonte wikipedia) como um conjunto de tuplas (d1, d2, d3..., dn) onde cada elemento dj é um membro de Dj, um domínio de dados.
Suas grandes vantagens são sua flexibilidade e o suporte a múltiplas plataformas, possuindo interfaces de administração nos mais diversos sistemas operacionais, o que a torna ideal para o desenvolvimento deste trabalho.
2.2	Soluções Existentes
Durante a fase de pesquisa de soluções existentes foram encontradas algumas soluções de controle de frota que implicam na instalação de equipamentos nos veículos a serem monitorados, o que inviabiliza uma auditoria 100% externa, automatizada e constante.
Deste modo, a análise comparativa entre as soluções foi feita com base nas soluções mais próximas encontradas.
A Tabela 1 apresenta um comparativo das principais características das soluções analisadas.
Tabela 1: Comparativo das principais características entre as soluções
Característica	Sistema de Auditoria de Transportes Coletivos	Solução Móvel de Vídeo Vigilância para Ônibus e Trens	Gestão de Frotas de Ônibus - Rastro	CHM – Controle e Monitoramento de Horários
Possibilidade de Vigilância Remota	X	X	X	X
Compartilhamento de Informação com Clientes	X	X		X
Necessidade de infraestrutura nos veículos		X	X	X
Monitoramento totalmente externo	X			
2.2.1	Sistema de Auditoria de Transportes Coletivos
A principal característica, que torna este sistema único é a possibilidade de realização de auditoria de maneira completamente externa, sem a necessidade de instalação de transmissores ou receptores nos veículos auditados, assim como nenhuma outra colaboração por parte da empresa auditada, permitindo que o processo ocorra sem nenhuma influência e sem riscos de fraude.
Sua desvantagem é a limitação causada pelo modo não invasivo de auditoria. As câmeras posicionadas nos pontos chave captam o posicionamento e o horário do ônibus, entretanto, o acompanhamento só é atualizado nos trechos em que o ônibus é filmado, trabalhando com estimativas de posicionamento nos trechos não cobertos pelas câmeras. No entanto, o escopo do projeto é exatamente esse, uma auditoria de horários.
2.2.2	Solução Móvel de Vídeo Vigilância para Ônibus e Trens
A principal característica desta ferramenta são os diversos modos de acompanhamento disponibilizados pela mesma. Rastreamento por GPS, filmagem do interior dos veículos em tempo real e conexão segura com as autoridades são suas principais características.
Entretanto, esta ferramenta não se destina ao processo de auditoria, mas para um acompanhamento em tempo real dos veículos de uma concessionária ou empresa de transportes. Os equipamentos de vigilância devem obrigatoriamente ser instalados em todos os veículos a serem monitorados.
Dadas as características robustas do sistema, seu custo também é elevado, o que limita o leque de clientes a empresas mais sólidas, estabelecidas no mercado ou a concessionárias de transporte público que normalmente operam em regime de monopólio.
2.2.3	Gestão de Frotas de Ônibus - Rastro
Este sistema possui como diferencial o controle de comandos do veículo, podendo realizar o corte de combustível em caso de alarme de roubo ou algum outro alerta de violação. Também possui sistema de controle de quilometragem rodada pela frota, localização em tempo real e diversas estatísticas relacionadas à operação dos veículos.
Do mesmo modo que a solução anterior, sua implementação demanda de hardware especial a ser instalado em todos os veículos, sistemas de comunicação, GPS, transmissão de dados, o que encarece bastante a utilização do mesmo, apesar de permitir um alto grau de controle da frota.
2.2.4	CHM – Controle e Monitoramento de Horários
Este sistema possui como sua característica principal a previsão de passagem dos veículos em seus pontos de parada. Além da possibilidade do monitoramento online, é possível ter acesso ao playback das filmagens dentro dos veículos, monitoramento de ocorrências, análise gráfica de metas e controle de usuários com acesso ao sistema.
Apesar de ser bem menos robusto que os demais sistemas, este possui uma versão para consulta totalmente online, onde, mediante autenticação, é possível ter acesso a todas as funcionalidades liberadas para a classe de usuário.

2.3	Levantamento de Requisitos
Esta seção apresenta o levantamento de requisitos da solução proposta.(funcionalidades do projeto)
2.4	Definição dos Stakeholders
Este sistema foi desenvolvido para atender primeiramente a empresas de auditoria, que necessitam de ferramentas para controle de frotas de maneira completamente não-invasiva, de modo que o processo seja completamente invisível à empresa auditada, evitando deste modo fraudes e “maquiagem” do desempenho durante o período de auditoria.
Este sistema também pode ser utilizado por prefeituras que desejem monitorar o desempenho de concessionárias de transportes públicos, rondas de vigilantes motorizados ou quaisquer outros processos que demandem rondas e o percurso de circuitos em momentos pré-determinados.
Empresas de transporte coletivo também podem utilizar o sistema para o monitoramento da pontualidade de sua frota e o acompanhamento de profissionais específicos, permitindo a análise do desempenho dos profissionais contratados.
3	DESENVOLVIMENTO
A técnica utilizada para a elaboração deste trabalho é a pesquisa experimental. Os testes a serem realizados ocorrerão ora com simulações eletrônicas e emulação de leituras em etapas incrementais, sendo:
(1)	Leitura de caracteres simples;
(2)	Leitura de conjuntos de caracteres;
(3)	Reconhecimento de padrões e isolamento de caracteres desejados;
(4)	Leitura de imagens diretamente de dispositivo de filmagem;
(5)	Comparação de caracteres com valores salvos em bancos de dados;
(6)	Cálculo com timestamps de leitura das placas com timestamps previamente registradas em banco de dados;
(7)	Tratamento e disponibilização dos dados para dispositivos móveis.

3.1	Leitura de Caracteres Simples
Nesta fase do desenvolvimento, será testada a eficiência da leitura de caracteres simples em imagens com a utilização da ferramenta OpenCV juntamente com um primeiro programa desenvolvido em Python.
Os principais pontos a serem testados nesta fase são a correta integração do OpenCV com Python e sua eficácia para a leitura de caracteres.
3.2	Leitura de Conjuntos de Caracteres
Conjuntos de caracteres formados por letras e números serão processados nesta fase do desenvolvimento. O mesmo programa desenvolvido na fase anterior deverá mostrar-se capaz de reconhecer de maneira satisfatória conjuntos de caracteres diversos, formados por letras e números.
Um dos desafios a serem enfrentados nesta fase é o correto reconhecimento de letras e números, uma vez que a letra “O” pode ser confundida facilmente com o número “0” e a letra “I” pode ser confundida com o número “1”.
3.3	Reconhecimento de Padrões e Isolamento de Caracteres Desejados
Placas de automóveis possuem um padrão conhecido, tendo três letras e quatro algarismos, no formato “XXX-0000”. Entretanto, o OpenCV realiza a leitura de todos os caracteres visíveis na imagem, lendo também o nome da cidade registrado na placa e demais grafismos visíveis, tal como adesivos, mensagens diversas, entre outros.
Deste modo, haverá a necessidade da implementação de uma lógica que permita o reconhecimento do padrão alfanumérico da placa de identificação do veículo e o isolamento deste valor para a fase seguinte, que é a comparação da placa com os registros do banco de dados.
3.4	Leitura de Imagens Diretamente de Dispositivo de Filmagem
Para esta fase do projeto será realizada uma pesquisa de viabilidade de hardware com a finalidade de escolher a melhor câmera filmadora para realizar testes de leitura de placas reais.
Neste ponto, o sistema deverá ser capaz de reconhecer, em uma imagem em movimento, todos os caracteres alfanuméricos apresentados na mesma e realizar a leitura dos mesmos no instante em que forem reconhecidos, utilizando a lógica previamente desenvolvida para isolar apenas os caracteres relacionados à placa do veículo e o retorno do código alfanumérico através de uma saída em tela.
3.5	Comparação dos Caracteres com Valores de Bancos de Dados
Uma vez que todos os testes relativos à visão computacional sejam bem-sucedidos, estes dados deverão ser comparados com valores armazenados no banco de dados MySQL.
A primeira parte desta comparação será uma consulta básica ao banco de dados, onde será gerada uma “query” (mandar termo para o glossário) para realizar a consulta, verificando se o código alfanumérico correspondente à placa consta no banco de dados da aplicação.
Caso positivo, o sistema retornará uma resposta positiva, indicando que a placa obtida pertence a um veículo monitorado. Caso negativo, a placa será ignorada e o sistema realizará o monitoramento até que uma placa cadastrada no banco de dados seja detectada.
3.6	Cálculo com Timestamps de Leitura de Placas com Timestamps Previamente Registradas em Banco de Dados
Nesta fase do desenvolvimento o trabalho será realizado com timestamps. No momento em que o sistema detectar a passagem de um veículo com uma placa cadastrada no sistema, este evento desencadeará uma lógica que verificará o horário em que a leitura foi feita.
O horário da leitura será comparado com os horários pré-determinados no banco de dados, já com suas devidas tolerâncias, o que será usado para verificar se a leitura ocorreu dentro ou fora da faixa de horários estipulados.
Deste modo, será verificada a pontualidade do veículo, constatando-se atraso, adiantamento ou pontualidade do mesmo. Caso o resultado não esteja dentro da faixa considerada pontual, um alerta será emitido ao operador do sistema, que será informado que o veículo não foi registrado no horário devido, fornecendo, inclusive, o tempo de atraso ou adiantamento do mesmo.
Finalmente, existe um contador de viagens, que informa se o veículo foi detectado no local pré-determinado em todas as ocasiões programadas.
3.7	Tratamento e Disponibilização dos Dados para Dispositivos Móveis
A previsão da consulta da situação e dos horários de passagem dos veículos está prevista para ser disponibilizada para dispositivos móveis.
Através de um código único de linha a ser gerado no momento da alimentação do banco de dados, usuários poderão consultar os horários de passagem dos veículos nos pontos pré-determinados e a lista completa dos horários previstos para aquela linha.
Estes dados serão disponibilizados em um formato padronizado ainda a ser estudado. Esta seção será atualizada logo que a formatação dos dados for definida.
3.8	Requisitos Funcionais
Nesta seção estão relacionados todos os requisitos funcionais do sistema.

Requisito Funcional	LerPlaca
Descrição	Realiza a leitura computacional da placa do veículo no momento em que a mesma é capturada pela câmera
Entrada	Imagem de câmera filmadora
Origem	Banco de Dados
Saída	Valor alfanumérico correspondente à placa registrada
Destino	Consulta em Banco de Dados
Ação	CF: A leitura computacional da placa é realizada com sucesso e o código alfanumérico correspondente à mesma é enviado para consulta no banco de dados.
	CI: A leitura incorreta é ignorada e o sistema aguarda pela próxima leitura.
Requer	---
Pós‐Condição	Código alfanumérico da placa enviado para consulta ao banco de dados.







Requisito Funcional	AvisarAtraso
Descrição	Envia um aviso de atraso do veículo monitorado para o operador do sistema e disponibiliza o aviso para a interface de dispositivos móveis.
Entrada	Resultado de processamento lógico.
Origem	Processamento lógico do sistema.
Saída	Mensagem de atraso enviada ao operador e à interface de conexão com dispositivos móveis.
Destino	Tela do computador, interface para dispositivos móveis.
Ação	CF: O atraso registrado é informado para os componentes devidos.
	CI: O veículo está no horário; nenhuma providência precisa ser tomada.
Requer	CalcularAtraso
Pós‐Condição	Número da linha é sinalizado como atrasado.


Requisito Funcional	MontarRelatorio
Descrição	Realiza a montagem de um relatório com todos os horários de viagens esperados e obtidos do veículo monitorado.
Entrada	Mouse, teclado
Origem	Banco de Dados
Saída	Relatório de horários
Destino	Tela do Computador
Ação	CF: O relatório é montado e exibido ao operador do sistema.
	CI: Mensagem de erro.
Requer	---
Pós‐Condição	Retorna relatório solicitado pelo operador.

Requisito Funcional	IncluirPlaca
Descrição	Permite a inclusão da placa a ser monitorada pelo sistema.
Entrada	Código alfanumérico
Origem	Mouse, teclado
Saída	Inclusão de placa no banco de dados
Destino	Banco de dados do sistema
Ação	CF: A placa é incluída no sistema e os demais dados são solicitados
	CI: A entrada não é reconhecida como uma placa
Requer	---
Pós‐Condição	Placa inclusa no sistema; demais dados solicitados.

Requisito Funcional	IncluirCodigoLinha
Descrição	Permite a inclusão de um código único para a linha a ser monitorada pelo sistema.
Entrada	Código alfanumérico
Origem	Mouse, teclado
Saída	Inclusão do código no banco de dados
Destino	Banco de dados do sistema
Ação	CF: O código é incluído no sistema e os dados restantes são solicitados
	CI: A entrada não é reconhecida como um código válido
Requer	IncluirPlaca
Pós‐Condição	Código relativo à linha incluso no banco de dados do sistema; demais dados solicitados.



Requisito Funcional	IncluirHorariosLinha
Descrição	Permite a inclusão dos horários a serem comparados para a linha a ser monitorada pelo sistema.
Entrada	Códigos numéricos
Origem	Mouse, teclado
Saída	Inclusão da lista de horários no banco de dados
Destino	Banco de dados do sistema
Ação	CF: Os horários são incluídos no sistema e os dados restantes são solicitados
	CI: A entrada não é reconhecida como um horário válido
Requer	IncluirPlaca
Pós‐Condição	Lista de horários relativos à linha incluso no banco de dados do sistema; demais dados solicitados.

Requisito Funcional	IncluirNumeroViagens
Descrição	Permite a inclusão do número de viagens realizadas pela linha em um intervalo de 24 horas.
Entrada	Lista de valores pré-determinados
Origem	Mouse, teclado
Saída	Inclusão do número de viagens no sistema
Destino	Banco de dados do sistema
Ação	CF: A quantidade de viagens é inclusa no sistema; processo de cadastro de linhas finalizado.
	CI: A entrada não é reconhecida como um número de viagens válido.
Requer	IncluirPlaca
Pós‐Condição	Número de viagens da linha incluso no banco de dados do sistema; finalização do cadastro.

Requisito Funcional	EditarPlaca
Descrição	Permite a edição de uma placa monitorada pelo sistema.
Entrada	Código alfanumérico
Origem	Mouse, teclado
Saída	Edição de placa no banco de dados
Destino	Banco de dados do sistema
Ação	CF: A placa é editada no sistema e os demais dados são solicitados
	CI: A entrada não é reconhecida como uma placa; edição não foi feita com sucesso
Requer	---
Pós‐Condição	Placa editada no sistema

Requisito Funcional	EditarCodigoLinha
Descrição	Permite a edição do código único da linha monitorada pelo sistema.
Entrada	Código alfanumérico
Origem	Mouse, teclado
Saída	Edição do código no banco de dados
Destino	Banco de dados do sistema
Ação	CF: O código é editado no sistema e os dados restantes são solicitados
	CI: A entrada não é reconhecida como um código válido; edição não foi feita com sucesso
Requer	EditarPlaca
Pós‐Condição	Código relativo à linha editado no banco de dados do sistema

Requisito Funcional	EditarHorariosLinha
Descrição	Permite a edição dos horários a serem comparados para a linha monitorada pelo sistema.
Entrada	Códigos numéricos
Origem	Mouse, teclado
Saída	Edição da lista de horários no banco de dados
Destino	Banco de dados do sistema
Ação	CF: Os horários são editados no sistema e os dados restantes são solicitados
	CI: A entrada não é reconhecida como um horário válido
Requer	EditarPlaca
Pós‐Condição	Lista de horários relativos à linha editada no banco de dados do sistema

Requisito Funcional	EditarNumeroViagens
Descrição	Permite a edição do número de viagens realizadas pela linha em um intervalo de 24 horas.
Entrada	Lista de valores pré-determinados
Origem	Mouse, teclado
Saída	Edição do número de viagens no sistema
Destino	Banco de dados do sistema
Ação	CF: A quantidade de viagens é editada no sistema
	CI: A entrada não é reconhecida como um número de viagens válido
Requer	EditarPlaca
Pós‐Condição	Número de viagens da linha editado no banco de dados do sistema

Requisito Funcional	ExcluirPlaca
Descrição	Permite a exclusão de uma placa monitorada pelo sistema.
Entrada	Código alfanumérico
Origem	Mouse, teclado
Saída	Exclusão de placa e todos os dados referentes à mesma do banco de dados
Destino	Banco de dados do sistema
Ação	CF: A placa é excluída do banco de dados e os dados ligados a ela são excluídos
	CI: A placa não foi removida do sistema; dados permanecem gravados no banco.
Requer	---
Pós‐Condição	Placa e dados ligados a ela excluídos do sistema











Requisito Funcional	ExcluirCodigoLinha
Descrição	Permite a exclusão do código único da linha monitorada pelo sistema.
Entrada	Código alfanumérico
Origem	Mouse, teclado
Saída	Exclusão do código e todos os dados referentes ao mesmo do banco de dados
Destino	Banco de dados do sistema
Ação	CF: O código é excluído do sistema e os dados ligados a ele também o são
	CI: O código não foi removido do sistema; dados permanecem gravados no banco.
Requer	ExcluirPlaca
Pós‐Condição	Código e dados ligados a ele excluídos do sistema

Requisito Funcional	ExcluirHorariosLinha
Descrição	Permite a exclusão de horários a serem comparados para a linha monitorada pelo sistema.
Entrada	Códigos numéricos
Origem	Mouse, teclado
Saída	Exclusão de horários selecionados no banco de dados
Destino	Banco de dados do sistema
Ação	CF: Os horários são excluídos no sistema
	CI: Os horários não são excluídos e permanecem no banco de dados
Requer	ExcluirPlaca
Pós‐Condição	Horários selecionados são excluídos no banco de dados do sistema

Requisito Funcional	CalcularAtraso
Descrição	Realiza o cálculo do atraso da linha, comparando o horário de registro da placa do veículo com os horários listados no banco de dados
Entrada	Dados em formato timestamp
Origem	Dados do sistema
Saída	Timestamp com o tempo de atraso ou adiantamento da linha
Destino	AvisarAtraso
Ação	CF: O atraso é calculado e o resultado é enviado para AvisarAtraso
	CI: O veículo está no horário correto; nenhuma ação é tomada
Requer	---
Pós‐Condição	Atraso informado no sistema
3.8.1	Requisitos Não Funcionais
Requisitos aguardando OK do Orientador.
3.8.1.1	Requisito 1
...
3.8.1.2	Requisito N
...


	

