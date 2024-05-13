#Сортировка методом прочесывания
def Sortcm(num):
    n = len(num) #длина списка
    step = n #шаг
    while step > 1 or flag:  #пока шаг больше 1 или flag=true
       if step > 1: #еслиш шаг больше 1
           step = int(step / 1.247331) # то делим шаг на 1.247331
       flag, i = False, 0  #присваиваем flag=false, i=0
       while i + step < n: #пока i+step < длины  списка num
          if num[i] > num[i + step]: #если элемент списка с индексом i больше, чем элемент индекса i+step
              num[i], num[i + step] = num[i + step], num[i] # то меняем местами
              flag = True # присваиваем flag= true
          i += step # увеличиваем i на step
    return num

num = input("Введите элементы списка, разделенные пробелом: ").split() # Получаем входные данные от пользователя и разделяем их по пробелу
num = [int(x) for x in num] # Преобразуем введенные значения в целочисленные элементы списка

sorted_list = Sortcm(num)
print("Отсортированный список:", sorted_list)