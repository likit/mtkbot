import os
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    from bot.app.chatbot import chatbot_bp
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')
    return app