import reflex as rx
import Reflex_web.styles.styles as styles

# El nombre de la función DEBE ser link_button, todo en minúsculas
def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_big_right"
                ),
                rx.hstack(
                    rx.text(text, style=styles.button_title_style),
                    rx.text(text, style=styles.button_body_style)
                )
                
            )
        ),
        href=url,
        is_external=True,    #para que cada vez que se le de a un boton, se abra en una nueva pagina del navegador y no se pierda la pg base
        width="100%",
        margin="2%"
    )