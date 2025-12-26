import reflex as rx
from Reflex_web.components.link_button import link_button
from Reflex_web.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces de interes:", ),
        link_button("Iglesia: Nuestra Señora de la Granada, Guillena.", "https://maps.app.goo.gl/GLPaEbceqssVoeQ46"),
        link_button("Celebración: Hacienda Toreon Nazarí, Gerena.","https://maps.app.goo.gl/9j8vxzaySszu7GeH9"),
        link_button("Formulario para personas alergicas:", "https://gooble.com"),
        link_button("Subir fotos del evento:", "https://gooble.com"),
        title("Contacto:", ),
        link_button("Email para Jesús", "mailto:pereabazan@gmail.com"),
        width="100%",
        text_size="5em"


        # link_button("otro"),
        # link_button("otro")
       
    )