import random
import math

def cifrar_afin(texto, a, b):
    """Cifra un texto usando el cifrado afín en el alfabeto inglés (A-Z)."""
    texto_cifrado = ""
    for caracter in texto.upper():  # Convertimos a mayúsculas para trabajar en A-Z
        if 'A' <= caracter <= 'Z':  # Solo ciframos letras
            codigo = ord(caracter) - ord('A')
            codigo_cifrado = (a * codigo + b) % 26
            texto_cifrado += chr(codigo_cifrado + ord('A'))
        else:
            texto_cifrado += caracter  # Mantener espacios y caracteres especiales sin cambios
    return texto_cifrado

def descifrar_afin(texto_cifrado, a, b):
    """Descifra un texto cifrado con el cifrado afín en el alfabeto inglés (A-Z)."""
    texto_descifrado = ""
    a_inverso = pow(a, -1, 26)  # Calcular el inverso modular de 'a' módulo 26

    for caracter in texto_cifrado.upper():
        if 'A' <= caracter <= 'Z':  # Solo desciframos letras
            codigo = ord(caracter) - ord('A')
            codigo_descifrado = (a_inverso * (codigo - b)) % 26
            texto_descifrado += chr(codigo_descifrado + ord('A'))
        else:
            texto_descifrado += caracter  # Mantener espacios y caracteres especiales sin cambios
    return texto_descifrado

def generar_claves_afin():
    """Genera una clave válida (a, b) para el cifrado afín en el alfabeto inglés."""
    coprimos = [i for i in range(1, 26) if math.gcd(i, 26) == 1]  # Valores de 'a' coprimos con 26
    a = random.choice(coprimos)
    b = random.randint(0, 25)  # 'b' puede ser cualquier valor entre 0 y 25
    return a, b
