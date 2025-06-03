nomes = ["Ana", "Lucas", "Beatriz"]



print("Menu")
print("1 - Cadastro.")
print("2 - Lista de contatos.")
print("3 - Excluir contato.")
print("0 - SAIR ")

menu = int(input('Digite o código:'))

match menu:
        case 1:
            nome = input("Digite o seu nome: ")  
            nomes.append(nome)                   
            print("Cadastrado :-)")
            print("Lista atualizada:", nomes)
        case 2:
            print(nomes)
        case 3:
            nome_remover = input("Digite o nome que deseja remover: ")
            if nome_remover in nomes:
                nomes.remove(nome_remover)
                print(f"{nome_remover} removido com sucesso!")
                print("Lista atualizada:", nomes)
            else:
                print("Nome não encontrado.")
        case _:
            print('Fechando agenda..')