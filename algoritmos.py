def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]


def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


def pares_com_soma(lista, alvo):
    resultado = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                resultado.append((lista[i], lista[j]))
    return resultado


def imprimir_pares_e_soma(lista):
    elementos = []
    pares = []

    for i in range(len(lista)):
        elementos.append(lista[i])

    for i in range(len(lista)):
        for j in range(len(lista)):
            pares.append((lista[i], lista[j]))

    return elementos, pares


def potencias_de_dois(n):
    resultado = []
    i = 1
    while i < n:
        resultado.append(i)
        i *= 2
    return resultado


def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def ordenacao_bolha(lista):
    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def produto_de_matrizes(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado
