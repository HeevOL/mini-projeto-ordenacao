def selectionSort1(uma_lista):
    for posicao_verificada in range(len(uma_lista)-1,0,-1):
        posicao_maior = 0
        for posicao in range(1,posicao_verificada+1):
            if uma_lista[posicao]>uma_lista[posicao_maior]:
                posicao_maior = posicao
        temp = uma_lista[posicao_verificada]
        uma_lista[posicao_verificada] = uma_lista[posicao_maior]
        uma_lista[posicao_maior] = temp
        

def selectionSort(uma_lista):
    i = 0
    for posicao_verificada in range(len(uma_lista)-1,len(uma_lista)//2-1,-1):
        posicao_maior = int(i)
        posicao_menor = posicao_verificada+i
        maior = False
        menor = False
        for posicao in range(i, posicao_verificada+1):
            if uma_lista[posicao] >= uma_lista[posicao_maior]:
                posicao_maior = posicao
                maior = True
            if uma_lista[posicao] <= uma_lista[posicao_menor]:
                posicao_menor = posicao
                menor = True

        if maior:
            temp = uma_lista[posicao_verificada]
            uma_lista[posicao_verificada] = uma_lista[posicao_maior]
            uma_lista[posicao_maior] = temp
        if menor:
            temp = uma_lista[0+i]
            uma_lista[0+i] = uma_lista[posicao_menor]
            uma_lista[posicao_menor] = temp

        i += 1

    return uma_lista


def mergeSort(uma_lista):
    if len(uma_lista)>1:
        meio = len(uma_lista)//2
        esquerda = uma_lista[:meio]
        direita = uma_lista[meio:]
        mergeSort(esquerda)
        mergeSort(direita)
        i=0
        j=0
        k=0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                uma_lista[k]=esquerda[i]
                i=i+1
            else:
                uma_lista[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            uma_lista[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            uma_lista[k]=direita[j]
            j=j+1
            k=k+1

    return uma_lista


def hibridSort(uma_lista):
    if len(uma_lista)>128:
        meio = len(uma_lista)//2
        esquerda = uma_lista[:meio]
        direita = uma_lista[meio:]
        hibridSort(esquerda)
        hibridSort(direita)
        i=0
        j=0
        k=0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                uma_lista[k]=esquerda[i]
                i=i+1
            else:
                uma_lista[k]=direita[j]
                j=j+1
            k=k+1

        while i < len(esquerda):
            uma_lista[k]=esquerda[i]
            i=i+1
            k=k+1

        while j < len(direita):
            uma_lista[k]=direita[j]
            j=j+1
            k=k+1

    else:
        i = 0
        for posicao_verificada in range(len(uma_lista)-1,len(uma_lista)//2-1,-1):
            posicao_maior = int(i)
            posicao_menor = posicao_verificada+i
            maior = False
            menor = False
            for posicao in range(i, posicao_verificada+1):
                if uma_lista[posicao] >= uma_lista[posicao_maior]:
                    posicao_maior = posicao
                    maior = True
                if uma_lista[posicao] <= uma_lista[posicao_menor]:
                    posicao_menor = posicao
                    menor = True

            if maior:
                temp = uma_lista[posicao_verificada]
                uma_lista[posicao_verificada] = uma_lista[posicao_maior]
                uma_lista[posicao_maior] = temp
            if menor:
                temp = uma_lista[0+i]
                uma_lista[0+i] = uma_lista[posicao_menor]
                uma_lista[posicao_menor] = temp

            i += 1

    return uma_lista


if __name__ == "__main__":
    lista = [2,1,3,8,5,6,7,9,4,10,2,1,3,8,5,6,7,9,4,10]
    print(selectionSort(lista))