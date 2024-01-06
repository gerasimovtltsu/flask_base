from flask import Blueprint

main_router = Blueprint('main', __name__)

@main_router.route('/')
def index():
    return 'Hello from the main router!' 
