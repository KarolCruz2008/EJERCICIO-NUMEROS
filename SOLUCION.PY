frecuencia = [0] * 10

while True:
    print("\n    MENÚ    ")
    print("1. Ingresar Número Del 0 Al 9")
    print("2. Mostrar Números No Elegidos")
    print("3. Ver Apariciones De Cada Número")
    print("4. Ver Media De Apariciones")
    print("5. Números Más Frecuentes")
    print("6. Números Menos Frecuentes")
    print("7. Diferencia Entre Pares E Impares")
    print("8. Total De Apariciones")
    print("9. Salir")

    opcion = input("Seleccione una opción entre el 1 y 9: ")

    if opcion == '1':
        entrada = input("Ingrese Un Número Del 0 Al 9: ")
        try:
            numero = int(entrada)
            if 0 <= numero <= 9:
                frecuencia[numero] += 1
                print("Número", numero, "registrado.")
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada no válida.")

    elif opcion == '2':
        no_elegidos = [0] * 10  # lista fija
        indice = 0
        for i in range(10):
            if frecuencia[i] == 0:
                no_elegidos[indice] = i
                indice += 1
        if indice > 0:
            print("Números no elegidos:", no_elegidos[:indice])
        else:
            print("Todos los números han sido elegidos al menos una vez.")

    elif opcion == '3':
        print("Apariciones por número:")
        for i in range(10):
            print("Número", i, ":", frecuencia[i], "veces")

    elif opcion == '4':
        total = 0
        for f in frecuencia:
            total += f
        media = total / 10
        print("Media de apariciones:", round(media, 2))

    elif opcion == '5':
        max_valor = 0
        for f in frecuencia:
            if f > max_valor:
                max_valor = f
        if max_valor == 0:
            print("Ningún número ha sido ingresado.")
        else:
            resultado = [0] * 10
            indice = 0
            for i in range(10):
                if frecuencia[i] == max_valor:
                    resultado[indice] = i
                    indice += 1
            print("Números más frecuentes:", resultado[:indice], "con", max_valor, "apariciones")

    elif opcion == '6':
        min_valor = None
        for f in frecuencia:
            if f > 0:
                if min_valor is None or f < min_valor:
                    min_valor = f
        if min_valor is None:
            print("Ningún número ha sido ingresado.")
        else:
            resultado = [0] * 10
            indice = 0
            for i in range(10):
                if frecuencia[i] == min_valor:
                    resultado[indice] = i
                    indice += 1
            print("Números menos frecuentes:", resultado[:indice], "con", min_valor, "apariciones")

    elif opcion == '7':
        pares = 0
        impares = 0
        for i in range(10):
            if i % 2 == 0:
                pares += frecuencia[i]
            else:
                impares += frecuencia[i]
        print("Apariciones pares:", pares)
        print("Apariciones impares:", impares)

    elif opcion == '8':
        total = 0
        for f in frecuencia:
            total += f
        print("Total de apariciones registradas:", total)

    elif opcion == '9':
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")