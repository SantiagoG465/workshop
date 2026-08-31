class Strings:
    def es_palindromo(self, texto):
        if texto == "":
            return True
        texto_normalizado = "".join(ch.lower() for ch in texto if ch.isalnum())
        return texto_normalizado == texto_normalizado[::-1]

    def invertir_cadena(self, texto):
        cadena_invertida = ""
        for i in range(len(texto) - 1, -1, -1):
            cadena_invertida += texto[i]
        return cadena_invertida

    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        return sum(1 for letra in texto if letra in vocales)

    def contar_consonantes(self, texto):
        consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for letra in texto if letra in consonantes)

    def es_anagrama(self, texto1, texto2):
        limpio1 = "".join(caracter.lower() for caracter in texto1 if caracter.isalnum())
        limpio2 = "".join(caracter.lower() for caracter in texto2 if caracter.isalnum())
        return sorted(limpio1) == sorted(limpio2)

    def contar_palabras(self, texto):
        if texto.strip() == "":
            return 0
        return len(texto.split())

    def palabras_mayus(self, texto):
        if texto == "":
            return ""
        palabras = texto.split(" ")
        resultado = []
        for palabra in palabras:
            if palabra == "":
                resultado.append("")
            else:
                resultado.append(palabra[:1].upper() + palabra[1:])
        return " ".join(resultado)

    def eliminar_espacios_duplicados(self, texto):
        if texto == "":
            return ""
        resultado = []
        ultimo_era_espacio = False
        for caracter in texto:
            if caracter == " ":
                if not ultimo_era_espacio:
                    resultado.append(caracter)
                    ultimo_era_espacio = True
            else:
                resultado.append(caracter)
                ultimo_era_espacio = False
        return "".join(resultado)

    def es_numero_entero(self, texto):
        if texto in ("", "+", "-"):
            return False
        if texto[0] in "+-":
            texto = texto[1:]
        if texto == "":
            return False
        for caracter in texto:
            if caracter < "0" or caracter > "9":
                return False
        return True

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = []
        for caracter in texto:
            if "a" <= caracter <= "z":
                base = ord("a")
                nuevo = chr((ord(caracter) - base + desplazamiento) % 26 + base)
                resultado.append(nuevo)
            elif "A" <= caracter <= "Z":
                base = ord("A")
                nuevo = chr((ord(caracter) - base + desplazamiento) % 26 + base)
                resultado.append(nuevo)
            else:
                resultado.append(caracter)
        return "".join(resultado)

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "" or len(subcadena) > len(texto):
            return []
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones