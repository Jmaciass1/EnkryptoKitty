import random
import string

def generar_clave_vigenere(texto):
    longitud = random.randint(2, max(2, len(texto) // 2))
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(longitud))

def cifrar_vigenere(texto, clave):
    texto = texto.upper()
    clave = clave.upper()
    texto_cifrado = ""
    clave_expandida = (clave * (len(texto) // len(clave))) + clave[:len(texto) % len(clave)]
    
    for i in range(len(texto)):
        if texto[i] in string.ascii_uppercase:
            codigo_texto = ord(texto[i]) - ord('A')
            codigo_clave = ord(clave_expandida[i]) - ord('A')
            codigo_cifrado = (codigo_texto + codigo_clave) % 26
            texto_cifrado += chr(codigo_cifrado + ord('A'))
        else:
            texto_cifrado += texto[i]  # Mantener caracteres no alfabéticos sin cambios
    
    return texto_cifrado

def descifrar_vigenere(texto_cifrado, clave):
    clave = clave.upper()
    texto_descifrado = ""
    clave_expandida = (clave * (len(texto_cifrado) // len(clave))) + clave[:len(texto_cifrado) % len(clave)]
    
    for i in range(len(texto_cifrado)):
        if texto_cifrado[i] in string.ascii_uppercase:
            codigo_cifrado = ord(texto_cifrado[i]) - ord('A')
            codigo_clave = ord(clave_expandida[i]) - ord('A')
            codigo_descifrado = (codigo_cifrado - codigo_clave) % 26
            texto_descifrado += chr(codigo_descifrado + ord('A'))
        else:
            texto_descifrado += texto_cifrado[i]  # Mantener caracteres no alfabéticos sin cambios
    
    return texto_descifrado
