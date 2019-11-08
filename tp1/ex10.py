import datetime

distance = 170000

def getDieTime(speed):
    speed_ms = speed/3.6
    minutes_left = round((distance/speed_ms)/60)
    return datetime.datetime.now() + datetime.timedelta(minutes=minutes_left)

print(getDieTime(130))

for i in range(100,310,10):
    res = getDieTime(i)
    print('Pour une vitesse de :',i,'km/h je serais écrasé à',res.hour,'h',res.minute,'m',res.second,'s')