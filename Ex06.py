import math

def e_primo(num):
    """
    Verifica se um número é primo.
    
    --------------------------------------------------
    
    Args:
        int: Número a ser verificado.
    Return:
        bool: True se o número for primo, False caso contrário.
    """
    
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def coletar_inicio():
    """
    Coleta o início do intervalo a ser verificado.
    
    --------------------------------------------------
    
    Return:
        int: Início do intervalo.
    """
    
    while True:
        try:
            inicio = int(input("Digite o inicio do intervalo: "));
            if inicio < 0:
                print("Digite um número positivo.");
            else:
                return inicio
        except ValueError:
            print("Digite um número inteiro válido.");
            
def coletar_fim():
    """
    Coleta o fim do intervalo a ser verificado.
    
    --------------------------------------------------
    
    Return:
        int: Fim do intervalo.
    """
    
    while True:
        try:
            fim = int(input("Digite o fim do intervalo: "));
            if fim < 0:
                print("Digite um número positivo.");
            else:
                return fim
        except ValueError:
            print("Digite um número inteiro válido.");
            
def filtrar():
    """
    Filtra os números primos em um intervalo.
    
    --------------------------------------------------
    
    Return:
        list: Lista com os números primos encontrados no intervalo.
    """
    
    primos = [];
    inicio = coletar_inicio();
    fim = coletar_fim();
    
    for i in range(inicio, fim + 1):
        if e_primo(i):
            primos.append(i);
            
    return primos;

def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Solicita um intervalo ao usuário e exibe os números primos encontrados no intervalo.
    """
    primos = filtrar();
    print(f"Foram encontrados {len(primos)} números primos no intervalo. São eles: {primos}");
    
main();