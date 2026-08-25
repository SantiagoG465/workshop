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
       
        if not lista:
            return lista
        
        k = k % len(lista)
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        return (n * (n + 1)) // 2 - sum(lista)
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }
    
    def implementar_cola(self):
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0) if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }
    
    def matriz_transpuesta(self, matriz):
        if not matriz or not matriz[0]:
            return []
        return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
