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
    # Implementar a soma dos elementos e dividir pelo tamanho da lista
    # Tratamento básico: se a lista estiver vazia, retornar 0 para evitar ZeroDivisionError
    if not lista:
        return 0

    total = 0
    for numero in lista:
        total += numero

    return total / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
    # Ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    # Tratamento básico: se a lista estiver vazia, retornar 0
    if not lista:
        return 0

    ordenada = sorted(lista)
    n = len(ordenada)
    meio = n // 2

    # Se n ímpar, retorna o elemento do meio
    if n % 2 == 1:
        return ordenada[meio]
    # Se n par, retorna a média dos dois elementos centrais
    else:
        return (ordenada[meio - 1] + ordenada[meio]) / 2


# Função para calcular a moda
def calcular_moda(lista):
    # Encontrar o valor que mais aparece
    # 💡 Dica: use um dicionário para contar as ocorrências
    # Se a lista estiver vazia, não há moda definida
    if not lista:
        return None

    ocorrencias = {}
    for numero in lista:
        ocorrencias[numero] = ocorrencias.get(numero, 0) + 1

    # Encontra a(s) chave(s) com a maior contagem
    max_count = max(ocorrencias.values())
    modos = [valor for valor, cont in ocorrencias.items() if cont == max_count]

    # Se houver apenas um modo, retorna o valor; se houver empate, retorna a lista de modos
    if len(modos) == 1:
        return modos[0]
    else:
        return sorted(modos)


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
