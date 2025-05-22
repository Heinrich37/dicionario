print("1 - Para iniciar o cadastro \n2 - Para sair")
cadastro = int(input("Escolha uma opçao: "))

if cadastro == 1:
    nome = input("Informe seu nome: ")
    sobre_nome = input("Informe seu Sobrenome: ")
    rg = input("Informe seu RG: ")
    cpf = input("Informe seu CPF: ")
    endereço = input("Informe seu endereço: ")
    telefone = input("Informe seu telefone: ")
    idade = input("Informe sua idade: ")
    print("")
    passagem = (input("Digite (Sim) para continuar:\n")).lower
    
    if passagem == "sim":
        destino = (input("Informe o destino que deseja: "))
        origem = (input("Informe a origem: "))
        duraçao = (input("Informe a duração do voo: "))
        valor_passagem = (input("Informe o valor da passagem: "))
        valor_passagem = valor_passagem * 0.05 - valor_passagem
        print(f"Valor da passagem com desconto de 5% {valor_passagem}")
        #desconto de 5%
        
elif cadastro == 2:
    print("Voçe saiu do programa!!!")


    