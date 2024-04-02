# Importar los módulos necesarios
import webbrowser
from win10toast_click import ToastNotifier

# Definir la función que se ejecutará cuando se haga clic en la notificación
def open_url():
    toaster.show_toast(
        "Ejemplo2",
        "Mensaje"
    )

# Inicializar el objeto ToastNotifier
toaster = ToastNotifier()

# Mostrar la notificación
toaster.show_toast(
    "Ejemplo",  # Título de la notificación
    "¡Haz clic para abrir la URL!",  # Mensaje de la notificación
    # Ruta al ícono de la notificación
    duration=5,  # Duración de la notificación en segundos; None = dejar la notificación en el Centro de notificaciones
    threaded=True,  # True = ejecutar otro código en paralelo; False = la ejecución del código esperará hasta que desaparezca la notificación
    callback_on_click=open_url  # Función que se ejecutará cuando se haga clic en la notificación
)
