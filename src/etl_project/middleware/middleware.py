from flask import Flask, Response
from config.Settings import UseSettings

class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        token = environ.get('HTTP_AUTHORIZATION')
        if not token or not self.__validate_token(token):
            print("Acesso não autorizado")
            res = Response("Unauthorized: Token inválido ou ausente", status=401)
            return res(environ, start_response)

        return self.app(environ, start_response)
    
    def __validate_token(self, token):
        settings = UseSettings.get_settings()
        return token == "Bearer " + settings.AUTH_TOKEN

        