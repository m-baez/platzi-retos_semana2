# Reto #3 - Rangos cambiantes.

"""Nuevamente pide a tu usuario que indique 3 números: un límite superior, un límite inferior y uno de comparación. Si el número de comparación se encuentra entre los 2 primeros, comunicarlo en pantalla. En caso estar por debajo del límite inferior o por arriba del límite superior, también mostrarlo en pantalla."""


def main():
    print('-'*50)
    upperLimit = int(
        input('Escribe un número para indicar un límite superior: '))
    lowerLimit = int(
        input('Ahora otro número que sirva para el límite inferior: '))
    compare = int(input('Este otro número va a comparar los dos límites: '))

    if compare < lowerLimit:
        print('\nLo siento, estás por debajo del límite permitido')
    elif compare > upperLimit:
        print('\nLo siento, estás por encima del límite permitido')
    else:
        print('\nExcelente, estás dentro del límite')
    print('-'*50)


if __name__ == '__main__':
    main()
