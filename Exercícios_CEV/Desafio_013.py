s = float(input('Qual o seu salário? R$'))
a = int(input('Qual o seu aumento? '))
aus = s * a /100

print(f'Seu salario com {a}% de aumento é de R${s+aus:.2f}.')