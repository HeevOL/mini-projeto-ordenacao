from sorts import *
import timeit
from random import randint

def test_selection():
    for lista_teste in conjunto_de_listas:   
        selectionSort(lista_teste)


def test_merge():
    for lista_teste in conjunto_de_listas:  
        mergeSort(lista_teste)


def test_hibrido():
    for lista_teste in conjunto_de_listas:  
        hibridSort(lista_teste)


def randlistas(lenght):
    lista = []
    for i in range(lenght):
        random = randint(0,200000)
        lista.append(random)
    
    return lista


if __name__ == "__main__":
    conjunto_de_listas = []
    for i in range(100):
        conjunto_de_listas.append(randlistas(1000))

    tempo_1k_selection = timeit.timeit(stmt=test_selection, number=1)
    tempo_1k_merge = timeit.timeit(stmt=test_merge, number=1)
    tempo_1k_hibrido = timeit.timeit(stmt=test_hibrido, number=1)

    print()
    print(f"Selection com 1000 elementos: {tempo_1k_selection}. Média: {tempo_1k_selection/100}")
    print(f"Merge com 1000 elementos: {tempo_1k_merge}. Média: {tempo_1k_merge/100}")
    print(f"Híbrido com 1000 elementos: {tempo_1k_hibrido}. Média: {tempo_1k_hibrido/100}")

    conjunto_de_listas = []
    for i in range(100):
        conjunto_de_listas.append(randlistas(10000))
    
    tempo_10k_selection = timeit.timeit(stmt=test_selection, number=1)
    tempo_10k_merge = timeit.timeit(stmt=test_merge, number=1)
    tempo_10k_hibrido = timeit.timeit(stmt=test_hibrido, number=1)

    print()
    print(f"Selection com 10000 elementos: {tempo_10k_selection}. Média: {tempo_10k_selection/100}")
    print(f"Merge com 10000 elementos: {tempo_10k_merge}. Média: {tempo_10k_merge/100}")
    print(f"Híbrido com 10000 elementos: {tempo_10k_hibrido}. Média: {tempo_10k_hibrido/100}")

    # ATENÇÃO DESCOMENTAR O CÓDIGO ABAIXO PARA TESTE PODE MANTER O CÓDIGO RODANDO POR MAIS DE 5 HORAS!
    # SELECTIONSORT VAI DEMORAR MUUUUUUITO PARA EXECUTAR, TENTE REDUZIR A QUANTIDADE DE LISTAS E/OU ELEMENTOS
    # OUTRA OPÇÃO É MANTER COMENTADO OS TESTES DE SELECTION, E MANTER O MERGE E O HÍBRIDO

    # conjunto_de_listas = []
    # for i in range(100):
    #     conjunto_de_listas.append(randlistas(100000))
    
    # tempo_100k_selection = timeit.timeit(stmt=test_selection, number=1)
    # tempo_100k_merge = timeit.timeit(stmt=test_merge, number=1)
    # tempo_100k_hibrido = timeit.timeit(stmt=test_hibrido, number=1)

    # print()
    # print(f"Selection com 100000 elementos: {tempo_100k_selection}. Média: {tempo_100k_selection/100}")
    # print(f"Merge com 100000 elementos: {tempo_100k_merge}. Média: {tempo_100k_merge/100}")
    # print(f"Híbrido com 100000 elementos: {tempo_100k_hibrido}. Média: {tempo_100k_hibrido/100}")