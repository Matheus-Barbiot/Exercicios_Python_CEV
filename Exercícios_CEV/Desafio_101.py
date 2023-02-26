from datetime import date

def voto(ano):
    idade = date.today().year - ano
    voto = str(' ')   
     
    if idade < 16:
        voto = 'NÃO VOTA'
    elif idade < 18 or idade > 60:
        voto = 'VOTO OPICIONAL'
    elif idade >= 18:
        voto = 'VOTO OBRIGATORIO'    
   
    return print (f'Com {idade} anos: {voto}')

    
ANO_N = int (input ('Digite seu ano de nascimento: '))
voto(ANO_N)