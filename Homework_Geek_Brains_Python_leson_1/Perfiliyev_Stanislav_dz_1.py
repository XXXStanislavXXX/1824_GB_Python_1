"""

Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

"""

duration = input(" введите ваше время в секундах ")
if int(duration)<60:
    print(duration + " секунд")
elif 60 < int(duration) < 3600:
    minutes = int(duration)//60
    seconds = int(duration) - (minutes * 60)
    print(str(minutes) + " минут " + str(seconds) + " секунд")
elif 3600 < int(duration) < 86400:
    hours = int(duration) // 3600
    minutes = (int(duration) - (hours * 3600)) // 60
    seconds = int(duration) - (minutes * 60) - (hours * 3600)
    print (str(hours) + " часов " + str(minutes) + " минут " + str(seconds) + " секунд")
else:
    days = int(duration) // 86400
    hours = (int(duration) - (days * 86400)) // 3600
    minutes = (int(duration) - (hours * 3600) - (days * 86400)) // 60
    seconds = (int(duration) - (minutes * 60) - (hours * 3600) - (days * 86400))
    print(str(days) + "дней " + str(hours) + " часов " + str(minutes) + " минут " + str(seconds) + " секунд")
