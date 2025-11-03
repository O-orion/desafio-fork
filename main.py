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

#from collections import Counter

# Função para calcular a média
def calcular_media(lista):
    """
    Calcula a média aritmética de uma lista de números.
    Retorna 0 se a lista estiver vazia para evitar erro de divisão por zero.
    """
    if not lista:
        return 0
    # TODO: implementar a soma dos elementos e dividir pelo tamanho da lista
    soma = sum(lista)
    tamanho = len(lista)
    media = soma / tamanho
    return media


# Função para calcular a mediana
def calcular_mediana(lista):
    """
    Calcula a mediana de uma lista de números.
    Retorna None se a lista estiver vazia.
    """
    if not lista:
        return None

    # TODO: ordenar a lista e encontrar o elemento do meio
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)

    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    if n % 2 == 1:
        # Tamanho ímpar: retorna o elemento central
        indice_mediana = n // 2
        mediana = lista_ordenada[indice_mediana]
    else:
        # Tamanho par: média dos dois elementos centrais
        indice1 = n // 2 - 1
        indice2 = n // 2
        mediana = (lista_ordenada[indice1] + lista_ordenada[indice2]) / 2

    return mediana


# Função para calcular a moda
def calcular_moda(lista):
    """
    Calcula a moda (o(s) valor(es) que mais aparece(m)) de uma lista.
    Retorna uma lista de modas ou None se a lista estiver vazia.
    """
    if not lista:
        return None

    # 💡 Dica: use um dicionário para contar as ocorrências
    # TODO: encontrar o valor que mais aparece
    ocorrencias = Counter(lista)
    
    # Encontra a frequência máxima (o maior número de ocorrências)
    frequencia_maxima = max(ocorrencias.values())
    
    # Filtra os elementos que têm a frequência máxima (pode haver mais de um)
    moda = [elemento for elemento, contagem in ocorrencias.items() if contagem == frequencia_maxima]
    
    # Retorna uma lista, pois pode ser multimodal
    return moda


def main():
    try:
        numeros = [10, 20, 20, 30, 40, 40, 40, 50]

        print("📊 Calculadora Estatística")
        print(f"Lista de números: {numeros}")
        print(f"Média: {calcular_media(numeros)}")
        print(f"Mediana: {calcular_mediana(numeros)}")
        print(f"Moda: {calcular_moda(numeros)}")

    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
