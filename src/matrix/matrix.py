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
        """
        Multiplica cada elemento de la matriz por un escalar.

        Args:
            matriz (list): Matriz (lista de listas)
            escalar (number): Valor escalar por el que se multiplica

        Returns:
            list: Matriz con cada elemento multiplicado por el escalar

        Ejemplo:
            multiplicar_escalar([[1, 2], [3, 4]], 3) -> [[3, 6], [9, 12]]
        """
        return [[matriz[i][j] * escalar for j in range(len(matriz[0]))] for i in range(len(matriz))]

    def transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz (intercambia filas por columnas).

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz transpuesta

        Ejemplo:
            transpuesta([[1, 2, 3], [4, 5, 6]]) -> [[1, 4], [2, 5], [3, 6]]
        """
        if not matriz:
            return []
        return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

    def es_cuadrada(self, matriz):
        """
        Verifica si una matriz es cuadrada (mismo número de filas y columnas).

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            bool: True si la matriz es cuadrada, False en caso contrario

        Ejemplo:
            es_cuadrada([[1, 2], [3, 4]]) -> True
            es_cuadrada([[1, 2, 3], [4, 5, 6]]) -> False
        """
        if not matriz or len(matriz) == 0:
            return False
        return all(len(row) == len(matriz) for row in matriz)

    def es_simetrica(self, matriz):
        """
        Verifica si una matriz es simétrica (igual a su transpuesta).
        Solo aplica a matrices cuadradas.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es simétrica, False en caso contrario

        Ejemplo:
            es_simetrica([[1, 2, 3], [2, 5, 6], [3, 6, 9]]) -> True
            es_simetrica([[1, 2], [3, 4]]) -> False
        """
        if not self.es_cuadrada(matriz):
            return False
        return matriz == self.transpuesta(matriz)

    def traza(self, matriz):
        """
        Calcula la traza de una matriz cuadrada (suma de los elementos de la diagonal principal).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            number: La suma de los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            traza([[1, 2], [3, 4]]) -> 5
            traza([[1, 0, 0], [0, 5, 0], [0, 0, 9]]) -> 15
        """
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada")
        return sum(matriz[i][i] for i in range(len(matriz)))

    def determinante_2x2(self, matriz):
        """
        Calcula el determinante de una matriz 2x2.
        det([[a, b], [c, d]]) = a*d - b*c

        Args:
            matriz (list): Matriz 2x2 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 2x2

        Ejemplo:
            determinante_2x2([[3, 8], [4, 6]]) -> -14
            determinante_2x2([[1, 2], [3, 4]]) -> -2
        """
        if not matriz or len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
            raise ValueError("La matriz debe ser 2x2")
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(self, matriz):
        """
        Calcula el determinante de una matriz 3x3 usando la regla de Sarrus.

        Args:
            matriz (list): Matriz 3x3 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 3x3

        Ejemplo:
            determinante_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 0
            determinante_3x3([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) -> 6
        """
        if not matriz or len(matriz) != 3 or any(len(row) != 3 for row in matriz):
            raise ValueError("La matriz debe ser 3x3")
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    def identidad(self, n):
        """
        Genera una matriz identidad de tamaño n x n.
        La diagonal principal tiene 1s y el resto 0s.

        Args:
            n (int): Tamaño de la matriz identidad

        Returns:
            list: Matriz identidad n x n

        Ejemplo:
            identidad(2) -> [[1, 0], [0, 1]]
            identidad(3) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        """
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, matriz):
        """
        Extrae los elementos de la diagonal principal de una matriz cuadrada.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            list: Lista con los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 5, 9]
            diagonal([[3, 0], [0, 7]]) -> [3, 7]
        """
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada")
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal
        (todos los elementos fuera de la diagonal principal son cero).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es diagonal, False en caso contrario

        Ejemplo:
            es_diagonal([[3, 0], [0, 7]]) -> True
            es_diagonal([[1, 2], [0, 4]]) -> False
        """
        if not self.es_cuadrada(matriz):
            return False
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i != j and matriz[i][j] != 0:
                    return False
        return True

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz rotada 90 grados en sentido horario

        Ejemplo:
            rotar_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
            rotar_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        if not matriz:
            return []
        return [list(reversed(col)) for col in zip(*matriz)]

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.

        Args:
            matriz (list): Matriz (lista de listas)
            valor: Valor a buscar en la matriz

        Returns:
            list: Lista de tuplas (fila, columna) con las posiciones del valor.
                  Retorna lista vacía si no se encuentra.

        Ejemplo:
            buscar_en_matriz([[1, 2, 3], [4, 2, 6], [7, 8, 2]], 2) -> [(0, 1), (1, 1), (2, 2)]
            buscar_en_matriz([[1, 2], [3, 4]], 9) -> []
        """
        posiciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))
        return posiciones
