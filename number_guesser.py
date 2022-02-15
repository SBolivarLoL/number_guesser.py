import random

número_aleatorio = random.randint(0, 21)
contador = 0
print('Tienes que adivinar el número del 0 al 20.\n' '¡Buena suerte!')
while True:
    contador += 1
    num_jugador = input('Intenta adivinar el número: ')
    if num_jugador.isdigit():
        num_jugador = int(num_jugador)
    else:
        print('Debe ser un número la próxima vez.')
        continue

    if num_jugador == número_aleatorio:
        print('¡Lo adivinaste!')
        break
    elif num_jugador > número_aleatorio:
        print('El número es más pequeño!')
    else:
        print('El número es más grande!')

print('Y solo en', contador, 'oportunidades;).')
