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
    if len(lista) == 0:
        return 0
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)


# Função para calcular a mediana
def calcular_mediana(lista):
   if len(lista) == 0:
        return 0
        lista_ordenada = sorted(lista)
        n = len(lista_ordenada)
        meio = n // 2

        if n % 2 == 0:
         return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
        else:
            return lista_ordenada[meio]


# Função para calcular a moda
def calcular_moda(lista):
    if len(lista) == 0:
        return None

    contagens = {}
    for num in lista:
        if num in contagens:
            contagens[num] += 1
        else:
            contagens[num] = 1

    maior_frequencia = max(contagens.values())
    modas = [num for num, freq in contagens.items() if freq == maior_frequencia]

    
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
