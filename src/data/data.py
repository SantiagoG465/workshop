class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        resultado = []

        for indice in range(len(lista) - 1, -1, -1):
            resultado.append(lista[indice])

        return resultado
    
    def buscar_elemento(self, lista, elemento):
        
        for indice, valor in enumerate(lista):
            if valor == elemento:
                return indice
        return -1
    
    def eliminar_duplicados(self, lista):
        resultado = []

        for elemento in lista:
            existe = False
            for guardado in resultado:
                if elemento == guardado and type(elemento) is type(guardado):
                    existe = True
                    break
            if not existe:
                resultado.append(elemento)

        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        resultado = []
        indice1 = 0
        indice2 = 0

        while indice1 < len(lista1) and indice2 < len(lista2):
            if lista1[indice1] <= lista2[indice2]:
                resultado.append(lista1[indice1])
                indice1 += 1
            else:
                resultado.append(lista2[indice2])
                indice2 += 1

        resultado.extend(lista1[indice1:])
        resultado.extend(lista2[indice2:])
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
            return lista
        
        k = k % len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass
