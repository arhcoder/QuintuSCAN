from urllib.parse import unquote

def obtener_url_texto_plano(url):
    # Decodificar la URL para convertirla a texto plano
    url_decodificada = unquote(url)
    # Convertir la URL decodificada a una lista de caracteres
    caracteres = list(url_decodificada)
    # Obtener los códigos ASCII de los caracteres
    codigos_ascii = [ord(caracter) for caracter in caracteres]
    # Traducir los códigos ASCII a caracteres y unirlos en una cadena de texto
    caracteres_texto_plano = ''.join([chr(codigo) for codigo in codigos_ascii])
    # Devolver la URL en texto plano, los códigos ASCII y los caracteres traducidos
    return url_decodificada, codigos_ascii, caracteres_texto_plano

# URL de ejemplo
url_ejemplo = "https://www.google.com.mx"

# Llamar a la función para obtener la URL en texto plano, los códigos ASCII y los caracteres traducidos
url_texto_plano, codigos_ascii, caracteres_texto_plano = obtener_url_texto_plano(url_ejemplo)

# Imprimir la URL en texto plano
print("URL en texto plano:", url_texto_plano)

# Imprimir los códigos ASCII obtenidos
print("Códigos ASCII de los caracteres de la URL:", codigos_ascii)

# Imprimir los caracteres traducidos
print("Caracteres traducidos de la URL:", caracteres_texto_plano)
