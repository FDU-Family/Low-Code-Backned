from datetime import timedelta


class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    JWT_SECRET_KEY = "密钥"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)


class Config_Dev(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database_dev.db"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    DEBUG = True
