from datetime import datetime,timedelta

offset_india=timedelta(hours=05.30)

offset_usa=timedelta(hours=12.00)

time_country1=datetime.utcnow()+offset_india
print("first",time_country1)

time_country2=datetime.utcnow()+offset_usa
print("second",time_country1)

time_diff=time_country1-time_country2
print("time difference",time_diff.total_seconds())