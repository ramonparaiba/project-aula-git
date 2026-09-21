"""Gerenciador de tarefas simples para o terminal."""


def exibir_menu():
    """Exibe as opções disponíveis no programa."""
    print("\n=== TASK CLI ===\n")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("0 - Sair")


def listar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas."""
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\nTarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "x" if tarefa["concluida"] else " "
        print(f'{indice} - [{status}] {tarefa["descricao"]}')


def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista."""
    descricao = input("\nDigite a descrição da tarefa: ").strip()

    if not descricao:
        print("A descrição não pode ficar vazia.")
        return

    nova_tarefa = {
        "descricao": descricao,
        "concluida": False,
    }
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")


def concluir_tarefa(tarefas):
    """Marca uma tarefa escolhida pelo usuário como concluída."""
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    listar_tarefas(tarefas)

    try:
        numero = int(input("\nDigite o número da tarefa concluída: "))
    except ValueError:
        print("Digite um número válido.")
        return

    if numero < 1 or numero > len(tarefas):
        print("Tarefa não encontrada.")
        return

    tarefas[numero - 1]["concluida"] = True
    print("Tarefa concluída com sucesso!")


def main():
    """Executa o menu principal do programa."""
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "0":
            print("\nAté logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
