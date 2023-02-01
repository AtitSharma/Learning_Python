from datetime import datetime
# Sun 10 May 2015 13:54:36 -0700
def timedelta(t1,t2):
    timeformat= "%a %d %b %Y %H:%M:%S %z"
    time1=datetime.strptime(t1,timeformat)
    time2=datetime.strptime(t2,timeformat)
    return int(abs(time1-time2).total_seconds())

for i in range(int(input())):
    t1=input()
    t2=input()
    print(timedelta(t1,t2))
