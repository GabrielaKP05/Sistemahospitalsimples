from bebe import Bebe
from mae import Mae
from medico import Medico

# Crie instâncias das classes
mae1 = Mae("Maria", "Rua das Flores, 123", "(51) 12345-6789", "1970-01-01")
mae2 = Mae("Joana", "Av. do Forte, 456", "(51) 98765-4321", "1975-02-02")
mae3 = Mae("Ana", "Rua da Praia, 789", "(51) 11122-3344", "1980-03-03")

medico1 = Medico("12345", "Dr.José", "(51) 55555-6666", "Pediatra")
medico2 = Medico("67890", "Dr.Carlos", "(51) 77777-8888", "Obstetra")

bebe1 = Bebe("Pedro", "2023-11-01", 3.5, 50, mae1, medico1)
bebe2 = Bebe("Lucas", "2023-11-02", 3.2, 48, mae2, medico2)
bebe3 = Bebe("Julia", "2023-11-03", 3.3, 49, mae3, medico1)

# Função para pesquisar informações
def pesquisar():
    opcao = input("Você deseja pesquisar informações sobre: 1 - Bebês, 2 - Mães, 3 - Médicos? ")
    if opcao == "1":
        nome = input("Digite o nome do bebê: ")
        if nome == bebe1.get_nome():
            print("Informações do bebê:", bebe1.__dict__)
        elif nome == bebe2.get_nome():
            print("Informações do bebê:", bebe2.__dict__)
        elif nome == bebe3.get_nome():
            print("Informações do bebê:", bebe3.__dict__)
        else:
            print("Bebê não encontrado.")
    elif opcao == "2":
        nome = input("Digite o nome da mãe: ")
        if nome == mae1.get_nome():
            print("Informações da mãe:", mae1.__dict__)
        elif nome == mae2.get_nome():
            print("Informações da mãe:", mae2.__dict__)
        elif nome == mae3.get_nome():
            print("Informações da mãe:", mae3.__dict__)
        else:
            print("Mãe não encontrada.")
    elif opcao == "3":
        nome = input("Digite o nome do médico: ")
        if nome == medico1.get_nome():
            print("Informações do médico:", medico1.__dict__)
        elif nome == medico2.get_nome():
            print("Informações do médico:", medico2.__dict__)
        else:
            print("Médico não encontrado.")
    else:
        print("Opção inválida.")


pesquisar()

