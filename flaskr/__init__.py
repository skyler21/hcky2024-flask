import os

from flask import Flask, render_template 


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
   
   
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    from . import getapi
    app.register_blueprint(getapi.bp)
 
    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
  
    return app
