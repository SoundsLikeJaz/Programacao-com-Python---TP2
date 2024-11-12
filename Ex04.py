def tabuada(n):
    """
    Exibe a tabuada de um número.
    
    --------------------------------------------------
    
    Args:
        int: Número a ser exibida a tabuada.
    """
    
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}');
        
def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Exibe a tabuada de 1 a 10.
    """
    
    for i in range(1, 11):
        tabuada(i);
        
main();