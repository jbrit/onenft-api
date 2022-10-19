import os

app_config = {
    'SQLALCHEMY_DATABASE_URI': os.environ.get("DATABASE_URL","sqlite:///app.db").replace("postgres://", "postgresql://"),
    'SECRET_KEY': os.environ.get("SECRET_KEY","SECRET_KEY"),
    'DEBUG': True,
}