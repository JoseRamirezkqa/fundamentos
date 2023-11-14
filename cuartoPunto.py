def division(numero):
    unidades = numero % 10
    numero //= 10
    decenas = numero % 10
    numero //= 10
    centenas = numero % 10
    numero //= 10
    miles = numero % 10
    numero //= 10

    if miles == 1:
        print("M", end="")
    elif miles == 2:
        print("MM" , end="")
    elif miles == 3:
        print("MMM" , end="")
    elif miles == 4:
        print("MV" , end="")
    elif miles == 5:
        print("V" , end="")
    if centenas == 1:
        print("C" , end="")
    elif centenas == 2:
        print("CC" , end="")
    elif centenas == 3:
        print("CCC" , end="")
    elif centenas == 4:
        print("CD" , end="")
    elif centenas == 5:
        print("D" , end="")
    elif centenas == 6:
        print("DC" , end="")
    elif centenas == 7:
        print("DCC" ,end="")
    elif centenas == 8:
        print("DCCC" , end="")
    elif centenas == 9:
        print("CM" , end="")
    if decenas == 1:
        print("X" , end="")
    elif decenas == 2:
        print("XX" , end="")
    elif decenas == 3:
        print("XXX" , end="")
    elif decenas == 4:
        print("XL" , end="")
    elif decenas == 5:
        print("L" , end="")
    elif decenas == 6:
        print("LX" ,end="")
    elif decenas == 7:
        print("LXX" , end="")
    elif decenas == 8:
        print("LXXX" ,end="")
    elif decenas == 9:
        print("XC" , end="")
    if unidades == 1:
        print("I" , end="")
    elif unidades == 2:
        print("II" , end="")
    elif unidades == 3:
        print("III" , end="")
    elif unidades == 4:
        print("IV", end="")
    elif unidades == 5:
        print("V" , end="")
    elif unidades == 6:
        print("VI" , end="")
    elif unidades == 7:
        print("VII" , end="")
    elif unidades == 8:
        print("VIII" , end="")
    elif unidades == 9:
        print("IX", end="" )

    print()

def main():
    n = 1
    i = 0
    romanos = []

    print("Todo número que ingreses se convertirá en romano")

    while n != 0:
        try:
            n = int(input("Ingresa un valor positivo para n. Si deseas finalizar, introduce el número cero: "))
            if 0 < n <= 5000:
                romanos.append(n)
                i += 1
            elif n < 0 or n >= 5000:
                print("El número ingresado es incorrecto. Por favor, ingresa un valor válido.")
        except ValueError:
            print("Por favor, ingresa un valor numérico.")

    for j in range(i):
        division(romanos[j])
if __name__ == "__main__":
    main()