# Reto #6 - Edad permitida

"""Pide al usuario que ingrese su edad y mostrarás un mensaje correspondiente si esta coincide con las siguientes condiciones:
Más de 30 años: Nunca es tarde para aprender ¿Qué curso tomaremos?
Entre 29 y 18 años: Es un momento excelente para impulsar tu carrera.
Menos de 18 años: ¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte."""


def main():
    print('-'*40)
    age = int(input('Ingresa tu edad: '))

    if age >= 30:
        print('\nNunca es tarde de aprender ¿Qué curso tomaremos?')
    elif age < 30 and age > 18:
        print('\nEs un momento execelente para impulsar tu carrera')
    elif age <= 18:
        print('\n¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte')
    print('-'*40)


if __name__ == '__main__':
    main()
