import flet as ft

def main(page: ft.page):
    page.title="QuintuScan"
    page.bgcolor=""
    page.add(
        ft.Text("QuintuScan"),
        ft.Text("Notificar anomalias a:"),
        ft.CupertinoFilledButton(
            content=ft.Text("Agregar correo"),
            opacity_on_click=0.3,
            on_click=lambda e: print("Pipipedo"),
        ),
    )
ft.app(target=main)
