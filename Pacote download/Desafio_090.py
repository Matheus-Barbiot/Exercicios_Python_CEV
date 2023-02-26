#            INICIO.
DICE_STUDENT = {}

#        DADOS.
DICE_STUDENT['nome'] = str (input ('Nome: '))
DICE_STUDENT['media'] = float (input (f'Media do aluno {DICE_STUDENT["nome"]}: '))

#        STUDENT SITUATION.
if DICE_STUDENT['media'] >= 6:
    DICE_STUDENT['situação'] = 'aprovado'
else:
    DICE_STUDENT['situação'] = 'reprovado'

#        FINALIZATION.
print ('=' * 50)
print (f'NOME: {DICE_STUDENT["nome"]} ')
print (f'MEDIA: {DICE_STUDENT["media"]}' )
print (f'O aluno foi {DICE_STUDENT["situação"]} ')