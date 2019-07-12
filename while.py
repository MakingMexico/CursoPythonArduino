loop = True

while loop:
    number = int(input('Ingrese un numero: '))
    if number > 5:
        print('El numero ingresado es mayor a 5')
    elif number == 5:
        print('El numero ingresado es 5')
    else:
        print('El numero ingresado es menor a 5')
        loop = False
