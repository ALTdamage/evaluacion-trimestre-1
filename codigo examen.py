print(" -----------------------------------------------------------------------------------")

while True:  # ciclo while sirve para que el programa no coninue hasta que ingrese dato correcto
    try:
        cantidad = int(input("bienvenido al sistema de notas institucionales:\ndigita la cantidad de estudiantes\n"))
        if cantidad > 0:#si la cantidad es mayor a 0 puede continuar
            break
        else:
            print("ingresa un número mayor que 0")#si no ingresa un numero mayor a 0
    except ValueError:#sirve para que cuando ingrese un dato no valido 
        print("por favor inserta un número válido")

for i in range(cantidad):# for es para un ciclo el cual sabemos que tiene un fin, i es la variable que va a ir aumentando de acuerdo a la cantidad
    print("estudiante", i+1)

    while True:#ciclo infinito que funciona siempre y cuando sea verdadero,dato booleano
        nombre = input("|  ingresa el nombre del estudiante:  |\n").strip()#strip sirve para que desaparezcan los espacios en la enrada
        if nombre.isalpha():#sivre para validar si un dato tiene texto
            break#detiene ciclo que esta,para continua con el for
        else:
            print("|  por favor inserta datos validos  |")

    while True:
        try:
            nota = float(input("| ingresa la nota #1: |\n"))
            if 1 <= nota <= 5:
                break
            else:
                print("ingresa un dato entre 1 y 5")
        except ValueError:
            print("ingrese un dato valido")

    while True:
        try:
            nota2 = float(input("| ingresa la nota #2: |\n"))
            if 1 <= nota2 <= 5:
                break
            else:
                print("ingresa un dato entre 1 y 5")
        except ValueError:
            print("ingrese un dato valido")

    while True:
        try:
            nota3 = float(input("| ingresa la nota #3: |\n"))
            if 1 <= nota3 <= 5:
                break
            else:
                print("ingresa un dato entre 1 y 5")
        except ValueError:
            print("ingrese un dato valido")

    promedio = (nota + nota2 + nota3) / 3

    print("\n---------------- RESULTADO ----------------")
    print("Estudiante:", nombre)
    print("Notas:", nota, "--", nota2, "--", nota3)
    print("Promedio:", round(promedio, 2))

    if promedio >= 3:
        print("Resultado: APROBÓ")
    else:
        print("Resultado: NO APROBÓ")

    print("-------------------------------------------\n")
    print("final")