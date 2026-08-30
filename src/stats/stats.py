class Stats:
    def promedio(self, numeros):
        return sum(numeros) / len(numeros) if numeros else 0
    
    def mediana(self, numeros):
        if not numeros:
            return 0
        sorted_nums = sorted(numeros)
        n = len(sorted_nums)
        if n % 2 == 1:
            return sorted_nums[n // 2]
        else:
            return (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
    def moda(self, numeros):
        if not numeros:
            return 0

        contador = {}
        for valor in numeros:
            contador[valor] = contador.get(valor, 0) + 1

        valor_mas_frecuente = numeros[0]
        max_frecuencia = 0

        for valor in numeros:
            if contador[valor] > max_frecuencia:
                max_frecuencia = contador[valor]
                valor_mas_frecuente = valor

        return valor_mas_frecuente
    
    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0

        media = self.promedio(numeros)
        varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return varianza ** 0.5
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        pass
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        pass