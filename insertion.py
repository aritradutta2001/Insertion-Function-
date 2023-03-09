import mysql.connector as con
conn=con.connect(host="localhost",port='3306',user='root',password='',database='insertdb')

def insert(connection,tableName,data):
        if(tableName!=''):
            cur = connection.cursor()
            sql = "INSERT INTO "+tableName+" VALUES (%s,%s,%s)"
            cur.execute(sql,data)
            connection.commit()
        else:
            print("Please Submit Data")

  
insert(conn,'users',['1','Aritra','Dutta'])



