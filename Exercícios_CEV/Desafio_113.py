def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Por favor digite um número inteiro VALIDO!\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mERRO! Por favor digite um número real VALIDO!\033[m')
            continue
        else:
            return n


NUM_INT = leiaint('Digite um número inteiro: ')
NUM_REAL = leiafloat('Digite um número real: ')
print(f'O número inteiro foi {NUM_INT} e o número real foi {NUM_REAL}.')