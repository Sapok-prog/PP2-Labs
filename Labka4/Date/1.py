import datetime

a = datetime.datetime.today()

for i in range(6):
    day_x = a - datetime.timedelta(days = i) 
    print(f'{i} days ago was : {day_x.strftime("%x")}')