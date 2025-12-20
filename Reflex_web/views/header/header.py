import reflex as rx

def header() -> rx.Component:
        return  rx.vstack(
                    rx.avatar(fallback="J & A",size="4"),
                    rx.text("Boda Jesús y Ana"),
                    rx.text("Texto de presentación de la boda...")         
                
                
        )
