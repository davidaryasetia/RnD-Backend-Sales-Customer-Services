from psycopg2 import sql
from config.db import get_db


def get_list_customers(): 
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT  
            customerid, 
            customername, 
            contactname,
            city, 
            postalcode, 
            country
        FROM 
            customers;
        """
    )

    response = cur.fetchall()
    cur.close()
    return response