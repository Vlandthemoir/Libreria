from flask import Blueprint

shop = Blueprint('shop',__name__,
                 template_folder='templates',
                 static_folder='static')
from . import routes
