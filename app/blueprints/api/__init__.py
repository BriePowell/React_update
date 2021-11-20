from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')

from . import routes    #from the same folder, import routes