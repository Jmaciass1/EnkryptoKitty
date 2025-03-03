import random
import string

def generar_clave_desplazamiento():
    """Genera una clave aleatoria entre 1 y 25 para el cifrado César."""
    return random.randint(1, 25)

def cifrar_desplazamiento(text, key):
    """Cifra un mensaje usando el cifrado César con módulo 26."""
    alphabet = string.ascii_uppercase
    text = text.upper()
    encrypted_text = "".join(alphabet[(alphabet.index(c) + key) % 26] if c in alphabet else c for c in text)
    return encrypted_text

def descifrar_desplazamiento(text, key):
    """Descifra un mensaje cifrado con el cifrado César en módulo 26."""
    alphabet = string.ascii_uppercase
    decrypted_text = "".join(alphabet[(alphabet.index(c) - key) % 26] if c in alphabet else c for c in text)
    return decrypted_text