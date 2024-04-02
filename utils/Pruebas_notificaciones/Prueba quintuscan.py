import time
from winotify import Notification, audio
import winotify
r= winotify.Registry("QuintuScan", winotify.PY_EXE,r"c:\abs\path\to\script.py")
notifier= winotify.Notifier(r)
@notifier.register_callback
def funcion2():
    print("Hola")
nombrenoti="QuintuScan"
toast= Notification(
    app_id=nombrenoti,
    title="Ejemplo",
    msg="Este es un mensaje de ejemplo",
    duration="long",
)
toast.add_actions(label="Boton",launch=funcion2)
toast.show()
