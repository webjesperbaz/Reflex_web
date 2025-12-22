import reflex as rx
import Reflex_web.styles.styles as styles

# El nombre de la función DEBE ser link_button, todo en minúsculas
def link_icon(url: str) -> rx.Component:
    return rx.link(
           rx.hstack(
                rx.icon("anchor"),
                href=url,
                is_external=True,
                align="center",
                margin="2%"

           )
            

        
        
    )