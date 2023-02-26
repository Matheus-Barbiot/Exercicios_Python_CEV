#         INÍCIO.
def escreva(txt):
    a = len(txt) + 4
    print (f'{"~"*a}')
    print (f'  {txt}')
    print (f'{"~"*a}')

#        INFORMAÇÕES.
while True:
    print ('=' * 65)
    TEXTO_OBJ = str (input ('Digite um texto: [@ finaliza] ')).upper()
    if TEXTO_OBJ == '@':
        break
    else:
        escreva(TEXTO_OBJ)

#        FINALIZANDO.        
print ('=' * 65)
print ('Finalizando, obrigado por usar')