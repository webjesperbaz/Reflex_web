import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Web Jesús",
            
        ),
        position="sticky",
        bg="grey",
        padding_x="16px",
        padding_y="8px",
        # z_index="999"
        top="0"
    )
  