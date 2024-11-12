TURMA = [];

def coletar_nome():
    """
    Coleta uma string com o nome do aluno.
    
    --------------------------------------------------
    
    Return:
        str: String coletada.
    """
    
    while True:
        nome = input("\nDigite o nome do aluno: ");
        if nome.isalpha() and len(nome) > 2:
            return nome;
        else:
            print("Nome inválido.");
            
def coletar_notas():
    """
    Coleta as notas do aluno.
    
    --------------------------------------------------
    
    Return:
        list: Lista com as notas do aluno.
    """
    
    notas = [];
    for i in range(2):
        while True:
            try:
                nota = float(input(f"\nDigite a {i + 1}ª nota do aluno: "));
                if nota < 0 or nota > 10:
                    print("Nota inválida! Digite uma nota entre 0 e 10.");
                else:
                    notas.append(nota);
                    break;
            except ValueError:
                print("Nota inválida! Digite uma nota válida.");
    return notas;

def definir_media(notas):
    """
    Calcula a média das notas de um aluno.
    
    --------------------------------------------------
    
    Args:
        list: Lista com as notas.
        
    Return:
        float: Média das notas.
    """
    
    return (sum(notas) / len(notas));

def definir_media_turma():
    """
    Calcula a média da turma.
    
    --------------------------------------------------
    
    Return:
        float: Média da turma.
    """
    
    return (sum([aluno["media"] for aluno in TURMA]) / len(TURMA));

def definir_situacao(media):
    """
    Define a situação do aluno.
    
    --------------------------------------------------
    
    Args:
        float: Média do aluno.
        
    Return:
        str: Situação do aluno, aprovado ou em prova final.
    """
    
    if media >= 6:
        return "Aprovado";
    else:
        return "Em prova final";
    
def coletar_dados_aluno():
    """
    Coleta os dados de um aluno.
    
    --------------------------------------------------
    
    Return:
        dict: Dicionário com os dados do aluno.
    """
    
    nome = coletar_nome();
    notas = coletar_notas();
    media = definir_media(notas);
    situacao = definir_situacao(media);
    return {"nome": nome, "notas": notas, "media": media, "situacao": situacao};
    
def criar_aluno():
    """
    Cria um aluno e adiciona na turma.
    """
    
    print("Iniciando entrada de dados do aluno.");

    while True:
        option = input("\nDigite 'fim' para encerrar ou qualquer outra tecla para adicionar um novo aluno: ");
        if option.lower() == "fim":
            break;
        
        aluno = coletar_dados_aluno();
        TURMA.append(aluno);
        
def exibir_alunos():
    """
    Exibe os alunos da turma.
    """
    
    print("Exibindo alunos da turma.");
    for aluno in TURMA:
        print(f"Nome: {aluno['nome']}", end=" - ");
        print(f"Notas: {aluno['notas']}", end=" - ");
        print(f"Média: {aluno['media']}", end=" - ");
        print(f"Situacao: {aluno['situacao']}. \n");
        
    print(f"Média da turma: {definir_media_turma()}.");
    
def main():
    """
    Função principal.
    
    --------------------------------------------------
    
    Descrição:
        Coleta os dados dos alunos e os exibe.
    """
    
    criar_aluno();
    exibir_alunos();
    
main();