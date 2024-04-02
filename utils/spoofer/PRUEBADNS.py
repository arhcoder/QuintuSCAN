def reemplazar_letras(url, letra_original, letra_cirilica):
    # Reemplazar la letra original por la letra cirílica en la URL
    nueva_url = url.replace(letra_original, letra_cirilica)
    return nueva_url

# URL original
url_original = "https://www.amazon.com.mx"

# Letras a reemplazar y su equivalente cirílico
letra_original = "a"
letra_cirilica = "а"

# Generar la nueva URL con la letra cirílica
url_nueva = reemplazar_letras(url_original, letra_original, letra_cirilica)

# Imprimir la nueva URL
print("URL original:", url_original)
print("URL con letras cirílicas:", url_nueva)
