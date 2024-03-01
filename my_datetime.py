from datetime import datetime

current_datetime = datetime.now()

# print(current_datetime.year)        
# print(current_datetime.month)       
# print(current_datetime.day)         
# print(current_datetime.hour)        
# print(current_datetime.minute)      
# print(current_datetime.second)      
# print(current_datetime.microsecond) 
# print(current_datetime.date())    
# print(current_datetime.time())  


d1 = datetime(year=2012, month=1, day=7, hour=14)

seventh_day_2020 = datetime(year=1990, month=10, day=28, hour=14)
print(seventh_day_2020.weekday()) # 6
