altura = float (input ('Qual a altura da sua parede? '))
largura = float (input ('Qual a largura da sua parede? '))
mq = largura * altura
tinta = mq / 2

print (f'Sua parede tem {mq}m², você precisa de {tinta}L de tinta.')