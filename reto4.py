# Reto #4 - “I like turtles”

"""Escribe un programa que pida al usuario ingrese su animal favorito, si coloca ‘Tortuga’, ‘tortuga’, ‘TORTUGA’ o cualquier otra variante de la palabra entonces mostrar en pantalla “También me gustan las tortugas”. En caso contrario mostrar el mensaje “Ese animal es genial, pero prefiero las tortugas”."""


def main():
    print('-'*50)
    favoriteAnimal = str(input('Escribe cual es tu animal favorito: '))

    if favoriteAnimal == 'Tortuga' or favoriteAnimal == 'tortuga' or favoriteAnimal == 'TORTUGA':
        print('También me gustan las tortugas')
    else:
        print('Ese animal es genial (%s), pero prefiero las tortugas' %
              favoriteAnimal)
    print('-'*50)


if __name__ == '__main__':
    main()
