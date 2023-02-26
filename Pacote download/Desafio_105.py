def nota(*n, sit=False):
    num = {}
    num['total'] = len(n)
    num['maior'] = max(n)
    num['menor'] = min(n)
    num['media'] = sum(n)/len(n)
    if sit == True:
        if num['media'] > 7:
            num['situação'] = 'boa'
        else:
            num['situação'] = 'ruim'
    return print(num)

nota(10, 8, 9, sit=True)