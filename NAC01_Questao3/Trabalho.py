'''Variaveis saparadas'''

idade = int(input("Qual a sua idade: "))

sexo = input("sexo : M/F: ").upper()

civil = input("Você é casado? S/N: ").upper()

'''Estrutura de condição'''

if sexo == "F":
    print("Você terá direito a licença a maternidade")

elif sexo == "M" and idade >= 20 and idade <=39 :
    print("Seu estado é regular")

elif sexo == "M" and idade >=40 and idade <=60:
    print("Você tem direito há Home Office")

else:
    print("Não entendi a sua resposta")