from auditoria import registrar_acao

# Lista que armazena receitas (valores positivos) e despesas (valores negativos)
registros = []

# Carrega os dados salvos anteriormente, se existirem
try:
    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
            registros.append(float(linha.strip()))
except FileNotFoundError:
    # Caso o arquivo não exista, o sistema inicia sem registros
    pass


# Loop principal do sistema
while True:
    print("\n=== GERENCIADOR FINANCEIRO ===")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Listar registros")
    print("4 - Mostrar saldo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # RECEITA 
    if opcao == "1":
        descricao = input("Descrição da receita: ")
        valor_input = input("Valor da receita: ")

        try:
            valor = float(valor_input)

            if valor <= 0:
                print("Valor inválido.")
                registrar_acao(
                    "ERRO",
                    f"Valor inválido informado na receita: {valor_input}"
                )
                continue

        except ValueError:
            print("Valor inválido.")
            registrar_acao(
                "ERRO",
                f"Valor não numérico informado na receita: {valor_input}"
            )
            continue

        registros.append(valor)

        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"{valor}\n")

        registrar_acao(
            "RECEITA",
            f"Receita registrada: {descricao} - R$ {valor}"
        )

        print("Receita registrada com sucesso!")


    # DESPESA 
    elif opcao == "2":
        descricao = input("Descrição da despesa: ")
        valor_input = input("Valor da despesa: ")

        try:
            valor = float(valor_input)

            if valor <= 0:
                print("Valor inválido.")
                registrar_acao(
                    "ERRO",
                    f"Valor inválido informado na despesa: {valor_input}"
                )
                continue

        except ValueError:
            print("Valor inválido.")
            registrar_acao(
                "ERRO",
                f"Valor não numérico informado na despesa: {valor_input}"
            )
            continue

        registros.append(-valor)

        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"{-valor}\n")

        registrar_acao(
            "DESPESA",
            f"Despesa registrada: {descricao} - R$ {valor}"
        )

        print("Despesa registrada com sucesso!")


    # LISTAR REGISTROS 
    elif opcao == "3":
        if not registros:
            print("Nenhum registro encontrado.")
        else:
            print("\n--- REGISTROS ---")
            for valor in registros:
                if valor >= 0:
                    print(f"Receita: R$ {valor}")
                else:
                    print(f"Despesa: R$ {abs(valor)}")


    # SALDO 
    elif opcao == "4":
        saldo = sum(registros)
        print(f"Saldo atual: R$ {saldo}")


    # SAIR 
    elif opcao == "5":
        print("Saindo do programa...")
        registrar_acao(
            "ENCERRAMENTO",
            "Sistema financeiro encerrado pelo usuário"
        )
        break


    # OPÇÃO INVÁLIDA 
    else:
        print("Opção inválida.")
        registrar_acao(
            "ERRO",
            f"Opção inválida selecionada: {opcao}"
        )
