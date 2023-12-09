catalogo = []

def adicionar_livro():
    titulo= str(input("Digite o título do Livro: "))
    autor = str (input("Digite o nome do autor: "))
    ano= int (input("Digite o ano da publicação: "))
    identificador= len (catalogo) + 1
    livro = {"Título": titulo, "Autor": autor, "Ano": ano, "ID": identificador}
    catalogo.append(livro)
    print ("Livro adicionado com sucesso!")

def listar_livros():
    if not catalogo:
        print ("Biblioteca vazia")
    else:
        print("CATÁLOGO DE LIVROS")
        for livro in catalogo:
            print(f"ID:{livro['ID']} - Título:{livro['Título']} - Autor:{livro['Autor']} - Ano:{livro['Ano']}")    

def emprestimo_livro():
    listar_livros()
    id_livro = int(input("Digite o ID do livro que deseja emprestar: "))
    for livro in catalogo:
        if livro['ID'] == id_livro:
            livro['Emprestado para'] = input("Digite o nome do destinatário: ")
            livro['Data de Devolução'] = input("Digite a data de devolução (DD/MM/YYYY): ")
            print("Livro emprestado com sucesso!")
            return
    print("Livro não encontrado.")

def retorno_livro():
    listar_livros()
    id_livro = int(input("Digite o ID do livro que deseja retornar: "))
    for livro in catalogo:
        if livro['ID'] == id_livro and 'Emprestado para' in livro:
            del livro['Emprestado para']
            del livro['Data de Devolução']
            print("Livro retornado com sucesso!")
            return
    print("Livro não encontrado ou não está emprestado.")


while True:
    menu= int(input ("""        -----Menu----
        1-Adicionar Livro
        2-Listar livros
        3-Empréstimo de livro
        4-Retorno de Livro
        5-Sair 
                     """))
    
    if menu == 1:
        adicionar_livro()
    elif menu == 2:
        listar_livros()
    elif menu == 3:
        emprestimo_livro()
    elif menu == 4:
        retorno_livro()
    elif menu == 5:
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")