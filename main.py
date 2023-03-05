from databaseconnect import store_db,providelength,check_user,get_minmumtoken,next_token
token=1
def start_process():
    early_token=get_minmumtoken()
    return early_token


def stop_process():
    pass

def absent_user():
    pass
######################################
def calculate_token(email,time,token_number):
    arrival_time=time
    waiting_time='19-11-11'
    store_db(email,token_number,arrival_time,waiting_time)
    # if  providelength()==0:
    #      store_db(email,token_number,arrival_time,waiting_time)

      
    

    






