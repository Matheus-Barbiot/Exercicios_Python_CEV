#             INICIO.
NAME_STUDENTS = []
ALL_NOTES = []
ALL_AVERAGES = []
GRADES = []

#            OBJETOS NESSESSARIOS.
while True:
    NAME_STUDENTS.append (str (input ('Nome do aluno: ')))
    GRADES.append (int (input ('Primeira nota: ')))
    GRADES.append (int (input ('segunda nota: ')))
    
#            APROPRIANDO LISTAS.
    AVERAGE = (GRADES[0] + GRADES[1]) / 2
    ALL_AVERAGES.append(AVERAGE)
    ALL_NOTES.append(GRADES[:])
    GRADES.clear()
    
#            ESCOLHENDO CONTINUAR.
    print ('=' * 30)
    CONTINUE = str (input ('Continuar? '))
    print ('=' * 30)
    if CONTINUE == 'não':
        break

#            BOLETIM.
print (f'No:          ALUNO:      MEDIAS:')
print ('-' * 30)
for S in range (0, len (NAME_STUDENTS)):
    print (f'Aluno n{S}:    {NAME_STUDENTS[S]:^7}{"|":>5}{ALL_AVERAGES[S]:^5}')
   
#            VISUALIZANDO NOTAS. 
while True:
    CONTINUE_2 = int (input ('Deseja ver a nota de algum aluno? [999 finaliza] '))
    print ('-' * 30)
    if CONTINUE_2 == 999:
        break
    else:
        print (f'As notas de {NAME_STUDENTS[CONTINUE_2]} foram {ALL_NOTES[CONTINUE_2]}.')
        print ('-' * 30)

#            FINALIZAÇÃO.
print ('Programa finalizado, obrigado por usar.')