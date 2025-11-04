"""
Desafio: Criar uma calculadora estatística simples em Python

Tarefa:
Impl=

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
