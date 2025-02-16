import datetime

a = datetime.datetime.today()
yesterday_a = a - datetime.timedelta(days = 1)
tomorrow_a = a + datetime.timedelta(days = 1)

print(f'yesterday was : {yesterday_a.strftime("%x")}')
print(f'today is : {a.strftime("%x")}')
print(f'tomorrow will be : {tomorrow_a.strftime("%x")}')