import flet as ft
def mailadd(page:ft.page):
    page.title ="Addmail",
def main(page: ft.page):
    page.title="QuintuScan"
    page.bgcolor=""
    page.add(
        ft.Text("QuintuScan"),
        ft.Text("Notificar anomalias a:"),
        ft.TextField(
            label="Ingresar correo electronico",
            
        ),
        ft.CupertinoFilledButton(
            content=ft.Text("Agregar correo"),
            opacity_on_click=0.3,
            on_click=lambda e:print("Prueba"),
        )
    )
ft.app(target=mailadd)
