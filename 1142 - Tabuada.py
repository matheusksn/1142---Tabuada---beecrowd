##Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada de N de 1 até 10.

##Entrada

##Um número natural N (0 <= N <= 10).

##Saída

##Exibir a tabuada do valor dado na entrada, conforme o modelo de saída dos exemplos


n = int(input())
tabuada = int(0)

while tabuada < 10:
    tabuada += 1
    print('{} x {} = {}'.format(n , tabuada , n * tabuada))

