import reflex as rx

config = rx.Config(
    app_name="tu_app",
    # Formato: mysql+pymysql://usuario:contraseña@host:puerto/nombre_db
    db_url="mysql+pymysql://root:password@localhost:3306/mi_base_datos",
)