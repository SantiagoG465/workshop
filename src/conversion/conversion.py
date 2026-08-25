class Conversion:
    def celsius_a_fahrenheit(self, celsius):
       return (celsius * 9 / 5) + 32
        
    def fahrenheit_a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9
    
    def metros_a_pies(self, metros):
         return metros * 3.28084
    
    def pies_a_metros(self, pies):
        return pies * 0.3048
    
    def decimal_a_binario(self, decimal):
        return bin(decimal)[2:]
    
    def binario_a_decimal(self, binario):
         return int(binario, 2)
    
    def decimal_a_romano(self, numero):
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        resultado = ''
        for valor, simbolo in valores:
            while numero >= valor:
                resultado += simbolo
                numero -= valor
        return resultado
    
    def romano_a_decimal(self, romano):
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        resultado = 0
        for i in range(len(romano)):
            valor_actual = valores[romano[i]]
            if i + 1 < len(romano) and valor_actual < valores[romano[i + 1]]:
                resultado -= valor_actual
            else:
                resultado += valor_actual
        return resultado
    
    def texto_a_morse(self, texto):
        texto = texto.upper()

        return ' '.join(self.MORSE_CODE[letra] for letra in texto if letra in self.MORSE_CODE)


    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        
        Args:
            morse (str): Código Morse separado por espacios
            
        Returns:
            str: Texto decodificado
            
        Ejemplo:
            morse_a_texto("... --- ...") -> "SOS"
            morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
        """
        pass