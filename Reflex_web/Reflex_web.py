import reflex as rx 
from Reflex_web.components.navbar import navbar 
from Reflex_web.views.header.header import header
from Reflex_web.views.links.links import links
from Reflex_web.components.footer import footer
import Reflex_web.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:  #todo lo que pongamos a continuacion es lo que se pintará en la web
    
    # text= rx.text("holiwiii", color="blue")
    # button= rx.button("button")
    return rx.box(
        navbar(),
        rx.center(
             rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100€",
                margin_y="20px"
            )
    
        ),
        footer()
    )


    


app = rx.App(               #creo una app
    style=styles.BASE_STYLE
)              
app.add_page(index)         #llamo a la pagina index
#app.compile()               #le digo que se compile, pero actualmente ya no es necesario


