#Área de login do usuario
login = input("Digite seu login : ")

#Área da senha do usuario
senha = input("Digite sua senha: ")

#Contagem de vezes que ele errou a senha
qtde_errada = 0

#Isso seria o laço de repetiçao para a contagem de erros de senha
while senha!=senha:
    print("Tente mais uma vez ")

#Laço de condição
    if qtde_errada == 3:
        print("Acesso negado")
    else:
        print("Você efetuou o login com sucesso")

#Print da contagem de quantas vezes ele errou
print("Você errou {} vezes".format(qtde_errada))


