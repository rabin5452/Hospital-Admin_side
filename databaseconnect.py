import mysql.connector
cnx=mysql.connector.connect(
#    host='localhost',
#     port=3307,
#     user='root',
#     password='bhattarai',
#     database='token'

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
    

def store_db(email,tokenid,arrival_time,waiting_time):
        query='insert into tokendata(email,tokenid,arrivaltime,waitingtime) values (%s,%s,%s,%s)'
        values=(email,tokenid,arrival_time,waiting_time)
        cursor.execute(query,values)
        cnx.commit()

def providelength():
        sql = "SELECT count(*) FROM tokendata"
        cursor.execute(sql)
        data=cursor.fetchone()
        data=data[0]
        return data

def check_email_exists(email):
        ac_tokenid=None
        query="SELECT tokenid from tokendata where email=%s"
        values=email
        access_pass=tuple()
        cursor.execute(query,(values,))
        access_pass=cursor.fetchall()
        for i in access_pass:
                ac_tokenid=i[0]
        cnx.commit()
        if ac_tokenid==None:
                ## not taken
                return 0
        else:   
                ## alredy taken
                return 1
        
def get_minmumtoken():
        query="SELECT * FROM tokendata WHERE tokenid = (SELECT MIN(tokenid) FROM tokendata)"
        cursor.execute(query)
        data=cursor.fetchone()
        return data

def nexttoken(tokenid):
        query=f'DELETE FROM tokendata WHERE tokenid={tokenid}'
        cursor.execute(query)
        cnx.commit()
def update_the_waiting_time():
        pass
def indicate_absent(tokenid,email):
        print("done")
        query="insert into absenttable(email,tokenid) values(%s,%s)"
        values=(email,tokenid)
        cursor.execute(query,values)
        cnx.commit()
        print("done")
def storearrivaltime(time,tokennum):
        query="insert into arrivaltime(tokenid,arrivaltime) values (%s,%s)"
        values=(tokennum,time)
        cursor.execute(query,values)
        cnx.commit()
        pass
def storeservicetime(time,tokennum):
        query="insert into servicetime(tokenid,servicetime) values (%s,%s)"
        values=(tokennum,time)
        cursor.execute(query,values)
        cnx.commit()
        pass

def delete_table():
        query="delete from absenttable"
        cursor.execute(query)
        cnx.commit()
        query="delete from arrivaltime"
        cursor.execute(query)
        cnx.commit()
        query="delete from servicetime"
        cursor.execute(query)
        cnx.commit()
        
def getlenghtofservice():
        query="select count(*) from servicetime"
        cursor.execute(query)
        data=cursor.fetchone()
        return data[0]
    
