class Magic:
    
    def fibonacci(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        fib_list = [0, 1]
        for _ in range(2, n):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list
    
    def es_primo(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        if n < 2:
            return []
        primos = []
        for num in range(2, n + 1):
            if self.es_primo(num):
                primos.append(num)
        return primos
    
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        suma_divisores = 0
        for i in range(1, n):
            if n % i == 0:
                suma_divisores += i
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        resultado = []
        for i in range(filas):
            fila = [1]
            if i > 0:
                for j in range(1, i):
                    fila.append(resultado[i-1][j-1] + resultado[i-1][j])
                fila.append(1)
            resultado.append(fila)
        return resultado
    
    def factorial(self, n):
        if n < 0:
            return None
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return (a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        digitos = str(abs(n))
        num_digitos = len(digitos)
        suma = sum(int(d) ** num_digitos for d in digitos)
        return suma == abs(n)
    
    def es_cuadrado_magico(self, matriz):
        if not matriz or len(matriz) == 0:
            return False
        
        n = len(matriz)
        
        for fila in matriz:
            if len(fila) != n:
                return False
        
        suma_magica = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_magica:
                return False
        
        for col in range(n):
            if sum(matriz[row][col] for row in range(n)) != suma_magica:
                return False
        
        if sum(matriz[i][i] for i in range(n)) != suma_magica:
            return False
        
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_magica:
            return False
        
        return True