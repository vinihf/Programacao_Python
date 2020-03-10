#Por padrão, os valores são lidos como string
nome = input("Informe seu nome:")
#Quando o valor informado é inteiro, precisa-se converter o valor para int
quantidade = int(input("Informe qual é a quantidade de produtos comprados:"))
#Quando o valor informado é real, precisa-se converter o valor para float
precoUni = float(input("Informe qual é o preço do produto:"))

precoTotal = quantidade*precoUni

print(f'{nome} comprou {quantidade} produtos por R${precoUni} cada. O total gasto foi de R${precoTotal}')
