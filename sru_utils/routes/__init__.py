from sru_utils.routes import util

def setup(app):
    app.router.add_route("POST", "/utils", util.util)