# Função para calcular a média
def calcular_media(lista):
    # TODO: implementar a soma dos elementos e dividir pelo tamanho da lista
    # 🔧 Implementação:
    soma = 0
    for numero in lista:
        soma += numero
    media = soma / len(lista)
    return media


# Função para calcular a mediana
def calcular_mediana(lista):
    # TODO: ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    # 🔧 Implementação:
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 == 0:
        mediana = (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        mediana = lista_ordenada[meio]

    return mediana


# Função para calcular a moda
def calcular_moda(lista):
    # TODO: encontrar o valor que mais aparece
    # 💡 Dica: use um dicionário para contar as ocorrências
    # 🔧 Implementação:
    contagem = {}
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    maior_freq = max(contagem.values())
    for numero, freq in contagem.items():
        if freq == maior_freq:
            return numero


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