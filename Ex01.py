def is_vowel(letter):
    """
    Verifica se uma letra é uma vogal.
    
    --------------------------------------------------
    
    Args: 
        str: Letra a ser verificada.
    Return: 
        bool: True se a letra for uma vogal, False caso contrário.
    """
    
    return letter in 'aeiou';

def entrar_letra():
    """
    Solicita ao usuário que digite uma letra.
    
    --------------------------------------------------
    
    Return:
        str: Letra digitada pelo usuário.
    """
    
    while True:
        letra = input('Digite uma letra: ');
        if len(letra) == 1:
            return letra;
        print('Digite apenas uma letra');
        
def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Conta quantas vogais foram digitadas pelo usuário.
    """
    
    vogais = 0;
    letra = entrar_letra();
    while letra != '.':
        if is_vowel(letra):
            vogais += 1;
        letra = entrar_letra();
        
    if vogais == 0:
        print("Nenhuma vogal foi digitada.");
    elif vogais == 1:
        print("Apenas uma vogal foi digitada.");
    else:
        print(f"{vogais} vogais foram digitadas.");
    
main();