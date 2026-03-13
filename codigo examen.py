print(" -----------------------------------------------------------------------------------")

while True:  # ciclo while que evita que el programa continúe si el dato es incorrecto
    try:
        cantidad = int(input("bienvenido al sistema de notas institucionales:\ndigita la cantidad de estudiantes\n"))
        if cantidad > 0:
            break
        else:
            print("ingresa un número mayor que 0")
    except ValueError:
        print("por favor inserta un número válido")

for i in range(cantidad):
    print("estudiante", i+1)

    while True:
        nombre = input("|  ingresa el nombre del estudiante:  |\n").strip()
        if nombre.isalpha():
            break
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