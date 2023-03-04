# Aula 1 - Introdução a python
print('Hello, World!') 
# A função 'print' significa 'imprimir.
# então tudo que estiver depois dela dentro do ( ) ira ser reproduzido na tela.
# No exemplo a cima sera demostrado na tela a seguinte informação: Hello, World!
print(10,20,30,40,50)
# Tambem podemos 'imprimir' diversas informações, como numeros e outros caracteres, como demonstrado com numeros acima.
# A informação que vai aparecer é: 10 20 30 40 50.
# Tambem podemos definir oque ficaria entre uma infomação e outra, utilizando a função (Sep="").
print(10,20,30, sep="-") # Como podem ver foi utilizado sep, e o espaço que aparecia antes
#entre as informações, agora é substituido pelo sinal de (-).
# Podemos adicionar ainda mais informações, como por exemplo (end="")
# que pode nos ajudar quando queremos evidenciar que a linha termina ali.
# para evitar que fique tudo na mesma linha usei (\n)
print(10,20,30, sep='-', end="\n")
print(40,50,60, sep='+')
# Acima vai ser imprimido as seguintes informações
# 10-20-30
# 40+50+60

# Aula avançada

teste1 = 10 == 12   # criei variaveis boolean para agregar no if/elif/else
teste2 = 10 == 11   # que seriam se/se não se / se não
teste3 = 10 == 10   # ele apenas ler oque é verdadeiro, oque é falso ele ignora
teste4 = 10 == 15   

if teste1:
    print('deu certo teste 1')   # Este não vai ler pois vai aparecer falso, pq o valor de teste1 é false.
elif teste2:
    print(' deu certo teste 2')
elif teste3:
    print('deu certo teste 3') 
elif teste4:
    print('deu certo teste4')
else:
    print('nada deu certo')