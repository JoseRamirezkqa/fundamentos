def funcion (nombre, numeroAtomico,):
    niveles = ["1s2","2s2","2p6","3s2","3p6","4s2","3d10","4p6","5s2","4d10","5p6","6s2","4f14","5d10","6p6","7s2","5f14","6d10","7p6"]
    if numeroAtomico <= 2:
        posicion = 0
    elif numeroAtomico <= 4:
        posicion = 1
        numeroAtomico -= 2
    elif numeroAtomico <= 10:
        posicion = 2
        numeroAtomico -= 4
    elif numeroAtomico <= 12:
        posicion = 3
        numeroAtomico -= 10
    elif numeroAtomico <= 18:
        posicion = 4
        numeroAtomico -= 12
    elif numeroAtomico <= 20:
        posicion = 5
        numeroAtomico -= 18
    elif numeroAtomico <= 30:
        posicion = 6
        numeroAtomico -= 20
    elif numeroAtomico <= 36:
        posicion = 7
        numeroAtomico -= 30
    elif numeroAtomico <= 38:
        posicion = 8
        numeroAtomico -= 36
    elif numeroAtomico <= 48:
        posicion = 9
        numeroAtomico -= 38
    elif numeroAtomico <= 54:
        posicion = 10
        numeroAtomico -= 48
    elif numeroAtomico <= 56:
        posicion = 11
        numeroAtomico -= 54
    elif numeroAtomico <= 70:
        posicion = 12
        numeroAtomico -= 56
    elif numeroAtomico <= 80:
        posicion = 13
        numeroAtomico -= 70
    elif numeroAtomico <= 86:
        posicion = 14
        numeroAtomico -= 80
    elif numeroAtomico <= 88:
        posicion = 15
        numeroAtomico -= 86
    elif numeroAtomico <= 102:
        posicion = 16
        numeroAtomico -= 88
    elif numeroAtomico <= 112:
        posicion = 17
        numeroAtomico -= 102
    elif numeroAtomico <= 118:
        posicion = 18
        numeroAtomico -= 112

    print(f"{nombre}: ", end="")
    for i in range(posicion):
        print(niveles[i], end=" ")

    ultimo = niveles[posicion]
    if len(ultimo) == 3:
        ultimo = ultimo[:-1]
    else:
        ultimo = ultimo[:-2]
    print(f"{ultimo}{numeroAtomico}")

if __name__ == "__main__":
    elementos = []
    numerosAtomicos = []

    while True:
        elemento_name = input("Ingrese el nombre del elemento (para salir ingrese \"Exit\"): ")
        if elemento_name.lower() == "exit":
            break
        numero_atomico = int(input("Ingrese el número atómico: "))
        elementos.append(elemento_name)
        numerosAtomicos.append(numero_atomico)

    for i in range(len(elementos)):
        funcion(elementos[i], numerosAtomicos[i])
