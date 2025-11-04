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
    tamanho = len(lista)
    for numero in lista:
        soma += numero
    return soma / tamanho if tamanho > 0 else 0

# Função para calcular a mediana
def calcular_mediana(lista):
    lista.sort()
    if len(lista) % 2 == 1:
        return lista[len(lista) // 2]
    else:
        return (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2

# Função para calcular a moda
def calcular_moda(lista):
    contagem = {}
    for num in lista:
        contagem[num] = contagem.get(num, 0) + 1
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
