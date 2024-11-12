def coletar_numeros():
    """
    Coleta números inteiros positivos e armazena em uma lista, encerrando a coleta quando o usuário digitar 0.
    
    --------------------------------------------------
    
    Return:
        list: Lista com os números coletados.
    """
    
    lista = [];
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo ou 0 para encerrrar: "));
            if numero < 0:
                print("Número inválido! Digite um número inteiro positivo.");
            elif numero == 0:
                break;
            else:
                lista.append(numero);
        except ValueError:
            print("Número inválido! Digite um número inteiro positivo.");
    return lista

def inverter(lista):
    """
    Inverte a ordem dos elementos de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista a ser invertida.
    Return:
        list: Lista invertida.
    """
    
    return lista[::-1];

def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Coleta números inteiros positivos e exibe a lista original e a lista invertida.
    """
    
    lista = coletar_numeros()
    print(f"Lista original: {lista}");
    print(f"Lista invertida: {inverter(lista)}");
    
main();