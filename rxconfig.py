import reflex as rx

config = rx.Config(
    app_name="Reflex_web",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)