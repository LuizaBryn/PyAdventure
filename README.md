# PyAdventure

Introdução

	Objetivo do desenvolvimento
Desenvolvimento de um programa para a disciplina de Análise e Projeto de Sistemas que gere partidas de um contra um do jogo criado pelo grupo PyAdventure a partir do suporte do PyNetGames. Estas partidas devem suportar jogador versus jogador e jogador versus máquina de forma on-line.

	Definições/Abreviaturas
	Regras do jogo

Em primeiro lugar, os dois jogadores escolherão um herói entre as opções: Guerreiro, Druida e Mago. Os jogadores podem escolher o mesmo herói. A diferença de um heróis para o outro é unicamente seus status, ou seja, cada um terá uma vantagem em algum dos três existentes: ataque, mana ou vitalidade. O objetivo do jogo é zerar os pontos de vida do herói adversário utilizando-se cartas que possuem (ou não) custo de mana.
	Após a escolha de seus heróis, cada jogador recebe 5 cartas aleatórias do baralho. O jogo será realizado em turnos, o primeiro a começar será por meio de sorteio.. Em seu turno, o jogador poderá ter duas ações: utilizar uma carta ou passar a vez para o adversário.  Após a primeira jogada de cada um, ou seja, em seu segundo turno, o jogador receberá uma carta do baralho.

	Atributos básicos:
Mana: 10
Ataque: 0
Vitalidade (pontos de vida): 60
	


Heróis:
Guerreiro - Vantagem em ataque - possui 2 pontos a mais de dano para as cartas: ataque básico e especial.
Mago - Vantagem em mana - possui 5 pontos a mais de mana.
Druida -  Vantagem em vitalidade - possui 10 a mais pontos de vida.

	Cartas:
Ataque básico - Custo: 2 de mana - Ataca o oponente retirando 3 de vida.
Meditar - Custo: 0 - Restaura 7 de mana.
Ataque especial - Custo: 5 de mana - Ataca o oponente retirando 7 de vida.
Barganha - Custo: 2 de mana - O jogador ganha duas cartas.
Cura - Custo: 3 de mana - Cure 5 de vida do herói.

Abreviaturas: 
RN : Regra de negócio 
RF : Requisito Funcional
RNF: Requisito não Funcional


Visão Geral
Premissas de desenvolvimento
O jogo deve ser desenvolvido em Python e suas tecnologias;
A interface do jogo deve ser feita utilizando a biblioteca TKinter;
O jogo deve utilizar PynetGames como suporte para execução distribuída;
Os diagramas de modelagem devem ser feitos em UML2, utilizando o software Visual Paradigm


Requisitos de Software

Requisitos Funcionais:

RF1 - Escolher 1 entre os 3 heróis disponíveis
RF2 - Escolher qual carta jogar a cada turno, utilizando uma das cartas que tem na mão.
RF3 - Passar a vez para o próximo jogador.
RF4 - Cada jogador tem o seu baralho de cartas
RF5 - Saber como está os status de vida e mana seu e do oponente.
RF6 - Cada herói possui atributos distintos, Vida, Mana e Ataque. 
RF7 - Conectar ao PlaNetGames e iniciar partida
RF8 - Comprar carta


Requisitos Não Funcionais:

RNF - O jogo vai ser implementado usando Python
RNF - A biblioteca gráfica que será utilizada é Tkinter
RNF - As modelagens serão feitas usando o software Visual Paradigm
RNF - O jogo poderá ser executado em desktops usando windows 10 e windows 11
RNF - As especificações mínimas para execução é um processador de 1ghz ou mais, e ao menos 4gb de ram.
RNF - Será utilizado PyNetGames para fazer a comunicação entre os jogadores.
