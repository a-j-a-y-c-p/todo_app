import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:0000@localhost/todo_app')
    SQLALCHEMY_TRACK_MODIFICATIONS = False