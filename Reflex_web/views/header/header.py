import reflex as rx
from Reflex_web.styles.colors import Color, TextColor 

def header() -> rx.Component:
        return  rx.vstack(
                    rx.hstack(
                       rx.avatar(fallback="J & A",
                            bg=Color.CONTENT.value,
                            size="9",
                              ),
                        rx.avatar(
                            src="/alianzas.jpg",
                            size= "9"
                              ),
                        margin="5%"      
                    ),    

                    rx.text("Boda Jesús y Ana", font_size= "1.5em", margin_top="3%"),
                    rx.text("20-06-26", font_size= "1.5em", ),
                   
                    rx.text("Texto de presentación de la boda................................. hasñhgajñhkjhakjlh..." , font_size= "1.2em", margin="3%",  align="center"),    
                    
                   
                    align="center",
                         
                )
