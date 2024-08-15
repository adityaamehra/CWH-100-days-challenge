import time 
ts=int(time.strftime('%H'))
if(ts>=00 and ts<12):
    print("GM sir")
elif(ts==12):
    print("Good NOON sir")
elif(ts>12 and ts<18):
    print("GA sir")
else:
    print("GE sir")