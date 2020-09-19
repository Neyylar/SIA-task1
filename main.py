import numpy
dic = {'1': [66, 32, 38, 37, 1],
 '2': [9, 16, 54, 2],
 '3':  [8, 7, 61]
 }
cum_sum = []
maxs = []
print ("Изначальное значение словаря:")
print (dic)
for key, value in dic.items():
  x = numpy.random.randint(-100, -1)
  cum_sum.append(numpy.cumsum(value))
  maxs.append(max (value))
  value.insert(0, x)
  dic.update({key: value})
dic.update({'4': maxs})
print ("Измененное значение словаря:")
print (dic)
print ("Нарастающая сумма:")
k = 1
for i in cum_sum:
  print (f'Для {k}-го элемента словаря')
  print (i)
  k = k + 1