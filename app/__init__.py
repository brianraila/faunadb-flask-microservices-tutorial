import os
from flask import Flask 

def create_app():

    app = Flask( __name__, instance_relative_config=True,)

    app.config.from_mapping( SECRET_KEY=os.environ.get('SECRET_KEY') or 'you-will-never-guess',)
    

    from app.services import index, products, reviews

    app.register_blueprint(index.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(reviews.bp)



    return app

app = create_app()