import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Satishdb@555'
)

cur = conn.cursor()


class deleted:
    def dptdelete(x,id):
        cur.execute(f"delete from department where departmentid={id}")
        conn.commit()

