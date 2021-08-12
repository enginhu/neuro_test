from flask import Blueprint

bp = Blueprint('calculate_distance', __name__)

from app.calculate_distance import routes