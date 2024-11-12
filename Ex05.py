def progressao_aritmetica(a1, razao):
    """
    Função que retorna o próximo termo da progressão aritmética.
    
    --------------------------------------------------
    
    Args:
        a1 (int): Primeiro termo da progressão aritmética.
        razao (int): Razão da progressão aritmética.
        
    Return:
        int: Próximo termo da progressão aritmética.
    """
    return a1 + razao;

def exibe_progressao_aritmetica(a1, razao):
    """
    Exibe os 10 primeiros termos de uma progressão aritmética.
    
    --------------------------------------------------
    
    Args:
        a1 (int): Primeiro termo da progressão aritmética.
        razao (int): Razão da progressão aritmética.
    """
    print(a1, end=", ");
    for i in range(9):
        print(progressao_aritmetica(a1, razao), end=", ");
        a1 = progressao_aritmetica(a1, razao);
        
def entrar_a1():
    """
    Solicita ao usuário que digite o primeiro termo da progressão aritmética.
    
    --------------------------------------------------
    
    Return:
        int: Primeiro termo da progressão aritmética.
    """
    
    while True:
        a1 = int(input('Digite o primeiro termo da progressão aritmética: '));
        if a1 > 0:
            return a1;
        print('Digite um número positivo.');
        
def entrar_razao():
    """
    Solicita ao usuário que digite a razão da progressão aritmética.
    
    --------------------------------------------------
    
    Return:
        int: Razão da progressão aritmética.
    """
    
    while True:
        razao = int(input('Digite a razão da progressão aritmética: '));
        if razao > 0:
            return razao;
        print('Digite um número positivo.');
        
def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Exibe os 10 primeiros termos de uma progressão aritmética.
    """
    
    a1 = entrar_a1();
    razao = entrar_razao();
    exibe_progressao_aritmetica(a1, razao);
    
main();