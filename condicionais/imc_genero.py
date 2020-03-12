altura = float(input("Informe a altura:"))
opcao = input("M (masculino) F (feminino)")
opcao = str.upper(opcao)
if opcao == "M":
    peso = (72.7*altura) - 58
    referencia = "masculino"
else:
    peso = (62.1*altura)-44.7
    referencia = "feminino"
print(f'O  peso ideal para o sexo {referencia} é {peso:.2f} .')
