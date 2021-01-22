def add_time(start, duration, day="No"):
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    st_time,du=start.split()
    st_h,st_m=map(int,st_time.split(":"))
    d_h,d_m=map(int,duration.split(":"))
    if(du == "PM"):
        du="AM"
        st_h+=12
    no_day=((st_h*60 + st_m) + (d_h*60 + d_m)) // 1440
    h=(((st_h*60 + st_m) + (d_h*60 + d_m)) % 1440) // 60
    m=(((st_h*60 + st_m) + (d_h*60 + d_m)) % 1440) - (60*h)
    if(h>11):
        du="PM"
        if(h>12):
            h-=12
    elif(h==0):
        h=12
    if(m<10):m="0"+str(m)
    nnd=""
    if no_day > 1: nnd=" ("+str(no_day)+" days later)" 
    elif no_day == 1: nnd=" (next day)"
    try:
        day=day.title()
        sdi=days.index(day)
        days=days[sdi: ] + days[:sdi]
        day=days[no_day % 7]
        return str(h)+":"+str(m)+" "+du+", "+day+nnd
    except ValueError:
        return str(h)+":"+str(m)+" "+du+nnd







 