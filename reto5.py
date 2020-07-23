# Reto #5 - ¿Cómo está el clima?

"""Crea un programa que pregunte al usuario si está lloviendo, en caso de responder “sí” pregunta si está haciendo mucho viento y si responde “sí” nuevamente muestra un mensaje indicando que hace mucho viento para salir con una sombrilla. En caso contrario, anima al usuario a que lleve una sombrilla. Para el caso de responder “no” en la primer pregunta, entonces solo desea un bonito día.
Considera que las respuestas pueden pasarse a minúsculas para evitar posibles errores."""


def main():
    print('-'*40)
    rain = str(input('¿Está lloviendo ahora? ').lower())

    if rain == 'si':
        wind = str(input('¿Está haciendo mucho viento? '))
        if wind == 'si':
            print('\nHay mucho viento para salir con una sombrilla')
        else:
            print('\nSería bueno que llevaras una sombrilla')
    elif rain == 'no':
        print('\nOk, pasa un bonito día')
    print('-'*40)


if __name__ == '__main__':
    main()
