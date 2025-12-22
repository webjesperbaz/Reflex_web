import reflex as rx
from Reflex_web.components.link_button import link_button
from Reflex_web.components.title import title
def links() -> rx.Component:
    return rx.vstack(
        title("BODAAAAAAAAAA"),
        link_button("google", "https://gooble.com"),
        link_button("youtube","https://www.youtube.com/watch?v=n2YrGsXJC6Y"),
        link_button("google", "https://gooble.com"),
        link_button("google", "https://gooble.com"),
        width="100%"
        # link_button("otro"),
        # link_button("otro")
       
    )