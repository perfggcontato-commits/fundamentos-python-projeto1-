import random
numero_computador = random.randint(0, 5)

print ('eu pensei em um numero entre 0 e 5, tente adivinhar qual é')
tentativa = int(input('qual é o seu palpite? '))
if tentativa == numero_computador:
    print('caramba voce acertou!')
else:
    print('tenta a sorte na proxima, o numero era {}'.format(numero_computador))
    

