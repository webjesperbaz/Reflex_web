import reflex as rx
import datetime     #para poner la fecha del año actual

# El nombre de la función DEBE ser link_button, todo en minúsculas
def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"google.es {datetime.date.today().year}",href="https://google.es", is_external=True ),
        rx.text("Derechos reservados"),
        align="center"
       
    )