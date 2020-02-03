from flask import Flask, render_template
from app.views import register_config
from app.config import config1
from app.extensions import config_extensions

def config_error(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html',e=e)


def crate_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config1.get(config_name) or 'default')
    config1.get(config_name).init_app(app)
    print('here111')

    register_config(app)

    config_error(app)

    config_extensions(app)


    return app


