menu = """
====Menu====
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3
while True:
  opcao = input(menu)

  if opcao == "d":
    valor = float(input("Valor do depósito: "))

    if valor >= 0:
      saldo += valor
      extrato += f"Depósito R$ {valor:.2f}\n"
      print("Depósito feito com sucesso!")

    else:
      print("Coloque um valor valido")

  elif opcao == "s":
    saque = float(input("Valor do saque: "))

    excedeu_saldo = saque > saldo
    excedeu_saque = numero_saques >= LIMITES_SAQUES
    excedeu_limite = saque > limite

    if excedeu_saldo:
      print("Saldo insuficiente")
    elif excedeu_saque:
      print("Limite de Saque excedido")
    elif excedeu_limite:
      print("Limite excedido")
    elif saque > 0:
      saldo -= saque
      extrato += f"Saque R$ {saque:.2f}\n"
      numero_saques +=1
      print("Saque feito com sucesso!")
    else:
      print("Operação falhou, informe um valor valido")

  elif opcao == "e":
    print("\n======= EXTRATO =======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print ("=======================")


  elif opcao == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")