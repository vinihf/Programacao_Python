#Neste caso, o programa irá imprimir apenas uma vez "Bom dia!"
#Caso nosso objetivo fosse imprimir 5 vezes a mensagem seriam necessários 5 impressões.

repeticao = 0
if repeticao < 5:
    print('Bom dia! (sem estrutura de repetição)')
    repeticao = repeticao + 1


#Aqui, ao usar a estrutura de repetição while, vemos um resultado diferente.

repeticao = 0
while repeticao < 5:
    print('Bom dia! (com estrutura de repetição while)')
    repeticao = repeticao + 1

#O mesmo resultado pode ser observado ao utilizar a estrutura de repetição for.

for repeticao in range(0,5):
    print('Bom dia! (com estrutura de repetição for)')
