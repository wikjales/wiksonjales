def fat(n): #Definindo funcao para fatorial.
	if n == 0: #Verificando com o laco if se n e diferente de 0, pois 0 fatorial e 1, ou seja, e excessao.
		return 1 #Resultado de 0 fatoreal.
	return n*fat(n-1) #Valor de retorno sera o valor fatorial, ou seja, o numero multiplicando por ele menos 1, ate que chegue em 1.

def insPos(lista, tam, x, pos): #Definindo funcao reorganizar posicao.
	listaNova = []	#Criando nova lista vazia.
	for i in range(tam+1): #Usando laco for para definir o elemento da lista que vai ser adicionado.
		if i < pos: #Verificando com o laco if se a posicao e maior que i.
			listaNova.append(lista[i]) #Se a posicao for maior que i listaNova vai receber o valor de lista na posicao i.
		elif i == pos: #Se falso o teste do laco if entra em um novo if.
			listaNova.append(x) #Se verdadeiro o teste do novo laco if listaNova vai receber x.
		else: #Teste para possibilidade ser falsa.
			listaNova.append(lista[i-1]) #listaNova recebe lista na posicao i-1.

	return listaNova #Valor do retorno sera a lista organizada.

def allPerm(lista, tam): #Definindo funcao todas permutacoes.
	if tam == 1: #Testando se a varialvel tam e igual a 1.
		return [lista] #Se verdadeiro returna a lista lista.
	
	listaNova = [] #Criando lista listaNova vazia.
	for i in range(1,tam): #Usando laco for para definir intervalo e posicao que vai adicionado elemento.
		listaNova.append(lista[i]) #Adicionando elemento em listaNova dando de qual lista e qual posicao vai extrair.
	perm = allPerm(listaNova, tam-1) #Criando a varivel perm colocando seu valor o valor da funcao allPerm.
	permTotal = [] #Crindo lista permTotal vazia.
	for i in range(fat(tam-1)): #Usando laco for para definir elemento a ser adicionado.
		for j in range(tam): #Usando laco for para definir elemento a ser adicionado.
			permTotal.append(insPos(perm[i], tam-1, lista[0], j)) #Definindo valor a ser adicionado a variavel permTotal, assemelhando com as funcoes insPos e perm.

	return permTotal #Valor de retorno sera o valor da lista permTotal.

print "MENOR DISTANCIA \n" #Imprimindo nome do projeto.
print "Digite a regiao que voce quer viajar: \n\n Nordeste \n Norte \n Sul \n Suldeste \n CentroOeste \n"

regiao = raw_input()
i=2
while i == 2:
	if regiao == 'Nordeste':
		arquivo = open('nordeste.txt','r')
		i = 1
	elif regiao == 'Norte':
		arquivo = open('norte.txt','r')
		i = 1
	elif regiao == 'Sul':
		arquivo = open('sul.txt','r')
		i = 1
	elif regiao == 'Sudeste':
		arquivo = open('sudeste.txt','r')
		i = 1
	elif regiao == 'CentroOeste':
		arquivo = open('centroOeste.txt','r')
		i = 1
	else:
		print "Digite uma regiao valida:"
		regiao = raw_input()
		i = 2	

listaEstados = arquivo.readline()
amostraEstados = arquivo.readline()
sig = arquivo.readline()
estados = eval(listaEstados)
matriz = eval(amostraEstados)
arquivo.close()
legenda = eval(sig)

print "\nEscolha entre um dos estados disponiveis: \n" #Imprimindo dialogo com usuario.
print legenda #Imprimindo lista dos estados com siglas de cada um.
origem = raw_input('Defina a sigla da sua origem: ') #Criando variavel origem, como um valor que o usuario ira estabelecer, com um dialogo.
destino = raw_input('Defina a sigla do seu destino: ') #Criando variavel desino, com um valor que o usuario ira estabelecer, com um dialogo.
i = 2 #Criando variavel para validacao.
while i == 2: #Iniciando validacao usando laco while.
	if origem == destino: #Condicao para validar o programa, usando se os dois for iguais apresentar algum valor.
		print "Destino invalido, digite um destino diferente da origem!" #Imprime destino invalido quando usuario digita origem e destino iguais.
		origem = raw_input('Defina sua origem: ') #Variavel origem recebe uma nova entrada pelo usuario caso origem seja igual a destino.
		destino = raw_input('Defina seu destino: ') #Variavel destino recebe uma nova entrada pelo usuario caso destino seja igual a origem.
		i = 2		#Variavel i recebe valor 1 para concluir validacao.
	elif origem or destido == error :
		print "\n Origem e/ou destino invalido, digite uma sigla valida!\n"
		print legenda
		origem = raw_input('Defina sua origem: ') #Variavel origem recebe uma nova entrada pelo usuario caso origem seja igual a destino.
		destino = raw_input('Defina seu destino: ') #Variavel destino recebe uma nova entrada pelo usuario caso destino seja igual a origem.
		i = 2
	else: #Entra no else caso a validacao tenha sido concluida.
		i = 1 #Variavel i recebe valor 1 para concluir validacao.
print "Calculando..." #Imprime calculando.
listaEstados = estados #listaEstados criada para armazenar os estados disponiveis.
matrizPermuta = allPerm(listaEstados, 9) #Criando permutacao de estados chamando a funcao allPerm
tamanho = len(matrizPermuta) #Para definir o numero de elementos dentro da matriz.
print "Foram encontrados: ", tamanho, " rotas." #Imprime o numero de rotas possiveis com a origem e o destino informados.
matrizOrigem = [] #Criando a lista matrizOrigem vazia.
for i in range (tamanho): #Usando laco for para definir intervalo em que vai ser acionada a funcao matrizPermuta.
	if matrizPermuta[i][0] == origem and matrizPermuta[i][8] == destino: #Usando o if para capturar origem e destino para fazer as permutacoes.
		matrizOrigem.append(matrizPermuta[i]) #Escolhendo a linha da matriz para fazer a permutacao para criar a rota.
tamanho = len(matrizOrigem) #Definindo tamanho da lista de estados.
print "Foram encontradas: ", tamanho, " rotas possiveis." #Imprimindo o numero de rotas possiveis.
distancias = matriz #Definindo matriz com distancias entre os estados.
col = 0 #Criando a variavel col, representando o numero de colunas da matriz.
lin = 0 #Criando a variavel lin, representando o numero de linhas da matriz.
comb = 0 #Criando a variavel comb, representando o numero de de combinacoes possiveis para a rota.
distPoss = [] #Criando uma lista vazia para receber as distancias possiveis das rotas.
for i in range (tamanho): #Usando laco for para iniciar comparacao de acordo com o numero de elementos.
	for j in range(8): #Usando laco for para iniciar comparacao dentro das listas da matrizOrigem.
		for k in range(9): #Usando for para iniciar comparacao dos itens da lista de estados.
			if matrizOrigem[i][j] == listaEstados[k]: #Comparando a matrizOrigem com listaEstados para calcular e maperar a distancia entre os estados.
				col = k #Se iguais a variavel col, representando a posicao da coluna recebe valor de k.
				break #Anulando um possivel loop usando o break.
		for l in range (9): #Usando laco for para mapear as distancias.
			if matrizOrigem[i][j+1] == listaEstados[l]: #Verificando se elemento da matriz esta mapeado.
				lin = l #Se iguais a variavel lin, representando a posicao da linha recebe valor de l.
				break #Anulando um possivel loop usando o break.
		comb = comb + distancias[col][lin] #Fazendo combinacao das distancias para obter a distancia final.
	distPoss.append(comb) #Assemelhando a variavel comb, que representa a combinacao, para colocar na lista distPoss, ou seja, a distancia das rotas.

aux = 0 #Criando variavel auxiliar para ajudar na criacao da menor rota.
pos = 0 #Criando a variavel posicao para ajudar na criacao da menor rota.
for i in range(tamanho): #Usando laco for para ordenar as rotas por tamanho.
	if distPoss[i] > aux: #Comparando o tamanho da rota com a variavel auxiliar.
		aux = distPoss[i] #Se auxiliar for menor que a rota vai ser usado o auxiliar para organizar a rota.
		pos = i #Variavel pos recebendo valor de i para organizar a rota por tamanho.

for i in range(tamanho): #Usando laco for para ordenar as rotas por tamanho.
	if distPoss[i] < aux: #Comparando o tamanho da variavel auxiliar e da distancia.
		aux = distPoss[i] #Se auxiliar for maior que a rota vai ser usado o auxiliar para organizar a rota
		pos = i #Variavel pos recebendo valor de i para organizar a rota por tamanho.

print "\nMenor rota possivel: ", matrizOrigem[pos] #Printando dialogo com usuario e funcao matrizOrigem, onde mostra a menor rota possivel.
print "Distancia da menor rota: ",distPoss[pos] #Printando dialogo com usuario e funcao distPoss, onde mostra a distancia da menor rota possivel.
listaFinal = matrizOrigem[pos]  #Atribuindo na variavel listaFinal o valor resultante da funcao matrizOrigem[pos].
distanciaFinal = str(distPoss[pos]) #Atribuindo na variavel distanciaFinal o valor resultante da funcao distPoss[pos].
origem = str(matrizOrigem[0][0]) #Atribuindo na variavel origem o valor resultante da funcao matrizOrigem[0][0].
destino = str(matrizOrigem[0][8]) #Atribuindo na variavel destino o valor resultante da funcao matrizOrigem[0][8].
arquivo = open('menorDistancia.txt','w') #Criando arquivo txt com os dados do programa.
arquivo.write('I FOUND!\n\n') #Escrevendo no arquivo o nome do programa.
arquivo.write('Origem: '+origem) #Escrevendo no arquivo um dialogo e a origem definida pelo usuario.
arquivo.write('\nDestino: '+destino+'\n\n') #Escrevendo no arquivo um dialogo e o destino escolhido pelo usuario.
arquivo.write('Rota: ') #Escrevendo no arquivo um dialogo com o usuario.
for i in range (9): #Definindo ate onde uma funcao ser executada.
	arquivo.write(str(listaFinal[i])+' ') #Escrevendo no arquivo a funcao listaFinal, onde mostra a menor rota possivel.
arquivo.write('\nDistancia: '+distanciaFinal) #Escrevendo no arquivo um dialogo, a funcao distanciaFinal que mostra a distancia da menor rota.
arquivo.write('\n\nCopyright 2016') #Escrevendo no programa os direitos autorais.
arquivo.write('\nClarissa Maria')
arquivo.write('\nLuiz Phelype') #Escrevendo no arquivo nome de integrante.
arquivo.write('\nWikson Silva') #Escrevendo no arquivo nome de integrante.
arquivo.close() #Fechando o arquivo.

print "\n\nFIM!!!" #Imprimindo mensagem final do programa.
input()