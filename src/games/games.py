import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower().strip()
        jugador2 = jugador2.lower().strip()
        
        opciones_validas = ["piedra", "papel", "tijera"]
        
        if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
            return "invalid"
        
        if jugador1 == jugador2:
            return "empate"
        
        if jugador1 == "piedra":
            return "jugador1" if jugador2 == "tijera" else "jugador2"
        elif jugador1 == "papel":
            return "jugador1" if jugador2 == "piedra" else "jugador2"
        elif jugador1 == "tijera":
            return "jugador1" if jugador2 == "papel" else "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]
        
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]
        
        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            return "empate"
        
        return "continua"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if desde_fila < 0 or desde_fila > 7 or desde_col < 0 or desde_col > 7:
            return False
        if hasta_fila < 0 or hasta_fila > 7 or hasta_col < 0 or hasta_col > 7:
            return False
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        if desde_fila == hasta_fila:
            inicio = min(desde_col, hasta_col) + 1
            fin = max(desde_col, hasta_col)
            for col in range(inicio, fin):
                if tablero[desde_fila][col] != " ":
                    return False
        else:
            inicio = min(desde_fila, hasta_fila) + 1
            fin = max(desde_fila, hasta_fila)
            for fila in range(inicio, fin):
                if tablero[fila][desde_col] != " ":
                    return False
        
        return True