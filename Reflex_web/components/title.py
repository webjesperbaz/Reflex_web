import reflex as rx


# El nombre de la función DEBE ser link_button, todo en minúsculas
def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        color="green",
        align="center",
        padding="5%"
        
        
    )