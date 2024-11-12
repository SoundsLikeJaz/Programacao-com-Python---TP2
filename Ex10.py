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
            numero = float(input("Digite um número ou 0 para encerrrar: "));
            if numero == 0:
                break;
            else:
                lista.append(numero);
        except ValueError:
            print("Número inválido! Digite um número válido.");
    return lista

def definir_media(lista):
    """
    Calcula a média dos números de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
        
    Return:
        float: Média dos números.
    """
    
    return sum(lista) / len(lista);

def definir_maiores(lista):
    """
    Define os números maiores que a média de uma lista.
    
    --------------------------------------------------
    
    Args:
        list: Lista com os números.
    Return:
        list: Lista com os números maiores que a média.
    """
    maiores = [];
    media = definir_media(lista);
    for numero in lista:
        if numero > media:
            maiores.append(numero);
    return maiores;

def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Coleta números inteiros positivos e exibe a média destes números e os números maiores que a média.
    """
    
    lista = coletar_numeros();
    print(f"Os números digitados foram: {lista}");
    print(f"A média destes números é {definir_media(lista)} e os números maiores que a média são: {definir_maiores(lista)}");
    
main();