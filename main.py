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
    # soma de todos os elementos dividido pelo tamanho da lista
    return sum(lista) / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 0:
        # se for par, retorna a média dos dois elementos centrais
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        # se for ímpar, retorna o elemento central
        return lista_ordenada[meio]


# Função para calcular a moda
def calcular_moda(lista):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1

    max_ocorrencias = max(contagem.values())
    modas = [num for num, qtd in contagem.items() if qtd == max_ocorrencias]

    # se houver mais de uma moda, retorna todas
    if len(modas) == 1:
        return modas[0]
    else:
        return modas


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
