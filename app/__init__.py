from flask import Flask
from flask_mysqldb import MySQL

db = MySQL()


def create_app():


    app = Flask(__name__)
    app.secret_key = 'mysecretkey'

    #inicializacion de la base de datos
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='100tifico'
    app.config['MYSQL_DB']='libreria'
    db.init_app(app)

    # Registro de los Blueprints
    from .shop import shop
    app.register_blueprint(shop, url_prefix='/shop')

    from .panel import panel
    app.register_blueprint(panel, url_prefix='/panel')


    return app
