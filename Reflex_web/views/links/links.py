import reflex as rx
from Reflex_web.components.link_button import link_button
from Reflex_web.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces de interes:", ),
        link_button("google", "https://gooble.com"),
        link_button("youtube","https://www.youtube.com/watch?v=n2YrGsXJC6Y"),
        link_button("google", "https://gooble.com"),
        link_button("google", "https://gooble.com"),
        title("Contacto:", ),
        link_button("Email para Jesús", "mailto:pereabazan@gmail.com"),
        width="100%"
        # link_button("otro"),
        # link_button("otro")
       
    )