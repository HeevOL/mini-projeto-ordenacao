def half(lista):
    esquerda = []
    direita = []
    meio = len(lista)//2
    for x in range(len(lista)):
        if x < meio:
            esquerda.append(lista[x])
        else:
            direita.append(lista[x])
    return esquerda, direita

# Selection apenas com o maior


def selectionSort1(uma_lista):
    for posicao_verificada in range(len(uma_lista)-1, 0, -1):
        posicao_maior = 0
        for posicao in range(1, posicao_verificada+1):
            if uma_lista[posicao] > uma_lista[posicao_maior]:
                posicao_maior = posicao
        temp = uma_lista[posicao_verificada]
        uma_lista[posicao_verificada] = uma_lista[posicao_maior]
        uma_lista[posicao_maior] = temp


# Selection com maior e menor

def selectionSort(uma_lista):
    limite_esquerdo = 0
    for limite_direito in range(len(uma_lista)-1, len(uma_lista)//2-1, -1):
        posicao_maior = int(limite_esquerdo)
        posicao_menor = int(limite_direito)

        for posicao in range(limite_esquerdo, limite_direito+1):
            if uma_lista[posicao] >= uma_lista[posicao_maior]:
                posicao_maior = posicao

            if uma_lista[posicao] <= uma_lista[posicao_menor]:
                posicao_menor = posicao

        if limite_direito == posicao_menor and limite_esquerdo == posicao_maior:
            uma_lista[limite_direito], uma_lista[limite_esquerdo] = uma_lista[limite_esquerdo], uma_lista[limite_direito]

        else:
            temp_maior = uma_lista[limite_direito]
            temp_menor = uma_lista[limite_esquerdo]
            uma_lista[limite_direito] = uma_lista[posicao_maior]
            uma_lista[posicao_maior] = temp_maior

            if posicao_menor != limite_direito and posicao_maior != limite_esquerdo:
                uma_lista[limite_esquerdo] = uma_lista[posicao_menor]
                uma_lista[posicao_menor] = temp_menor

            elif posicao_menor == limite_direito:
                uma_lista[limite_esquerdo] = temp_maior
                uma_lista[posicao_maior] = temp_menor

            elif posicao_maior == limite_esquerdo:
                uma_lista[limite_esquerdo] = uma_lista[posicao_menor]
                uma_lista[posicao_menor] = temp_maior

        limite_esquerdo += 1

    return uma_lista


# MergeSort com slice

def mergeSort(uma_lista):
    if len(uma_lista) > 1:
        esquerda, direita = half(uma_lista)
        mergeSort(esquerda)
        mergeSort(direita)
        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                uma_lista[k] = esquerda[i]
                i = i+1
            else:
                uma_lista[k] = direita[j]
                j = j+1
            k = k+1

        while i < len(esquerda):
            uma_lista[k] = esquerda[i]
            i = i+1
            k = k+1

        while j < len(direita):
            uma_lista[k] = direita[j]
            j = j+1
            k = k+1

    return uma_lista


# Merge + Selection

def hibridSort(uma_lista):
    if len(uma_lista) > 128:
        meio = len(uma_lista)//2
        esquerda = uma_lista[:meio]
        direita = uma_lista[meio:]
        hibridSort(esquerda)
        hibridSort(direita)
        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                uma_lista[k] = esquerda[i]
                i = i+1
            else:
                uma_lista[k] = direita[j]
                j = j+1
            k = k+1

        while i < len(esquerda):
            uma_lista[k] = esquerda[i]
            i = i+1
            k = k+1

        while j < len(direita):
            uma_lista[k] = direita[j]
            j = j+1
            k = k+1

    else:
        limite_esquerdo = 0
        for limite_direito in range(len(uma_lista)-1, len(uma_lista)//2-1, -1):
            posicao_maior = int(limite_esquerdo)
            posicao_menor = int(limite_direito)

            for posicao in range(limite_esquerdo, limite_direito+1):
                if uma_lista[posicao] >= uma_lista[posicao_maior]:
                    posicao_maior = posicao

                if uma_lista[posicao] <= uma_lista[posicao_menor]:
                    posicao_menor = posicao

            if limite_direito == posicao_menor and limite_esquerdo == posicao_maior:
                uma_lista[limite_direito], uma_lista[limite_esquerdo] = uma_lista[limite_esquerdo], uma_lista[limite_direito]
            else:
                temp_maior = uma_lista[limite_direito]
                temp_menor = uma_lista[limite_esquerdo]
                uma_lista[limite_direito] = uma_lista[posicao_maior]
                uma_lista[posicao_maior] = temp_maior

                if posicao_menor != limite_direito and posicao_maior != limite_esquerdo:
                    uma_lista[limite_esquerdo] = uma_lista[posicao_menor]
                    uma_lista[posicao_menor] = temp_menor

                elif posicao_menor == limite_direito:
                    uma_lista[limite_esquerdo] = temp_maior
                    uma_lista[posicao_maior] = temp_menor

                elif posicao_maior == limite_esquerdo:
                    uma_lista[limite_esquerdo] = uma_lista[posicao_menor]
                    uma_lista[posicao_menor] = temp_maior

            limite_esquerdo += 1

    return uma_lista


if __name__ == "__main__":
    lista = [2, 1, 3, 8, 5, 6, 7, 9, 4, 10, 2, 1.2, 3, 8, 5, 6, 7, 9, 4, 10]
    print(selectionSort(lista))
