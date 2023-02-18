import sqlite3

def db_select():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('SELECT * FROM info_userdata')
    userdatalist = c.fetchall()

    tuplenum = len(userdatalist)
    userdatalast = userdatalist[tuplenum-1]
    
    user_id = userdatalast[0]
    user_temp = userdatalast[1]
    user_humid = userdatalast[2]    
    user_philipshuetoken = userdatalast[3]
    user_smartthingstoken = userdatalast[4]
    user_location = userdatalast[5]
 
    #return(user_id, user_temp, user_humid, user_philipshuetoken, user_smartthingstoken)
    print(user_id, user_temp, user_humid, user_philipshuetoken, user_smartthingstoken, user_location)

db_select()    