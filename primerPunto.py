def comprobar(numero):
    suma = 0
    arrayNumber = list(numero)
    for i, elem in enumerate(arrayNumber):
        if i != len(arrayNumber) -1: 
            print(elem, "+", end=' ')
        else:
            print(elem, "=", end=' ')
        suma += int(elem)
    print(suma)
opcion = 0
numbersArray = []
while opcion >= 0:
    opcion = int(input('Ingrese el número: '))
    if opcion >= 0:
        numbersArray.append(opcion)
for elem in numbersArray:
    comprobar(str(elem))    
