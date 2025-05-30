import psycopg2
from flask import current_app, g
from config.config import Config
from psycopg2.extras import RealDictCursor

def get_db(): 
    if 'db' not in g: 
        g.db = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            dbname=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD, 
            cursor_factory=RealDictCursor
        )
    return g.db  # ✅ pindahkan return ke luar blok if

    
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None: 
        db.close()