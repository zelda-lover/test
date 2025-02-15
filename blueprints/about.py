from flask import Blueprint
about_bp = Blueprint('about', __name__)
@about_bp.route('/')
def index():
    return "Hello Flask Blueprints"