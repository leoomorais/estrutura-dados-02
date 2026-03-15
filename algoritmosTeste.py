from algoritmos import *

def run_tests():
    assert verificar_primeiro([10,20,30]) == 10
    assert verificar_primeiro([]) is None

    assert somar_lista([1,2,3,4]) == 10

    lista = [1,3,5,7,9]
    assert busca_binaria(lista,7) == 3
    assert busca_binaria(lista,2) == -1

    assert pares_com_soma([1,2,3,4],5) == [(1,4),(2,3)]

    elementos, pares = imprimir_pares_e_soma([1,2])
    assert elementos == [1,2]
    assert len(pares) == 4

    assert potencias_de_dois(10) == [1,2,4,8]

    assert fibonacci_recursivo(6) == 8

    assert ordenacao_bolha([5,3,1,4,2]) == [1,2,3,4,5]

    A = [[1,2],[3,4]]
    B = [[5,6],[7,8]]
    C = produto_de_matrizes(A,B,2)
    assert C == [[19,22],[43,50]]

    assert merge_sort([5,1,4,2,3]) == [1,2,3,4,5]

    print("Todos os testes passaram!")

run_tests()
