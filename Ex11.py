LISTA = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100];

def coletar_numero():
    """
    Coleta um número inteiro.
    
    --------------------------------------------------
    
    Return:
        int: Número coletado.
    """
    
    while True:
        try:
            return int(input("Digite um número: "));
        except ValueError:
            print("Número inválido! Digite um número inteiro.");

def procurar(lista):
    """
    Procura um número em uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    """
    
    numero = coletar_numero();
    index = lista.index(numero) if numero in lista else -1;
    
    if index == -1:
        print(f"O número {numero} não está na lista.");
    else:
        print(f"O número {numero} está na posição {index} da lista.");
        
procurar(LISTA);