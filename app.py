from flask import Flask
from routers.main_router import main_router

app = Flask(__name__)

app.register_blueprint(main_router)

if __name__ == '__main__':
    app.run()