# Reto #2 - En el rango, por favor.

"""Pide al usuario que indique 2 números: uno que servirá como límite y otro para comparar. Si el segundo número es menor al primero, mostrarás un mensaje diciendo “El número ‘x’ se encuentra en el rango, gracias” y en caso contrario dirá “El número ‘x’ excede el límite permitido”."""


def main():
    print('-'*50)
    limit = int(input('Escribe un número que servirá como límite: '))
    compare = int(input('Escibe otro número que servirá para comparar: '))

    if compare <= limit:
        print('El número %d se encuentra en el rango, gracias' % compare)
    else:
        print('El número %d excede el límite permitido' % compare)
    print('-'*50)


if __name__ == '__main__':
    main()
