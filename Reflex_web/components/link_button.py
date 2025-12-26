import reflex as rx
from Reflex_web.styles.styles import Size as Size
from Reflex_web.styles.styles import button_title_style as button_title_style
from Reflex_web.styles.styles import button_body_style as button_body_style

from Reflex_web.styles.colors import TextColor as TextColor
from Reflex_web.styles.colors import Color as Color



# El nombre de la función DEBE ser link_button, todo en minúsculas
def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_big_right",
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin= Size.MEDIUM.value
                ),
                rx.hstack(
                    rx.text(text, size="3"),
                    spacing="1"
                ) 
            ),
            bg=Color.CONTENT, 
            height="4em"
                              
        ),
        href=url,
        is_external=True,    #para que cada vez que se le de a un boton, se abra en una nueva pagina del navegador y no se pierda la pg base
        width="100%",
        margin="1%",
        padding="2%",
        
        
        
        
    )