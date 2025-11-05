def calcular_media(lista):
    soma = 0

    for num in lista:
        soma += num
    
    return soma / len(lista)


def calcular_mediana(lista):
    lista.sort()
    
    tamanho_lista = len(lista)
    
    if tamanho_lista % 2 == 0:
        idx = tamanho_lista // 2
        return (lista[idx - 1] + lista[idx]) / 2
    else:
        return lista[tamanho_lista // 2]


def calcular_moda(lista):
    counts = {}
    
    for num in lista:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    moda = None
    max_count = 0
    
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            moda = num
    
    return moda


def main():
    try:
        numeros = [10, 20, 20, 30, 40, 40, 40, 50]

        print("Calculadora Estatística")
        print(f"Lista de números: {numeros}")
        print(f"Média: {calcular_media(numeros)}")
        print(f"Mediana: {calcular_mediana(numeros)}")
        print(f"Moda: {calcular_moda(numeros)}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
