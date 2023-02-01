import mysql.connector
cnx=mysql.connector.connect(
   host='127.0.0.1',
    user='root',
    password='',
    database='token'
)
cursor=cnx.cursor()
def getdata(cashierid):
        query='SELECT password from cashier where cashierid= %s'
        values=cashierid
        cursor.execute(query,(values,))
        access_password=cursor.fetchone()
        cnx.commit()
        return access_password[0]
    

def store_db(email,token,arrival_time,waiting_time):
        query='insert into tokendata(email,tokenid,arrivaltime,waitingtime) values (%s,%s,%s,%s)'
        values=(email,token,arrival_time,waiting_time)
        cursor.execute(query,values)
        cnx.commit() 
def providelength():
        sql = """SELECT count(*) as tot FROM tokendata"""
        cursor.execute(sql)
        data=cursor.fetchone()
        data=data[0]
        return data