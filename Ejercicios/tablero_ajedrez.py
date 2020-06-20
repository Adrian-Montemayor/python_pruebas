
cuadro1 = "[X]"
cuadro2 = "[O]"

print("##### Tablero de Ajedrez #####")

for filas in range(0,8):
    print("")
    for columnas in range(0,8):
        if filas % 2 == 0:
            if columnas % 2 == 0:
                print(cuadro2, end=" ")
            else:
                print(cuadro1, end=" ")
        else:
            if columnas % 2 == 0:
                print(cuadro1, end=" ")
            else:
                print(cuadro2, end=" ")