registros = []

try:
    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
            registros.append(float(linha.strip()))
except FileNotFoundError:
    pass

while True:
     print("\n=== GERENCIADOR FINANCEIRO===")
     print("1 - registrar receita")
     print("2 - registrar despesa")
     print("3 - listar registros")
     print("4 - mostrar saldos")
     print("5 - sair")

     #gerenciador financeiro criado através de estudos apenas enriquecimento prático e acadêmico
     #pensado para realizar tarefas básicas de registros
     #obrigado pela oportunidade meu Deus!! 

     opcao = input("escolha uma opcao: ")

     if opcao == "1":
        descricao = input("descricao de receita: ")
        valor = float(input("valor da receita: "))
        registros.append(valor)

        # na descricao a informacao "input" faz com que seja seja mostrado um campo para ser preenchido pelo usuario
        # valor tras o valor a ser inserido pelo usuario
        # registros mostra em fomra de numeros??  
        
        with open("dados.txt", "a") as arquivo:
           arquivo.write(f"{valor}\n")
        print("receita registrada com sucesso!")

     elif opcao == "2":
        descricao = input("descricao das despesas: ")
        valor = float(input("valor das despesas: "))
        registros.append(-valor)

        # aqui os campos tem basicamente a mesma funcionalidade do numero 1 
        # difernca está no valor negativo
        
        with open("dados.txt", "a") as arquivo:
           arquivo.write(f"{-valor}\n")
        print("despesa registrada com sucesso!")
        
     elif opcao == "3":
        if not registros:
            print("nenhum registro encontrado")
        else:
            print("\n--- REGISTROS---")
            for valor in registros:
                if valor >= 0:
                    print(f"receitas: R$ {valor}")
                else:
                    print(f"despesas: R$ {abs(valor)}")

       # aqui é mostrado o registro de cada campo preenchido de forma subsequente da ordem que foi feita
     
     elif opcao == "4":
        saldo = sum(registros)
        print(f"saldo atual: R$ {saldo}")

       # funcao que calcula e demonstra o saldo exato quando os valores das receitas e despesas sao preenchidos 

     elif opcao == "5":
        print("saindo do programa...")
        break
       # funcao para encerrar o programa
     
     else:
        print("opcao invalida")
