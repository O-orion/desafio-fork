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
    return sum(lista) / len(lista) 

# Função para calcular a mediana
def calcular_mediana(lista):
    # TODO: ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    # Primeiro, ordenamos a lista
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    # Se o tamanho for ímpar, retorna o elemento do meio
    if n % 2 != 0:
        return lista_ordenada[meio]
    else:
        # Se for par, retorna a média dos dois elementos centrais
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2


# Função para calcular a moda
def calcular_moda(lista):
    # TODO: encontrar o valor que mais aparece
    # 💡 Dica: use um dicionário para contar as ocorrências
    contagem = {}
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    # Encontra o maior valor de ocorrência
    maior_frequencia = max(contagem.values())

    # Retorna o(s) número(s) que aparecem mais vezes
    # (Aqui retornamos apenas um valor, o primeiro mais frequente)
    for numero, frequencia in contagem.items():
        if frequencia == maior_frequencia:
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
