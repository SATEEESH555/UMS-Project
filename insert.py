import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Satishdb@555'
)

cur = conn.cursor()


class inserted:
    
    def dptinsert(x,dptid,dptname):
        cur.execute(f"insert into department values({dptid},'{dptname}')")
        conn.commit()