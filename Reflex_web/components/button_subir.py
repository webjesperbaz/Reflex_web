import reflex as rx
from Reflex_web.models import Imagen
import base64

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

def botton_subir():
    return rx.center(
        rx.vstack(
            rx.heading("Subir fotos del evento"),
            rx.upload(
                rx.text("Arrastra o haz click aquí"),
                id="upload_id",
                border="2px dashed green",
            ),
            rx.button(
                "Subir foto",
                on_click=State.guardar_foto(rx.upload_files(upload_id="upload_id")),
            ),
            rx.divider(),
            rx.button("Mostrar última foto", on_click=State.recuperar_ultima_foto),
            rx.cond(
                State.imagen_base64 != "",
                rx.image(src=State.imagen_base64, width="300px"),
            ),
        ),
        padding="2em",
    )