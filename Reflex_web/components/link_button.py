import reflex as rx

# El nombre de la función DEBE ser link_button, todo en minúsculas
def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True    #para que cada vez que se le de a un boton, se abra en una nueva pagina del navegador y no se pierda la pg base

)