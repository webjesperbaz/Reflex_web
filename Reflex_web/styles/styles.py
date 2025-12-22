from enum import Enum
import reflex as rx

# constantes:
MAX_WIDTH="600px",


# tamaños:
class Size(Enum):
    SMALL= "0,5em"
    MEDIUM= "0,8"
    DEFAULT= "1em"
    BIG = "2em"


# Styles

BASE_STYLE= {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value

        
    }
} 


button_title_style= dict(
    font_size= Size.DEFAULT.value
)
    
button_body_style= dict(
    font_size= Size.MEDIUM.value
)
    
    
