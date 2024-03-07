while True:
    print("Ingresa la opción \n1.de Celsius a Fahrenheit\n2.de Fahrenheit a Celsius\n3. Finalizar")

    numero = input("Ingrese el número de la opción que desea realizar: ")

    if numero == "1":
        temperatura = int(input(" Temperatura en grados Celsius: "))
        fahrenheit = (temperatura * 9/5) + 32
        print(temperatura, 'Grados Celsius son equivalentes a', fahrenheit, 'grados Fahrenheit\n')
    elif numero == "2":
        temperatura = int(input(" temperatura en grados Fahrenheit: "))
        celsius = (temperatura - 32) * 5/9
        print(temperatura,'Grados Fahrenheit son equivalentes a', celsius, 'grados Celsius.\n')
    elif numero == "3":
        print("Hasta la proxima")
        break
    else:
        print("Ingresa algo valido por favor\n")
        
    