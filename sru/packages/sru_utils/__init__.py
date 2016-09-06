from . import routes

def setup(app):
    app.router.add_route("POST", "/utils", routes.util)