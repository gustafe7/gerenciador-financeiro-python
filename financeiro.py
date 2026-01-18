 from auditoria import registrar_acao

# Lista que armazena receitas (valores positivos) e despesas (valores negativos)
registros = []

# Carrega os dados salvos anteriormente, se existirem
# Cada linha do arquivo representa um valor financeiro (positivo ou negativo)
try:
    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
            # Converte cada linha do arquivo para float e adiciona à lista de registros
            registros.append(float(linha.strip()))
except FileNotFoundError:
    # Caso o arquivo não exista, o sistema inicia sem registros
    pass


# Loop principal do sistema
# Mantém o programa em execução até o usuário escolher a opção de sair
while True:
    print("\n=== GERENCIADOR FINANCEIRO ===")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Listar registros")
    print("4 - Mostrar saldo")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # REGISTRO DE RECEITA
    # Valores positivos representam entradas financeiras
    if opcao == "1":
        descricao = input("Descrição da receita: ")
        valor_input = input("Valor da receita: ")

        try:
            # Tenta converter o valor informado para número
            valor = float(valor_input)

            # Validação para impedir valores zero ou negativos
            if valor <= 0:
                print("Valor inválido.")
                registrar_acao(
                    "ERRO",
                    f"Valor inválido informado na receita: {valor_input}"
                )
                continue

        except ValueError:
            # Tratamento para valores não numéricos
            print("Valor inválido.")
            registrar_acao(
                "ERRO",
                f"Valor não numérico informado na receita: {valor_input}"
            )
            continue

        # Adiciona a receita à lista de registros
        registros.append(valor)

        # Persiste o valor no arquivo de dados
        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"{valor}\n")

        # Registra a ação no sistema de auditoria
        registrar_acao(
            "RECEITA",
            f"Receita registrada: {descricao} - R$ {valor}"
        )

        print("Receita registrada com sucesso!")


    # REGISTRO DE DESPESA
    # Valores negativos representam saídas financeiras
    elif opcao == "2":
        descricao = input("Descrição da despesa: ")
        valor_input = input("Valor da despesa: ")

        try:
            # Tenta converter o valor informado para número
            valor = float(valor_input)

            # Validação para impedir valores zero ou negativos
            if valor <= 0:
                print("Valor inválido.")
                registrar_acao(
                    "ERRO",
                    f"Valor inválido informado na despesa: {valor_input}"
                )
                continue

        except ValueError:
            # Tratamento para valores não numéricos
            print("Valor inválido.")
            registrar_acao(
                "ERRO",
                f"Valor não numérico informado na despesa: {valor_input}"
            )
            continue

        # Armazena a despesa como valor negativo
        registros.append(-valor)

        # Persiste o valor negativo no arquivo de dados
        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"{-valor}\n")

        # Registra a ação no sistema de auditoria
        registrar_acao(
            "DESPESA",
            f"Despesa registrada: {descricao} - R$ {valor}"
        )

        print("Despesa registrada com sucesso!")


    # LISTAGEM DE REGISTROS
    # Exibe todas as receitas e despesas registradas
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


    # CÁLCULO DE SALDO
    # Soma todas as receitas e despesas
    elif opcao == "4":
        saldo = sum(registros)
        print(f"Saldo atual: R$ {saldo}")


    # ENCERRAMENTO DO SISTEMA
    elif opcao == "5":
        print("Saindo do programa...")
        registrar_acao(
            "ENCERRAMENTO",
            "Sistema financeiro encerrado pelo usuário"
        )
        break


    # TRATAMENTO DE OPÇÃO INVÁLIDA
    else:
        print("Opção inválida.")
        registrar_acao(
            "ERRO",
            f"Opção inválida selecionada: {opcao}"
        )
