# Função para calcular a média
def calcular_media(lista):
    # Soma todos os elementos e divide pelo tamanho da lista
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    return media


# Função para calcular a mediana
def calcular_mediana(lista):
    # Ordena a lista
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    # Se o tamanho for ímpar, retorna o elemento do meio
    if n % 2 != 0:
        return lista_ordenada[meio]
    else:
        # Se for par, faz a média dos dois elementos centrais
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2


# Função para calcular a moda
def calcular_moda(lista):
    contagem = {}
    for num in lista:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1

    # Encontra o valor mais frequente
    max_ocorrencias = max(contagem.values())
    modas = [num for num, freq in contagem.items() if freq == max_ocorrencias]

    # Se houver mais de uma moda, retorna a lista delas
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
