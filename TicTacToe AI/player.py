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
        cuadro = random.choice(juego.movimientos_disponi())
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
                if val not in juego.movimientos_disponi():
                    raise ValueError
                cuadro_valido = True
            except ValueError:
                print('Cuadro inválido. Vuelve a intentarlo.')

        return val

class ComputadoraInteligente(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def minimax(self, estado, jugador):
        max_jugador = self.letter #yo
        otro_jugador = 'O' if jugador == 'X' else 'X' #el otro jugador

        #primero veremos si la movida anterior es ganadora
        #este es nuestro caso base
        if estado.actual_ganador == otro_jugador:
            #debemos regresar posición y puntaje para llevar el conteo del score para que funcione minimax
            return {'posición' : None,
                    'puntaje' : 1 * (estado.num_cuadros_vacios() + 1) if otro_jugador == max_jugador else -1 * (
                        estado.num_cuadros_vacios() + 1)
                    }
        elif not estado.cuadros_vacios(): #no hay cuadros vacios
            return {'posición' : None,
                    'puntaje' : 0}

        #inicializamos los diccionarios
        if jugador == max_jugador: #aqui empezamos lo que es el algoritmo
            mejor = {'posición' : None, 'puntaje' : -math.inf} #cada puntaje debe ser máximo (más grandes)
        else:
            mejor = {'posición' : None, 'puntaje' : math.inf} #cada puntaje debe ser mínimo

        for posible_movimiento in estado.movimientos_disponi():
            #primer paso: hacer un movimiento y probar ese cuadro
            estado.make_movimiento(posible_movimiento, jugador)
            #sugundo paso: usar minimax recursivamente para simular un juego después de hacer ese movimiento
            puntaje_sim = self.minimax(estado, otro_jugador) #ahora alternamos el jugador
            #tercer paso: deshacer ese movimiento para poder probar otro es la próxima iteración
            estado.tablero[posible_movimiento] = ' '
            estado.actual_ganador = None
            puntaje_sim['posición'] = posible_movimiento #de lo contrario, esto se estropeará por la recursividad
            #cuarto paso: actualizar los diccionarios si es necesario
            if jugador == max_jugador: #estamos tratando de maximizar al max_jugador
                if puntaje_sim['puntaje'] > mejor['puntaje'] :
                    mejor = puntaje_sim #remplaza "mejor"
            else: #pero minimizar el otro jugador
                if puntaje_sim['puntaje'] < mejor['puntaje']:
                    mejor = puntaje_sim
        return mejor
    
    def get_move(self, juego):
        if len(juego.movimientos_disponi()) == 9:
            cuadro = random.choice(juego.movimientos_disponi())
        else:
            #vamos a buscar el cuadro usando el algoritmo minimax
            cuadro = self.minimax(juego, self.letter)['posición']
        return cuadro