base = 1
baseArray = []
exponenteArray = []
while base >= 1:
    base = int(input("Ingrese el valor para la base: "))
    exponente = int(input("Ingrese el exponente: "))
    if(base <= 100 and exponente <= 10**9):
        baseArray.append(base)
        exponenteArray.append(exponente)
    else:
        print("El valor ingresado no es valido")
for i, elem in enumerate(baseArray):
    print(elem, exponenteArray[i])