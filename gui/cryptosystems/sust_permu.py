import random
import string

def generar_permutacion_aleatoria(longitud):
    permutacion = list(range(longitud))
    random.shuffle(permutacion)
    return permutacion

def generar_permutacion_inversa(permutacion):
    inversa = [0] * len(permutacion)
    for i, pos in enumerate(permutacion):
        inversa[pos] = i
    return inversa

def generar_claves(texto):
    texto = texto.upper()  # Convertir todo a mayúsculas
    texto = ''.join(filter(lambda c: c in string.ascii_uppercase, texto))  # Filtrar solo letras A-Z

    num_bloques = random.randint(1, max(1, len(texto) // 2))
    bloque_longitud = len(texto) // num_bloques
    bloques = [texto[i:i + bloque_longitud] for i in range(0, len(texto), bloque_longitud)]

    claves = [generar_permutacion_aleatoria(len(bloque)) for bloque in bloques]
    permutacion_final = generar_permutacion_aleatoria(len(texto))

    return claves, permutacion_final, bloque_longitud

def cifrar_sustPermu(texto, bloque_longitud, claves, permutacion_final):
    texto = texto.upper()
    texto = ''.join(filter(lambda c: c in string.ascii_uppercase, texto))

    bloques = [texto[i:i + bloque_longitud] for i in range(0, len(texto), bloque_longitud)]
    texto_cifrado = ""

    for i, bloque in enumerate(bloques):
        clave = claves[i]
        bloque_cifrado = ''.join(bloque[clave[j]] for j in range(len(bloque)))
        texto_cifrado += bloque_cifrado

    texto_cifrado = ''.join(texto_cifrado[permutacion_final[i]] for i in range(len(texto_cifrado)))
    return texto_cifrado

def descifrar_sustPermu(texto_cifrado, claves, permutacion_final):
    inversa_permutacion_final = generar_permutacion_inversa(permutacion_final)
    texto_cifrado = ''.join(texto_cifrado[inversa_permutacion_final[i]] for i in range(len(texto_cifrado)))

    texto_descifrado = ""
    inicio = 0
    for clave in claves:
        longitud = len(clave)
        bloque_cifrado = texto_cifrado[inicio:inicio + longitud]
        clave_inversa = generar_permutacion_inversa(clave)
        bloque_descifrado = ''.join(bloque_cifrado[clave_inversa[j]] for j in range(longitud))
        texto_descifrado += bloque_descifrado
        inicio += longitud

    return texto_descifrado
