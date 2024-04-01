import winotify

# Declarar el ID de la aplicación, el intérprete predeterminado y la ruta del script de manera global
r = winotify.Registry("app_id", winotify.PY_EXE, r"c:\abs\path\to\script.py")
notifier = winotify.Notifier(r)

# Registrar una función para usar como callback
@notifier.register_callback
def say_hello():
    print("¡Hola!")

# Crear una nueva notificación y pasar la función registrada al parámetro 'launch'
toast = notifier.create_notification(title="Una notificación", 
                                     msg='¡Haz clic en mí!',
                                     )
toast.add_actions(label="Hola",launch=say_hello)
toast.show()

# No need for the following line
# notifier.start()