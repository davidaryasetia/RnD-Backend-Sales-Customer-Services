from psycopg2 import sql 
from config.db import get_db 

def get_list_employees(): 
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT 
            employeeid, 
            lastname, 
            firstname, 
            birthdate, 
            photo, 
            notes 
        FROM 
            employees
            """
    )
    response = cur.fetchall()
    cur.close()
    return response


def get_employee_details(employeeid):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT 
            employeeid, 
            lastname, 
            firstname, 
            birthdate, 
            photo, 
            notes
        FROM 
            employees
        WHERE 
            employeeid = %(employeeid)s
    """, {
        "employeeid": employeeid
    }
)
    
    response = cur.fetchone()
    cur.close()
    return response


def update_employee(employeeid, data): 
    conn = get_db()
    cur = conn.cursor()
    query = sql.SQL(
        """
        UPDATE 
            employees
        SET
            lastname = %(lastname)s, 
            firstname = %(firstname)s, 
            birthdate = %(birthdate)s,
            notes = %(notes)s
        WHERE 
            employeeid = %(employeeid)s
    """, {
        "employeeid": employeeid
    }
    )

