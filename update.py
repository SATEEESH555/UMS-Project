import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='ums',
    user='root',
    password='Satishdb@555'
)

cur = conn.cursor()


class updated:
    
    def dptupdate(x,colname,newval,oldval):
        cur.execute(f"update department set {colname}='{newval}' where {colname} = '{oldval}'")
        conn.commit()

