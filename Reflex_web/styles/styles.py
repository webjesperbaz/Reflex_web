from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TexColor
from .fonts import Font as Font

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
    "font_family": Font.DEFAULT.value,                               #Para cambiar la web de manera global
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value, 
    }
} 


button_title_style= dict(
    font_size= Size.DEFAULT.value,
    color=TexColor.HEADER.value,
     
)
    
button_body_style= dict(
    font_size= Size.MEDIUM.value,
    color=TexColor.BODY.value
)
    
    
navbar_tittle_style= dict(
    font_size= Font.LOGO.value,
    font_weight="bold",    
    font_family="confortaa",
    
)