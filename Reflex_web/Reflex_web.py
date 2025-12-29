import reflex as rx 
from Reflex_web.components.navbar import navbar 
from Reflex_web.views.header.header import header
from Reflex_web.views.links.links import links
from Reflex_web.components.footer import footer
from Reflex_web.components.title import title 
from Reflex_web.components.link_icon import link_icon
import Reflex_web.styles.styles as styles
from .models import Imagen
import base64
from Reflex_web.components.button_subir import botton_subir


# class State(rx.State):       #Para hacer el backend
#     pass
class State(rx.State):
    # Variable para mostrar la imagen recuperada
    imagen_base64: str = ""

    async def guardar_foto(self, files: list[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            
            with rx.session() as session:
                nueva_img = Imagen(
                    nombre=file.filename,
                    datos=upload_data,
                    tipo=file.content_type
                )
                session.add(nueva_img)
                session.commit()
        return rx.window_alert("Imagen guardada en MySQL")

    def recuperar_ultima_foto(self):
        with rx.session() as session:
            # Buscamos la última imagen subida
            result = session.exec(Imagen.select().order_by(Imagen.id.desc())).first()
            if result:
                # Convertimos bytes a base64 para que el navegador pueda mostrarlo
                encoded = base64.b64encode(result.datos).decode("utf-8")
                self.imagen_base64 = f"data:{result.tipo};base64,{encoded}"


def index() -> rx.Component:  #todo lo que pongamos a continuacion es lo que se pintará en la web
    
    # text= rx.text("holiwiii", color="blue")
    # button= rx.button("button")
    return rx.box(
        navbar(),
        rx.center(
             rx.vstack(
                header(),
                links(),
                botton_subir(),
                max_width=styles.MAX_WIDTH,
                width="95%",
                margin_y="20px",
                align="center", 
            ),
            
        ),
        
        footer(),
    
    )


    


app = rx.App(               #creo una app
    style=styles.BASE_STYLE
)              
app.add_page(index)         #llamo a la pagina index
#app.compile()               #le digo que se compile, pero actualmente ya no es necesario


