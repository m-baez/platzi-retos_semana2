# Reto #1 - Número mayor y menor

"""Escribe un programa que pida al usuario 2 números, mostrando como salida cuál es el número mayor y la diferencia de uno respecto al otro. En caso de que los números sean iguales, mostrarlo también en pantalla."""


def main():
    print('-'*50)
    n1 = int(input('Escribe un número y da ENTER: '))
    n2 = int(input('Escribe otro número y da ENTER: '))
    res1 = n2 - n1
    res2 = n1 - n2

    if n1 == n2:
        print('Los dos números son iguales')
    elif n1 < n2:
        print('El número %d es mayor a %d y tiene una diferencia de %d' %
              (n2, n1, res1))
    else:
        print('El número %d es mayor a %d y tiene una diferencia de %d' %
              (n1, n2, res2))
    print('-'*50)


if __name__ == '__main__':
    main()
