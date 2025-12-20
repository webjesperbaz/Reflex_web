import reflex as rx 
from Reflex_web.components.navbar import navbar 
from Reflex_web.views.header.header import header
from Reflex_web.views.links.links import links
from Reflex_web.components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:  #todo lo que pongamos a continuacion es lo que se pintará en la web
    
    # text= rx.text("holiwiii", color="blue")
    # button= rx.button("button")
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )
    


app = rx.App()              #creo una app
app.add_page(index)         #llamo a la pagina index
#app.compile()               #le digo que se compile, pero actualmente ya no es necesario


