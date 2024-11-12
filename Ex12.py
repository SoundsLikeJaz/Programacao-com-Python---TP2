LISTA = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1];

def definir_media(lista):
    """
    Define a média de uma lista de números.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    Return:
        float: Média dos números.
    """
    
    return sum(lista) / len(lista);

def definir_maior(lista):
    """
    Define o maior número de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    Return:
        int: Maior número.
    """
    
    return max(lista);

def definir_menor(lista):
    """
    Define o menor número de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    Return:
        int: Menor número.
    """
    
    return min(lista);

def definir_soma(lista):
    """
    Define a soma dos números de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    Return:
        int: Soma dos números.
    """
    
    return sum(lista);

def exibir_resultados(lista):
    """
    Exibe a lista, a média, o maior número, o menor número e a soma dos números de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    """
    
    print(f"Lista: {lista}");
    print(f"Média: {definir_media(lista)}");
    print(f"Maior número: {definir_maior(lista)}");
    print(f"Menor número: {definir_menor(lista)}");
    print(f"Soma: {definir_soma(lista)}");
    
exibir_resultados(LISTA);