from flask import Flask

from config import DevelopmentConfig, ProductionConfig, get_config

from routers.main_router import main_router

app = Flask(__name__)
app.config.from_object(get_config('development'))
secret_key = app.config['SECRET_KEY']

app.register_blueprint(main_router)

if __name__ == '__main__':
    app.run()