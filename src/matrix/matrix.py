class Matrix:
   
    def suma_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
       
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices deben tener las mismas dimensiones")
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def multiplicar_matrices(self, A, B):
        """
        Multiplica dos matrices usando la multiplicación matricial estándar.
        El número de columnas de A debe ser igual al número de filas de B.

        Args:
            A (list): Primera matriz de dimensiones m x n
            B (list): Segunda matriz de dimensiones n x p

        Returns:
            list: Matriz resultante de dimensiones m x p

        Raises:
            ValueError: Si las dimensiones son incompatibles para multiplicación

        Ejemplo:
            multiplicar_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) -> [[19, 22], [43, 50]]
        """
        if not A or not B or len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles para multiplicación")
        return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

    def multiplicar_escalar(self, matriz, escalar):
        
        return [[matriz[i][j] * escalar for j in range(len(matriz[0]))] for i in range(len(matriz))]

    def transpuesta(self, matriz):
        
        if not matriz:
            return []
        return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

    def es_cuadrada(self, matriz):
        
        if not matriz or len(matriz) == 0:
            return False
        return all(len(row) == len(matriz) for row in matriz)

    def es_simetrica(self, matriz):
        
        if not self.es_cuadrada(matriz):
            return False
        return matriz == self.transpuesta(matriz)

    def traza(self, matriz):
        
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada")
        return sum(matriz[i][i] for i in range(len(matriz)))

    def determinante_2x2(self, matriz):
        
        if not matriz or len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
            raise ValueError("La matriz debe ser 2x2")
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(self, matriz):
        
        if not matriz or len(matriz) != 3 or any(len(row) != 3 for row in matriz):
            raise ValueError("La matriz debe ser 3x3")
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    def identidad(self, n):
        
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, matriz):
        
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada")
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
       
        if not self.es_cuadrada(matriz):
            return False
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i != j and matriz[i][j] != 0:
                    return False
        return True

    def rotar_90(self, matriz):
        
        if not matriz:
            return []
        return [list(reversed(col)) for col in zip(*matriz)]

    def buscar_en_matriz(self, matriz, valor):
        
        posiciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))
        return posiciones
