import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('hotel_bookings.csv', sep=';')

#0 - Размер, форма и типы данных в дататсете
shape = df.shape
size = df.size
types = df.dtypes
#print (size, shape, types)

#1 - Процентное соотношение людей, заказывавших приемы пищи в отеле
print("Процент людей, заказавших только завтрак:")
print(100*df['meal'].value_counts().loc['BB']/len(df))
print("Процент людей, заказавших два приема пищи:")
print(100*df['meal'].value_counts().loc['HB']/len(df))
print("Процент людей, заказавших три приема пищи:")
print(100*df['meal'].value_counts().loc['FB']/len(df))

#2 - График количества заездов по месяцам
#df['arrival_date_month'].value_counts().plot(x='arrival_date_month')
#plt.show()
#3 - Круговая диаграмма гостей отеля по странам, которым номера заказало туристическое агенство
#df.query('distribution_channel == "TA/TO"')['country'].value_counts().plot.pie(y='country')
#plt.show()

#4 - Процент случаев, когда зарезервированный номер не совпадает с утвержденным
print("Процент случаев, когда зарезервированный номер не совпадает с утвержденным")
print(100*len(df.query('reserved_room_type != assigned_room_type'))/len(df))
#5 - Гистограмма людей которые забронировали номер во второй раз по странам
#df.query('is_repeated_guest == 1')['country'].value_counts().plot.bar()
#plt.show()
#6 - Наименьшее время до въезда во время будней или во время выходных? (Спонтанная бронь - на один - два дня)
if len(df.query('stays_in_weekend_nights < 3 and lead_time == 0 and stays_in_week_nights == 0'))/2 > len(df.query('stays_in_weekend_nights == 0 and lead_time == 0 and stays_in_week_nights < 3'))/5:
    print("Люди чаще спонтанно остаются в отеле по выходным")
else:
    print("Люди чаще спонтанно остаются в отеле в будние дни")
#7 - В какое время года люди предпочитают Resort Hotel, а в какое - City Hotel?
autRH = len(df.query('hotel == "Resort Hotel" and (arrival_date_month == "September" or arrival_date_month == "October" or arrival_date_month == "November")'))
winRH = len(df.query('hotel == "Resort Hotel" and (arrival_date_month == "December" or arrival_date_month == "January" or arrival_date_month == "February")'))
sprRH = len(df.query('hotel == "Resort Hotel" and (arrival_date_month == "March" or arrival_date_month == "April" or arrival_date_month == "May")'))
sumRH = len(df.query('hotel == "Resort Hotel" and (arrival_date_month == "June" or arrival_date_month == "July" or arrival_date_month == "August")'))

autCH = len(df.query('hotel == "City Hotel" and (arrival_date_month == "September" or arrival_date_month == "October" or arrival_date_month == "November")'))
winCH = len(df.query('hotel == "City Hotel" and (arrival_date_month == "December" or arrival_date_month == "January" or arrival_date_month == "February")'))
sprCH = len(df.query('hotel == "City Hotel" and (arrival_date_month == "March" or arrival_date_month == "April" or arrival_date_month == "May")'))
sumCH = len(df.query('hotel == "City Hotel" and (arrival_date_month == "June" or arrival_date_month == "July" or arrival_date_month == "August")'))

if (autRH > autCH): print("Осенью люди предпочитают Resort Hotel")
else: print("Осенью люди предпочитают City Hotel")
print(autRH/autCH)
if (winRH > winCH): print("Зимой люди предпочитают Resort Hotel")
else: print("Зимой люди предпочитают City Hotel")
print(winRH/winCH)
if (sprRH > sprCH): print("Весной люди предпочитают Resort Hotel")
else: print("Весной люди предпочитают City Hotel")
print(sprRH/sprCH)
if (sumRH > sumCH): print("Летом люди предпочитают Resort Hotel")
else: print("Летом люди предпочитают City Hotel")
print(sumRH/sumCH)