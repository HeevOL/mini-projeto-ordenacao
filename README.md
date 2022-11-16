Integrantes:
Heverton de Oliveira Lourenço, José Adrian Torres dos Santos

Conteúdos de consulta:
Adrian, Heverton:

Material disponibilizado no classroom.
Documentação do timeit, para melhor compreensão do seu uso. Disponível em: https://docs.python.org/3/library/timeit.html

Dificuldades:

Heverton: 
*   Demorei bastante para implementar o SelectionSort buscando o maior e o menor em cada varredura, não era dificil,mas transcrever a lógica demandou certo tempo, os erros eram sempre besteiras e o debug ajudou muito!
*   Para a segunda questão imaginei criar variaveis de controle para armazenar as posições de inicio e fim da lista e de suas "sublistas virtuais", mas não consegui implementar até o momento.
*   O teste de 100 listas de 100.000 elementos cada seria algo muito demorado para testar fazendo o uso do SelectionSort, mudei para 5 teste que durou em média de 186 segundos (3,1 minutos), então fazer os 100 testes demoraria mais de 5 horas.
*   No teste híbrido pensei em fazer as chamadas das funções, mas não tinha certeza do funcionamento. Imaginei que seria trabalhoso demais tratar os erros que poderiam acontecer no retorno das funções. Por exemplo: Quando o Merge criasse uma lista menor que 128 elementos deveria ser feito o selection, mas como eu garantiria que essa lista enviada para o SelectionSort seria corretamente posicionada no MergeSort depois de ser retornada? Por ser um slice da lista principal acredito que não seria um problema, mas peguei o caminho mais seguro e optei por apenas copiar o código (tenho a consciência que seria uma melhoria de código muito bem vinda e em certos casos obrigatória.), DESCULPA! 

Adrian:

Resumo da avaliação de desempenho:

*   A diferença entre o tempo total e médio das ordenações feitas tanto pelo SelectionSort apenas do ultimo elemento, quanto do SelectionSort dos elementos de inicio e fim, possuem uma certa diferença de tempo, o SelectionSort com ínicio e fim é mais rápido (Em alguns testes provou levar aproximadamente 68% do tempo que o SelectionSort do ultimo elemento levaria.), mas continua ineficiente quando estamos trabalhando com listas com um grande volume de dados.
*   É praticamente incomparavél a diferença que o MergeSort tem sobre a SelectionSort, mesmo em listas com quantidades de dados pequenas. 
12x mais rápida com listas de 1000 elementos; 
87x mais rápida em listas com 10000 elementos;
732x mais rápida em listas com 100000 elementos!!!
*   Isso só mostra a importancia de saber utilizar a estrutura de dados certa para cada caso particular que o programador encontrar.
*   O uso do código híbrido não teve uma diferença significativa em comparação com o MergeSort puro, a limitação para o uso do SelectionSort foi para listas pequenas de até 127 elementos por isso o impacto no timing não foi tão grande. É de se esperar que o uso do código híbrido seja inferior, pois mesmo no melhor cénario de SelectionSort[O(n²)] ele ainda será mais lento que o MergeSort[O(n log n)]. Com isso, o uso do SelectionSort é mais recomendado quando há a limitação do espaço de mémoria. Onde SelectionSort[O(1)] e MergeSort[O(n)], isso se dá por que o Selection faz as operações na mesma lista de elementos, enquanto o Merge cria listas a parte. O que me faz pensar se é realmente possivel implementar o Merge sem o operador de slice que foi pedido na segunda questão. Se não for possivel foi uma brincadeira de mau gosto de sua parte, professor. Ficarei muito triste. :(