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
    if not lista:
        return 0
    return sum(lista) / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
    # TODO: ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    if not lista:
        return 0
    
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    
    if n % 2 == 1:
        # Se o tamanho é ímpar, retorna o elemento do meio
        return lista_ordenada[n // 2]
    else:
        # Se o tamanho é par, retorna a média dos dois elementos centrais
        meio1 = lista_ordenada[n // 2 - 1]
        meio2 = lista_ordenada[n // 2]
        return (meio1 + meio2) / 2


# Função para calcular a moda
def calcular_moda(lista):
    # TODO: encontrar o valor que mais aparece
    # 💡 Dica: use um dicionário para contar as ocorrências
    if not lista:
        return None
    
    # Contar ocorrências de cada elemento
    contagem = {}
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    
    # Encontrar o valor com maior frequência
    moda = max(contagem, key=contagem.get)
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
