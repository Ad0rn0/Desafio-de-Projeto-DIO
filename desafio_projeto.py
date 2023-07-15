menu = '''Bem vindo ao SeuBanco.
Digite os valores referentes à opção que você deseja fazer:
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair
'''
balance = 0
statement = ""
WITHDRAWAL_QUANTITY_LIMIT = 3
WITHDRAWAL_VALUE_LIMIT = 500
daily_draft = 0

while True:

    option = str(input(menu))

    # The user chose to leave
    if option == "4":
        print("\nAté a próxima")
        break

    # The user chose to deposit
    elif option == "1":
        deposit = float(input("\nDigite o valor do seu depósito: "))

        if deposit <= 0:
            print("\033[31m")  # Red
            print("\nQuantidade inválida. Depósito não pode ser menor ou igual a zero!\n")
            print("\033[0m")  # Reset
        else:
            balance += deposit
            statement += f"Depósito de R${deposit:.2f}\n"
            print("\033[32m")  # Green
            print("Depósito Efetuado com sucesso!")
            print("\033[0m")  # Reset

    # The user chose to draft
    elif option == "2":
        draft = float(input("Digite o valor que deseja sacar: "))

        if draft <= 0:
            print("\033[31m")  # Red
            print("\nQuantidade inválida. Saque não pode ser menor ou igual a zero!\n")
            print("\033[0m")  # Reset

        else:
            if draft > balance:
                print("\033[31m")  # Red
                print(
                    f"\nO valor informado para saque é maior que o saldo atual da sua conta.\nSaldo atual = R${balance:.2f}\n")
                print("\033[0m")  # Reset

            elif draft <= balance:
                if draft <= WITHDRAWAL_VALUE_LIMIT:
                    if daily_draft != WITHDRAWAL_QUANTITY_LIMIT:
                        balance -= draft
                        statement += f"Saque de R${draft:.2f}\n"
                        print("\033[32m")  # Green
                        print("Saque efetuado com sucesso!")
                        print("\033[0m")  # Reset
                        daily_draft += 1
                    else:
                        print("\033[31m")  # Red
                        print(
                            f"\nVocê excedeu o limite de saques por hoje, volte amanhã\n")
                        print("\033[0m")  # Reset
                else:
                    print("\033[31m")  # Red
                    print(f"\nVocê excedeu o limite de R$ 500,00 por saque.\n")
                    print("\033[0m")  # Reset

    elif option == "3":
        print(
            f"\nNão foram realizadas movimentações de saldo\nSaldo atual: R${balance}\n" if not statement else f"\nO extrato da sua conta é:\n{statement}\nSaldo atual: R${balance}\n")

    else:
        print("\nOpção inválida. Tente novamente.\n")
