from urllib.parse import unquote

def obtener_url_texto_plano(url):
    # Decodificar la URL para convertirla a texto plano
    url_decodificada = unquote(url)
    # Convertir la URL decodificada a una lista de caracteres
    caracteres = list(url_decodificada)
    # Obtener los códigos ASCII de los caracteres
    codigos_ascii = [ord(caracter) for caracter in caracteres]
    # Devolver la URL en texto plano y los códigos ASCII
    return url_decodificada, codigos_ascii

# URL de ejemplo
url_ejemplo = "https://www.google.com.mx"

# Llamar a la función para obtener la URL en texto plano y los códigos ASCII
url_texto_plano, codigos_ascii = obtener_url_texto_plano(url_ejemplo)

# Imprimir la URL en texto plano y los códigos ASCII
print("URL en texto plano:", url_texto_plano)
print("Códigos ASCII de los caracteres de la URL:", codigos_ascii)
