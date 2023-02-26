frase = str (input ('Digite um palindromo: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverter = juntar[::-1]

if juntar == inverter:
    print ('Esta frase é um palindromo!')
else:
    print ('Esta frase não é um pilindromo!')