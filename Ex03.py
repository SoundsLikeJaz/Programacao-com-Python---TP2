nums = [];

def coletar_numeros():
    """
    Coleta números inteiros positivos e armazena em uma lista, encerrando a coleta quando o usuário digitar 0.
    """
    
    while True:
        try:
            num = int(input('Digite um número inteiro positivo ou 0 para finalizar: '));
            if num < 0:
                print('Número negativo não é permitido.');
            elif num == 0:
                break;
            else:
                nums.append(num);
                
        except ValueError:
            print('Digite um número inteiro.');

def fatorial(n):
    """
    Calcula o fatorial de um número.
    
    --------------------------------------------------
    
    Args:
        int: Número a ser calculado.
    Return:
        int: Fatorial do número.
    """
    
    if n == 0:
        return 1;
    elif n < 0:
        print('Fatorial de número negativo não existe.');
    else:
        return n * fatorial(n - 1);
    
def exibir():
    """
    Exibe o fatorial de cada número coletado.
    """
    
    for num in nums:
        print(f'O fatorial de {num} é {fatorial(num)}.');
        
def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Coleta números inteiros positivos e exibe o fatorial de cada número.
    """
    
    coletar_numeros();
    exibir();
    
main();