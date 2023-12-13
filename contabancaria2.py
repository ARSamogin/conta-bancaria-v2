from random import randint


def menu():
  LIMITE_SAQ = 3
  AGENCIA = "0001"

  saldo = 0
  extrato = ""
  limite_valor = 500
  num_saq = 0
  Usuarios = []
  Contas_corrente = []

  while True:
    opcao = int(
      input(
        "Escolha uma opção abaixo: \n 1-Depósito \n 2-Saque \n 3-Extrato \n 4-Sair \n 5-Cadastrar usuário \n 6-Nova conta corrente \n 7-Listar contas \n Escolha a opção:"
      ))

    if opcao == 1:
      dep = float(input("Digite o valor a ser depositado:"))
      saldo, extrato = deposito(saldo, dep, extrato)

    elif opcao == 2:
      saq = float(input("Digite o valor a ser sacado:"))
      saldo, extrato = saque(saldo=saldo,
                             num_saq=num_saq,
                             extrato=extrato,
                             saq=saq,
                             LIMITE_SAQ=LIMITE_SAQ,
                             limite_valor=limite_valor)

    elif opcao == 3:
      consulta_extrato(saldo, extrato)

    elif opcao == 4:
      print("Obrigado pela preferência")

    elif opcao == 5:
      cadastro_usuario(Usuarios)

    elif opcao == 6:
      num_conta = randint(111111, 999999)
      nova_conta = conta_corrente(AGENCIA, Usuarios, num_conta)
      if nova_conta:
        Contas_corrente.append(nova_conta)

    elif opcao == 7:
      print(Contas_corrente)

    else:
      print("Opção inexistente")


def deposito(saldo, dep, extrato, /):
  saldo += dep
  extrato += f"Depósito de R$ {dep :.2f} \n"
  return saldo, extrato


def saque(*, saldo, saq, LIMITE_SAQ, limite_valor, extrato, num_saq):
  if saq > saldo:
    print("Saldo Insuficiente")
  elif saq > limite_valor:
    print("Valor acima do limite permitido")
  elif num_saq > LIMITE_SAQ:
    print("Operação negada, limite diário de saques excedido")
  elif saq < 500 and num_saq < LIMITE_SAQ and saq <= 500:
    saldo -= saq
    num_saq += 1
    extrato += f"Saque de R$ {saq :.2f} \n"
    print(f"Saque realizado com sucesso, seu novo saldo é de {saldo} reais")
  return saldo, extrato


def consulta_extrato(saldo, /, extrato):
  print(extrato)
  print((f'Seu saldo atual é de {saldo} reais'))


def cadastro_usuario(Usuarios):
  cpf = int(input("Por favor, insira seu CPF, somente números:"))
  user = filtro_users(cpf, Usuarios)
  if user:
    print("Usuário já cadastrado! \n")
    return

  else:
    nome = str(input("Informe seu nome completo:"))
    data_nasc = input("informe sua data de nascimento com o ano completo:")
    endereco = input(
      "Informe seu endereço com logradouro, número e complemento, bairro, cidade  e estado:"
    )
    dicionario = {
      "Nome": nome,
      "Data de Nascimento": data_nasc,
      "Endereço": endereco,
      "CPF": cpf
    }
    Usuarios.append(dicionario)
    print("Cadastro concluído com sucesso!")


def filtro_users(cpf, Usuarios):
  user = [user for user in Usuarios if user["CPF"] == cpf]
  return user


def conta_corrente(AGENCIA, Usuarios, num_conta):
  cpf = int(input("Informe o CPF do usuário (somente números)"))
  user = filtro_users(cpf, Usuarios)
  if user:
    print("Conta criada com sucesso!")
    return {
      "Agência": AGENCIA,
      "Numero da conta": num_conta,
      "Usuário": Usuarios
    }
  else:
    print(
      "Usuário não encontrado, realize seu cadastro antes de criar sua conta corrente"
    )


def lista_contas(Contas_corrente):
  for conta in Contas_corrente:
    print(f'Agência: {conta["Agência"]}\n'
          f'Número da conta: {conta["Numero da conta"]}\n'
          f'Usuário: {conta["Usuarios"]["dicionario"]["Nome"]}\n')


menu()
