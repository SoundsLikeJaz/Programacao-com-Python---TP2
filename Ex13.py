LISTA = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1];

def separar_pares_impares(lista):
    """
    Separa os números pares e ímpares de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    Return:
        list, list: Listas com os números pares e ímpares.
    """
    
    pares = [];
    impares = [];
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero);
        else:
            impares.append(numero);
    
    return pares, impares;

def exibir_resultados(lista, pares, impares):
    """
    Exibe a lista original, os números pares e os números ímpares.
    
    --------------------------------------------------
    
    Args:
        a (list): Lista original.
        b (list): Lista com os números pares.
        c (list): Lista com os números ímpares.
    """
    print(f"Lista: {lista}");
    print(f"Pares: {pares}");
    print(f"Impares: {impares}");
    
def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Separa os números pares e ímpares de uma lista e exibe os resultados.
    """
    
    pares, impares = separar_pares_impares(LISTA);
    exibir_resultados(LISTA, pares, impares);
    
main();