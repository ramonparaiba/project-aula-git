# Task CLI

O **Task CLI** é um pequeno gerenciador de tarefas executado no terminal. Com ele, é possível cadastrar, listar e concluir tarefas durante a execução do programa.

## Objetivo

Este projeto foi criado para uma aula prática de Git e GitHub. O código é propositalmente pequeno e simples, para que estudantes iniciantes possam entendê-lo e implementar melhorias usando Fork, branches, commits e Pull Requests.

As tarefas ficam armazenadas apenas na memória. Por isso, elas são apagadas quando o programa é encerrado.

## Requisitos

- Python 3.8 ou superior.
- Um terminal para executar os comandos.
- Git, caso você queira realizar a atividade da aula.

O projeto não utiliza bibliotecas externas.

## Como executar o projeto

Entre na pasta do projeto e execute:

```bash
python main.py
```

Em alguns sistemas, o comando pode ser:

```bash
python3 main.py
```

## Exemplo de execução

```text
=== TASK CLI ===

1 - Listar tarefas
2 - Adicionar tarefa
3 - Concluir tarefa
0 - Sair

Escolha uma opção: 2

Digite a descrição da tarefa: Estudar Git
Tarefa adicionada com sucesso!

Escolha uma opção: 1

Tarefas:
1 - [ ] Estudar Git

Escolha uma opção: 3

Tarefas:
1 - [ ] Estudar Git

Digite o número da tarefa concluída: 1
Tarefa concluída com sucesso!

Tarefas:
1 - [x] Estudar Git
```

## Estrutura do projeto

```text
task-cli/
├── README.md
├── .gitignore
├── main.py
└── requirements.txt
```

- `main.py`: contém o código do gerenciador de tarefas.
- `README.md`: apresenta o projeto e explica como utilizá-lo.
- `.gitignore`: informa ao Git quais arquivos não devem ser versionados.
- `requirements.txt`: informa que não há dependências externas.

## Atividade da aula

Nesta atividade, cada aluno deverá:

1. Fazer um **Fork** deste projeto no GitHub.
2. Clonar o próprio Fork para o computador.
3. Criar uma branch para desenvolver uma pequena melhoria.
4. Alterar o código e testar o programa.
5. Fazer um commit com a alteração.
6. Enviar a branch para o próprio Fork no GitHub.
7. Abrir um **Pull Request** para o projeto original.

Comandos básicos para realizar a atividade:

```bash
git clone URL_DO_SEU_FORK
cd task-cli
git switch -c minha-melhoria
git add .
git commit -m "Adiciona melhoria"
git push -u origin minha-melhoria
```

Algumas sugestões de melhorias:

- adicionar uma opção para excluir uma tarefa;
- limpar todas as tarefas concluídas;
- contar quantas tarefas estão pendentes;
- melhorar a apresentação das tarefas;
- adicionar uma prioridade para cada tarefa;
- exibir uma mensagem de boas-vindas;
- adicionar uma nova opção ao menu.
