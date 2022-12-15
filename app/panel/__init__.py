from flask import Blueprint

panel = Blueprint('panel',__name__,
                 template_folder='templates',
                 static_folder='static')
from . import routes
