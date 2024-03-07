import os
controlBln = True
a = 0
e = 0
i = 0
o = 0
u = 0
total_vocales = 0

while controlBln == True:
    letraStr = (input('Ingresa una variedad de letras\n2.Finalizar\n ->'))
    
    if letraStr == 'a':
            a += 1
            total_vocales += 1
    if letraStr == 'e':
            e += 1
            total_vocales += 1
    if letraStr == 'i':
            i += 1
            total_vocales += 1
    if letraStr == 'o':
            o += 1
            total_vocales += 1
    if letraStr == 'u':
            u += 1
            total_vocales += 1
            os.system('cls')
    if letraStr == '2':
        controlBln = False
        print('Total vocales:', total_vocales)
        print('A: ', a)
        print('E: ', e)
        print('I: ', i)
        print('O: ', o)
        print('U: ', u)