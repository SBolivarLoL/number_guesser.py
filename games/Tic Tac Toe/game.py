import time
from player import Human_player, RandomComputer_player

class TicTacToe:
    def __init__(self):
        self.tablero = [' ' for _ in range(9)] #usamos solo una lista para representar el tablero 3x3
        self.actual_ganador = None #sigue el puntaje de los ganadores

    def print_tablero(self):
        #para sacar las filas
        for fila in [self.tablero[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(fila) + ' |')

    @staticmethod   
    def print_num_tablero():
        # 0 | 1 | 2 etc. nos dice qué numero le corresponde a cada espacio
        numero_tablero = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for fila in numero_tablero:
            print('| ' + ' | '.join(fila) + ' |')

    def posibles_movimientos(self):
        # usamos list comprenhension para volver todo lo que está abajo en una sola linea
        return [i for i, lugar in enumerate(self.tablero) if lugar == ' '] # enumerate() crea una lista con tuplas adentro que en este caso tendran x u o y su indice
        #movimientos = []
        # for (i,  lugar) in enumerate(self.board):
        #      ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #       if lugar == ' ':
        #           movimientos.append(i)
        # return movimientos

    def cuadros_vacios(self):
        return ' ' in self.tablero

    def num_cuadros_vacios(self):
        return self.tablero.count(' ')

    def make_movimiento(self, cuadro, letter):
        if self.tablero[cuadro] == ' ':
            self.tablero[cuadro] = letter
            if self.ganador(cuadro, letter):
                self.actual_ganador = letter
            return True
        else:
            return False

    def ganador(self, cuadro, letter):
        # gana si hay 3 seguidas, verificamos filas, columnas y diagonales
        #verificar fila
        fila_ind = cuadro // 3
        fila = self.tablero[fila_ind*3 : (fila_ind + 1) * 3]
        if all([lugar == letter for lugar in fila]):
            return True

        #verificar columna
        columna_ind = cuadro % 3
        columna = [self.tablero[columna_ind+i*3] for i in range(3)]
        if all([lugar == letter for lugar in columna]):
            return True

        #verificar diagonales
        #pero solo los números pares que son las únicas diagonales viables
        if cuadro % 2 == 0:
            diagonal1 = [self.tablero[i] for i in [0, 4, 8]] #diagonal de izquierda arriba a derecha abajo
            if all([lugar == letter for lugar in diagonal1]):
                return True
            diagonal2 = [self.tablero[i] for i in [2, 4, 6]] #diagonal de derecha arriba a izquierda abajo
            if all([lugar == letter for lugar in diagonal2]):
                return True

        #si  al final nada es cierto
        return False

def jugar(juego, jugador_x, jugador_o, print_juego=True):
    
    if print_juego:
        juego.print_num_tablero()

    letter = 'X' #primera letra
        #iterar mientras el juego todavía tiene cuadros vacíos
        # (no  nos preocupamos por el ganador porque solo vamos a devolver eso, lo cual rompe el loop)
    while juego.cuadros_vacios():
            #ver el movimiento del jugador correcto
        if letter == 'O':
            cuadro = jugador_o.get_move(juego)
        else:
            cuadro = jugador_x.get_move(juego)

        if juego.make_movimiento(cuadro, letter):
            if print_juego:
                print (letter + f' hace un movimiento al cuadro {cuadro}')
                juego.print_tablero()
                print('') #línea vacía

            if juego.actual_ganador:
                if print_juego:
                    print(letter + ' ganó!')
                return letter

            letter = 'O' if letter == 'X' else 'X' #cambia el jugador
        #pausa para que no se vea todo feo
        time.sleep(1)

    if print_juego:
        print('Es un empate!')

if __name__ == '__main__':
    jugador_x = Human_player('X')
    jugador_o = RandomComputer_player('O')
    #t es tic tac toe
    t = TicTacToe()
    jugar(t, jugador_x, jugador_o, print_juego=True)