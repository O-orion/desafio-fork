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
    # TODO: implementar a soma dos elementos e dividir pelo tamanho da lista
    pass


# Função para calcular a mediana
def calcular_mediana(lista):
    # TODO: ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    pass


# Função para calcular a moda
def calcular_moda(lista):
    # TODO: encontrar o valor que mais aparece
    # 💡 Dica: use um dicionário para contar as ocorrências
    pass
def calcular_media(lista):
    if not lista:
        return None  # ou lançar um erro, dependendo da preferência
    return sum(lista) / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
    if not lista:
        return None
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 1:
        # Tamanho ímpar: retorna o elemento do meio
        return lista_ordenada[meio]
    else:
        # Tamanho par: retorna a média dos dois elementos centrais
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2


# Função para calcular a moda
def calcular_moda(lista):
    if not lista:
        return None
    contagem = {}
    for valor in lista:
        contagem[valor] = contagem.get(valor, 0) + 1

    max_contagem = max(contagem.values())
    # Encontra todos os valores com a contagem máxima
    modas = [k for k, v in contagem.items() if v == max_contagem]

    # Se todos os valores aparecem com a mesma frequência, não há moda
    if len(modas) == len(set(lista)):
        return None  # ou uma mensagem indicando que não há moda

    return modas[0]  # Retorna a primeira moda encontrada



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
