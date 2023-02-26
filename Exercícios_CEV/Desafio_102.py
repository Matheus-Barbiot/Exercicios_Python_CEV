def fatorial(num, calc=False):
    """
    Função de calculo de fatorial

    :num [int] (obrigatorio): indica o numero que fará o fatorial
    :calc [true ou false] (opicional): mostra o calculo de fatoral

    """

    num = 5
    fator = 1

    for n in range(num, 0, -1):
        fator *= n

    if calc == True:
        for n in range(num, 0, -1):
            print(f'{n}', end=' ')
            if n != 1:
                print(f'X', end = ' ')

    else:
        print(f'{num}', end = ' ')
    print(f'= {fator}')




help(fatorial)
