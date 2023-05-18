from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    # CORS(app)
    app.config.from_object("config.Config_Dev")

    db.init_app(app)
    jwt.init_app(app)

    global rmbg, q

    # 注册蓝图
    from .router.user import user

    app.register_blueprint(user)

    return app
