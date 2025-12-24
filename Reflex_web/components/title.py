import reflex as rx
from Reflex_web.styles.colors import TextColor as TextColor


# El nombre de la función DEBE ser link_button, todo en minúsculas
def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        color=TextColor.BODY,
        align="center",
        padding="5%"
        
        
    )