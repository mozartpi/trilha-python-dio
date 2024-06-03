from datetime import datetime
menu = """
########## MENU ##########
     
     [d] Depositar
     [s] Sacar
     [e] Extrato
     [q] Sair

########## MENU ##########
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor):
    if valor > 0:
        return valor
    else:
        return 0

def saque(valor):
    if valor > 0:
        return valor
    else:
        return 0
    
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo += deposito(valor)
        if(deposito(valor)):
            data = datetime.now()
            extrato += f"Depósito: R$ {valor:.2f}               {data}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= saque(valor)
            data = datetime.now()
            extrato += f"Saque:    R$ {valor:.2f}               {data}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
