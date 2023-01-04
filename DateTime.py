import datetime
import time
import sys


StartTime = datetime.datetime.now()


print(' Дата и время = ', StartTime)
print(' Месяц = ', StartTime.month)
print(' День = ', StartTime.day)
print(' Час = ', StartTime.hour)
print(' Минуты = ', StartTime.minute)

a = list(range(2, 3500000))


EndTime = datetime.datetime.now()
print(" Время выполнения - ", str(EndTime - StartTime))

# Дата и время сейчас
Now = time.time()
DateTime = time.ctime(Now)
print("   Дата и время", DateTime)
print("   Дата и время", str(DateTime))

# см. Простой Python стр. 295
