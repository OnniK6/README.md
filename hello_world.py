def main():

    lista = []

    counter = 0

    monta = int(input("Monta numeroa: "))

    while counter < monta:

        numero = int(input(""))

        counter += 1

        lista.append(numero)


    print(lista)


if __name__ == '__main__':
    main()