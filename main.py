from databaseconnect import store_db,get_minmumtoken,providelength,storearrivaltime,getlenghtofservice
from datetime import datetime
import numpy as np
from welcome import services_times
from scipy.stats import poisson
arrivaltimes=[]

def time_operation(time_str, operation, value):
    hours, minutes, seconds = map(int, time_str.split('-'))
    time_in_min = hours * 60 + minutes + seconds / 60.0
    if operation == '+':
        result_in_min = time_in_min + value
    elif operation == '-':
        result_in_min = time_in_min - value
    else:
        raise ValueError(f"Invalid operation '{operation}', must be '+' or '-'")
    result_hours, result_minutes = divmod(result_in_min, 60)
    result_seconds = round((result_in_min - result_minutes * 60) * 60)
    if result_seconds<0:
        result_seconds=0
    return f"{int(result_hours):02d}-{int(result_minutes):02d}-{int(result_seconds):02d}"
def time_op(time1,time2):
    hour1,min1,sec1=time1.split("-")
    hour2,min2,sec2=time2.split("-")
    hour1=int(hour1)*60+int(min1)+int(sec1)/60
    hour2=int(hour2)*60+int(min2)+int(sec2)/60
    return hour2-hour1



def stop_process():
    pass

def absent_user():
    pass
######################################
def calculate_token(email,time,token_number,start_time):
    arrival_time=time
    if (providelength()==1) or (providelength()==0):
        arrival_times_for_a_user=time_op(str(start_time),str(arrival_time))
        storearrivaltime(arrival_times_for_a_user,token_number)
        arrivaltimes.append(arrival_times_for_a_user)
        waiting_time=time_operation(arrival_time,"+",5)
        store_db(email,token_number,arrival_time,waiting_time)
    else:
        #calculate the arrival rate
        arrival_times_for_a_user=time_op(str(start_time),str(arrival_time))
        arrivaltimes.append(arrival_times_for_a_user)
        storearrivaltime(arrival_times_for_a_user,token_number)
        #calculating difference between two successive arrival time
        inter_arrival_times = np.diff(arrivaltimes)
        # Calculate the mean inter-arrival time
        mean_inter_arrival_time = np.mean(inter_arrival_times)
        # Calculate the arrival rate lambda
        lambda_est = 1 / mean_inter_arrival_time
        if getlenghtofservice()==0:
            queueline=providelength()
            wait=(queueline//2+1)*5
            waiting_time=time_operation(arrival_time,"+",wait)
            store_db(email,token_number,arrival_time,waiting_time)
        else:
            service_line=getlenghtofservice()
            #calculate the service rate of the 2 servers
            avg_service_time=sum(services_times)/service_line
            mu=2/avg_service_time
            
            #calculate the utilization rate of the servers
            rho=lambda_est/mu

            #get the number of people in the queue line

            #calculate the average waiting time
            avg_waiting_time=((1 / (mu - lambda_est )) * rho) / (1 - rho)
            waiting_time=time_operation(arrival_time,"+",avg_waiting_time)
            store_db(email,token_number,arrival_time,waiting_time)

      
    

    






