import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
#1
df = pd.read_csv('Aids2.csv', sep=';')

#2
shape = df.shape
size = df.size
types = df.dtypes
print("Характеристики датасета: размер, форма, типы данных")
print (size, shape, types)

#3
print("Процент женщин, заразившихся СПИДом в Австралии:")
print(100*df['sex'].value_counts().loc['F']/len(df))
print("Процент мужчин, заразившихся СПИДом в Австралии:")
print(100*df['sex'].value_counts().loc['M']/len(df))

#4
print("Процент мужчин до 45 лет, успешно прошедших курс лечения:")
print(len(df.query('sex == "M" and age < 45 and status == "A"'))/len(df.query('sex == "M"')))

#5
#df.query('age > 14 and status == "D"').sort_values(by = 'death').plot(x='death', y='age')
#plt.show()

#px.line(df.query('age > 14 and status == "D"').sort_values(by='death'), x='death', y='age').show()

#6
#df.query('age < 30 and status == "D"')['state'].value_counts().plot.pie(y='status')
#plt.show()

#plt.pie(df.query('age < 30 and status == "D"')['state'].value_counts().values, labels=df['state'].value_counts().axes[0])
#plt.show()

#7
data7_1 = df.query('status == "D"').groupby('state')['age'].mean()
data7_2 = data7_1.append(pd.Series(df.query('status == "D"')['age'].mean(), index=['Australia']))
#data7_2.plot.bar()
#plt.show()

#8
print("Максимальный возраст смерти по регионам:")
print(df.query('status == "D"').groupby('state')['age'].max())
print("Минимальный возраст смерти по регионам:")
print(df.query('status == "D"').groupby('state')['age'].min())
for state in df["state"].unique():
    if (len(df.query ('age < 30'))>len(df.query ('age > 31 and age < 55'))+ len(df.query ('age > 55'))):
        print ("В регионе " + state + " больше зараженных в возрасте до 30 лет")
    if (len(df.query('age > 31 and age < 55')) > len(df.query('age < 30')) + len(df.query('age > 55'))):
        print("В регионе " + state + " больше зараженных в возрасте от 30 до 55 лет")
    if (len(df.query('age > 55')) > len(df.query('age < 30')) + len(df.query('age > 31 and age < 55'))):
        print("В регионе " + state + " больше зараженных в возрасте от 55 лет")

#9
#df.groupby('state')['T.categ'].value_counts().plot.barh()
#plt.show()

#10
if (len(df.query('age < 30 and status == "A"'))/len(df.query('age < 30 and status == "D"')) > 1):
    print ("До 30 лет больше выживших")
if (len(df.query('age > 30 and age < 55 and status == "A"')) / len(df.query('age > 30 and age < 55 and status == "D"')) > 1):
    print("От 30 до 55 лет больше выживших")
if (len(df.query('age > 54 and status == "A"'))/len(df.query('age > 54 and status == "D"')) > 1):
    print ("От 55 лет больше выживших")
