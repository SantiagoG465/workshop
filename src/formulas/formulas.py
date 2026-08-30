class Formulas:
    """
    Clase con ejercicios de fórmulas de física, finanzas y álgebra.
    """

    def velocidad_media(self, distancia, tiempo):
        if tiempo <= 0:
            raise ValueError("El tiempo debe ser mayor que 0 segundos.")

        return distancia / tiempo

    def mruv_posicion(self, posicion_inicial, velocidad_inicial, aceleracion, tiempo):
            if tiempo < 0:

                raise ValueError("El tiempo no puede ser negativo.")
            return posicion_inicial + velocidad_inicial * tiempo + 0.5 * aceleracion * tiempo ** 2

    def mruv_velocidad(self, velocidad_inicial, aceleracion, tiempo):
        
        if tiempo < 0:
            raise ValueError("El tiempo no puede ser negativo.")
        return velocidad_inicial + aceleracion * tiempo

    def fuerza_newton(self, masa, aceleracion):
        
        if masa < 0:
            raise ValueError("La masa no puede ser negativa.")
        return masa * aceleracion

    def energia_cinetica(self, masa, velocidad):
        
        if masa < 0:
            raise ValueError("La masa no puede ser negativa.")
        return 0.5 * masa * velocidad ** 2

    def energia_potencial(self, masa, altura, gravedad=9.8):
        
        if masa < 0:
            raise ValueError("La masa no puede ser negativa.")
        return masa * gravedad * altura

    def ley_ohm_voltaje(self, corriente, resistencia):
        
        return corriente * resistencia

    def ley_ohm_corriente(self, voltaje, resistencia):
         if resistencia == 0:
            raise ValueError("La resistencia no puede ser cero.")

         return voltaje / resistencia

    def interes_simple(self, capital, tasa, tiempo):
        if capital < 0:
            raise ValueError("El capital no puede ser negativo.")
        if tiempo < 0:
            raise ValueError("El tiempo no puede ser negativo.")
        return capital * tasa * tiempo

    def interes_compuesto(self, capital, tasa, tiempo, n=1):
        if capital < 0:
            raise ValueError("El capital no puede ser negativo.")
        if tiempo < 0:
            raise ValueError("El tiempo no puede ser negativo.")
        if n <= 0:
            raise ValueError("El número de capitalizaciones debe ser mayor que cero.")
        return capital * (1 + tasa / n) ** (n * tiempo)

    def discriminante(self, a, b, c):
        return b ** 2 - 4 * a * c

    def raices_cuadraticas(self, a, b, c):
        if a == 0:
            raise ValueError("El coeficiente cuadrático no puede ser cero.")
        
        discriminante = b ** 2 - 4 * a * c
        
        if discriminante < 0:
            raise ValueError("El discriminante es negativo, no hay raíces reales.")
        
        sqrt_discriminante = discriminante ** 0.5
        raiz1 = (-b + sqrt_discriminante) / (2 * a)
        raiz2 = (-b - sqrt_discriminante) / (2 * a)
        
        return (raiz1, raiz2)

    def imc(self, peso, altura):
        """
        Calcula el Índice de Masa Corporal (IMC).

        Args:
            peso (float): Peso en kilogramos
            altura (float): Altura en metros

        Returns:
            float: Índice de Masa Corporal

        Fórmula: IMC = peso / altura^2

        Ejemplo:
            imc(70, 1.75) -> 22.86
        """
        pass

    def hipotenusa_pitagoras(self, cateto1, cateto2):
        """
        Calcula la longitud de la hipotenusa de un triángulo rectángulo.

        Args:
            cateto1 (float): Longitud del primer cateto
            cateto2 (float): Longitud del segundo cateto

        Returns:
            float: Longitud de la hipotenusa

        Fórmula: h = sqrt(cateto1^2 + cateto2^2)

        Ejemplo:
            hipotenusa_pitagoras(3, 4) -> 5.0
        """
        pass
