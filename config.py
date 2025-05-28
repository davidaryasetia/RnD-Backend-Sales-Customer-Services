import os 

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:Okokokdalll1@localhost:5432/hris_system_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
