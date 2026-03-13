print(" -----------------------------------------------------------------------------------")
cantidad=int(input(" bienvenido a el sistema de notas institucionales: \ndigita la cantidad de estudiantes \n"))
for i in range(cantidad):
    print("estudiante    ",i+1)
    while True:
        nombre=input("|  ingresa el nombre del estudiante:  |\n")
        if nombre.isalpha():
            break
        else:
            print("|  por favor inserta datos validos  |")    
    while True:
        try:
            nota=float(input("|ingresa la nota #1:  |\n"))
            if 1<=nota<=5:
                break
            else:
                print("ingresa un dato entre 1-5")
        except ValueError:
            print("ingrese un dato valido")
    while True:
        try:
            nota2=float(input("ingresa la nota #2:\n"))
            if 1<=nota<=5:
                break
            else:
                print("ingresa un dato entre 1-5")
        except ValueError:
            print("ingrese un dato valido")
    while True:
        try:
            nota3=float(input("ingresa la nota #3:\n"))
            if 1<=nota<=5:
                break
            else:
                print("ingresa un dato entre 1-5")
        except ValueError:
            print("ingrese un dato valido")
print("el recuento de notas fue\n",nota,"\n",nota2,"\n",nota3,"\n",)
promedio=(nota+nota2+nota3)/3


            
