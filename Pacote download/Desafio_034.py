salario = float (input ('digite seu salário: '))
if salario > 1250:
    aumento = salario * 10 / 100
    print (f'Seu novo salário é {salario+aumento}.')
else:
    aumento = salario * 15 / 100
    print (f'Seu novo salário é {salario+aumento}.')