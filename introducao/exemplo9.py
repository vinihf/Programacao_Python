qtdProd = 10
precProd = 4.33

#Print padrão, concatena as informações como elas são por meio da vírgula
print("Quantidade = ",qtdProd,"\nPreço = R$",precProd)

#Print formatado, versão atual do print
print(f'Quantidade = {qtdProd:2} \nPreço = R$ {precProd:3.2f}')

#Função format da String, substitui pelos argumentos informados
print("Quantidade = {0:2d}\nPreço = R$ {1:2.2f}".format(qtdProd,precProd))
