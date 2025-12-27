import reflex as rx
from Reflex_web.components.link_button import link_button
from Reflex_web.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces de interes:", ),
        link_button("Iglesia: Nuestra Señora de la Granada, Guillena.", "https://maps.app.goo.gl/GLPaEbceqssVoeQ46", "/icon/iglesia.svg"),
        link_button("Celebración: Hacienda Toreon Nazarí, Gerena.","https://maps.app.goo.gl/9j8vxzaySszu7GeH9", "/icon/copas.svg"),
        link_button("Formulario para personas alérgicas:", "https://docs.google.com/forms/d/e/1FAIpQLSd5JUOXLFvzjpCB55a_HACp52fvrZti_Ao4qMqcg6Az8I7WLg/viewform?usp=dialog", "/icon/alergico.svg"),
        link_button("Subir fotos del evento:", "https://gooble.com", "/icon/upload.svg"),
        title("Contacto:", ),
        link_button("Email para Jesús", "mailto:pereabazan@gmail.com", "/icon/email.svg"),
        width="100%",


        # link_button("otro"),
        # link_button("otro")
       
    )