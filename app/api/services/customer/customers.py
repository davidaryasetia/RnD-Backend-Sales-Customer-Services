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
            city as city, 
            postalcode, 
            country 
        FROM 
            customers;
        """
    )
    response = cur.fetchall()
    cur.close()
    return response

def update_customer(customer_id, data): 
    conn = get_db()
    cur = conn.cursor()
    query = sql.SQL(
        """
        UPDATE 
            customers
        SET 
            customername = %(customername)s, 
            contactname = %(contactname)s, 
            address = %(address)s, 
            city = %(city)s, 
            postalcode = %(postalcode)s, 
            country = %(country)s
        WHERE
            customerid = %(customer_id)s
        """, {
            "customer_id": customer_id, 
        }
    )

def get_customer_details(customer_id: int): 
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT
            customerid, 
            customername, 
            contactname, 
            city as city, 
            postalcode, 
            country
        FROM 
            customers
        WHERE 
            customerid = %(customer_id)s
        """, {
            "customer_id": customer_id
        }
    )
    result = cur.fetchone()
    return result


def delete_customer(customer_id: int): 
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        DELETE FROM 
            customers
        WHERE 
            customerid = %(customer_id)s
        """, {
            "customer_id": customer_id
        }
    )
    conn.commit()
    return 