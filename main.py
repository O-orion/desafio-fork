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
    media = 0
    soma = 0

    for i in lista:
        soma += i

    media = soma/len(lista)
    return media
    # TODO: implementar a soma dos elementos e dividir pelo tamanho da lista
    


# Função para calcular a mediana
def calcular_mediana(lista):
    mediana = 0
    lista.sort()
    tamanho = len(lista)
    if tamanho%2==1:

        mediana = lista[tamanho//2]
    
    else:
        meio1 = lista[tamanho//2-1] 
        meio2 = lista[tamanho//2]
        mediana = (meio1+meio2)/2

    return mediana

    # TODO: ordenar a lista e encontrar o elemento do meio
    # 💡 Dica: se o tamanho for par, tire a média dos dois elementos centrais
    


# Função para calcular a moda
def calcular_moda(lista):
    contagem = {}  
    
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

   
    maior_frequencia = max(contagem.values())
    
    
    modas = [num for num, freq in contagem.items() if freq == maior_frequencia]
    
    if len(modas) == 1:
        return modas[0]
    else:
        return modas 
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
