def coletar_numero():
    """
    Coleta um número inteiro.
    
    --------------------------------------------------
    
    Return:
        int: Número coletado.
    """
    
    while True:
        try:
            numero = int(input("Digite um número: "));
            if numero < 0:
                print("Número inválido! Digite um número inteiro positivo.");
        except ValueError:
            print("Número inválido! Digite um número inteiro.");