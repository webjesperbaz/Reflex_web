import reflex as rx
from Reflex_web.styles.colors import Color
# from Reflex_web.styles.colors. import TextColor
from Reflex_web.styles.styles import Size
import Reflex_web.styles.styles as styles 

def navbar() -> rx.Component:
    return rx.hstack(
        # rx.text(
        #     "Web Jesús",   
        # ),
        rx.hstack(
            rx.text("Jesús", color=Color.BACKGROUND.value),
            rx.text("&", color=Color.PRIMARI.value),
            rx.text("Ana", color=Color.BACKGROUND.value),
            # spacing="2", # Espacio pequeño entre Jesús y Perea
            # font_weight="bold",    *lo hemos puesto todo en la parte de styles y color, para tenerlo mas odenado
            # font_family="confortaa",
            # font_size="1em"
            # style=styles.navbar_tittle_style

            
        ),
        position="sticky",
        bg=Color.CONTENT,
        padding_x=Size.BIG,
        padding_y=Size.DEFAULT,
        # z_index="999"=
        top="0",
        width="100%"
    )
  