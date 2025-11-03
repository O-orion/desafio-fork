"""
Desafio: Criar uma calculadora estatística simples em Python

Tarefa:
Implemente as funções abaixo para calcular média, mediana e moda de uma lista de números.

Instruções:
1. Faça o fork deste repositório no seu GitHub.
2. Clone o seu fork para sua máquina.
3. Complete as funções abaixo.
4. Teste o código executando: python calculadora_estatistica.py
5. Envie um Pull Request com a sua solução.

💡 Dica: não use bibliotecas externas como numpy ou statistics.
"""


# Função para calcular a média
def calcular_media(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 0:
        # média dos dois elementos centrais
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        # elemento central
        return lista_ordenada[meio]


# Função para calcular a moda
def calcular_moda(lista):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1

    max_ocorrencias = max(contagem.values())
    modas = [num for num, qtd in contagem.items() if qtd == max_ocorrencias]
