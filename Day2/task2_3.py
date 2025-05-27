# Convert hours and Minutes into Seconds

def Convert(time):
    hours,minutes,seconds = map(int,time.split(":"))
    return hours*3600 + minutes*60 + seconds
print(Convert("01:01:20"))
print(Convert("12:11:00"))