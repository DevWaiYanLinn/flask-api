from src import create_app
from asgiref.wsgi import WsgiToAsgi

asgi = WsgiToAsgi(create_app())
