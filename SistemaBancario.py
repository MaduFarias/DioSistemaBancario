def Opcoes():
    print(
        '''
        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Sair
        '''
    )


def Deposito(deposito): #A variavel vai ser tratada na função, mas o valor tem que ser declarado onde será usado.
    while True:
        if (deposito > 0):
            return deposito #não pode break após return 

def Saque(saque):
    if (saque > 0 and saque <= 500):
        return saque
    else: 
        while True:
            saque = float(input("Digite valor a ser sacado(max R$500):"))
            if (saque > 0 and saque <= 500):
                return saque
            else: 
                continue
    

def ExtratoD(*, depositoE,): #Passar como uma **kwargs para lista
    i = 0
    for i in depositoE: 
        print(i)

def ExtratoS(*, saqueE):
    j = 0
    for j in saqueE:
        print(j)

def operacao():
    depositlist = []
    saquelist = []
    total = 0.0
    saquesoma = 0
    
    while True:
        Opcoes()
        operacao = int(input("Selecione uma opção "))

        if (operacao == 1):
            deposito = float(input("Digite o valor a ser depositado: "))
            valordeposilist = Deposito(deposito)
            depositlist.append(valordeposilist) 
            total += valordeposilist

        elif (operacao == 2):
            if (len(saquelist) == 3):
                print("Limite de saques atingido, tente outra operação")

            else:
                saque = float(input("Digite o valor a ser sacado: "))
                valorsaquelist = Saque(saque)
                somasaque = valorsaquelist

                if (total < somasaque):
                    print(f"Falha na operação saldo insuficiente \nValor na conta R${total}")
                    continue

                else: 
                    saquelist.append(-valorsaquelist)
                    total -= valorsaquelist

        elif (operacao == 3):
            #SE = ExtratoS(saqueE=saquelist)

            print("\nExtrato \nDepositos realizados: ")
            ExtratoD(depositoE=depositlist)

            if (saquelist):
                print("Saques: ")
                ExtratoS(saqueE=saquelist)

            else:
                continue

            print(f"Valor restante: \nR${total}")
            

        elif (operacao == 4):
            print("Obrigada por usar nossos serviços! Operação encerrada")
            break

        else:
            print("Operação inválida, tente novamente")

operacao()