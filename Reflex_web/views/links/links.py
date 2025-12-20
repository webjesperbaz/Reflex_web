import reflex as rx
from Reflex_web.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("google", "https://gooble.com"),
        link_button("youtube","https://www.youtube.com/watch?v=n2YrGsXJC6Y"),
        # link_button("otro"),
        # link_button("otro")
       
    )