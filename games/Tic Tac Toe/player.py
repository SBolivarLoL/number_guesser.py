import math
import random 
class Player: #creamos una clase llamada Player para definir los jugadores en general y luego usar inheritance para crear jugadores humanos y  de computadora
    def __init__(self, letter): #así podemos crear las clases específicas sin mucho trabajo
        #la letra será x u o
        self.letter = letter #asignamos el atributo letter
    
    #queremos que el jugador tenga su sigiente movimiento después de cada juego
    def get_move(self, juego):
        pass

class RandomComputer_player(Player):
    def __init__(self, letter): #usamos inheritance para tomar los atributos de la clase Player
        super().__init__(letter)

    def get_move(self, juego):
        # sacar un lugar aleatorio válido para nuestro siguiente movimiento
        cuadro = random.choice(juego.posibles_movimientos())
        return cuadro

class Human_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, juego):
        cuadro_valido = False
        val = None
        while not cuadro_valido:
            cuadro = input(self.letter + 's juegan. Introduce una jugada (0-8):')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(cuadro)
                if val not in juego.posibles_movimientos():
                    raise ValueError
                cuadro_valido = True
            except ValueError:
                print('Cuadro inválido. Vuelve a intentarlo.')

        return val

