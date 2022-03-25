import timeit
import time
import random

# Задание №1.
print("Задание №1.\n")

# Реализованная мною ф-я, использующая побитовое сравнение,
# показывает единую производительность независимо от размерности проверяемого числа.

# Однако в представленной реализации проверки числа на четность производительность
# ухудшается с увеличением размерности проверяемого числа.

def IsEven(value):
    return value % 2 == 0

def IsEvenBin(value):
    return value & 1 == 0


s = 2132

print(timeit.timeit(lambda :IsEven(s))) # 0.11713129999407101
print(timeit.timeit(lambda :IsEvenBin(s)),"\n") # 0.1356789999990724


s = 21325364759
print(timeit.timeit(lambda :IsEven(s))) # 0.15058549999957904
print(timeit.timeit(lambda :IsEvenBin(s)),"\n") # 0.13549780000175815

s = 21325364759589564575858
print(timeit.timeit(lambda :IsEven(s))) # 0.16536030000133906
print(timeit.timeit(lambda :IsEvenBin(s)),"\n") # 0.13718359998892993

s = 21325364759589564575858586575675755657586976878978907897897
print(timeit.timeit(lambda :IsEven(s))) # 0.20848990000376943
print(timeit.timeit(lambda :IsEvenBin(s)),"\n") # 0.13335210000514053

s = 9223372036854775807**2
print(timeit.timeit(lambda :IsEven(s))) # 41.038770999992266
print(timeit.timeit(lambda :IsEvenBin(s)),"\n") # 0.13619720000133384




# Задание №2.
print("Задание №2.\n")

# Во втором задании не удалость конкретно определить поставленную задачу, а именно:
# каким функционалом необходимо наделить самописный буфер
# и в каком виде его необходимо реализовать. Но определенного результата удалось достичь.
# Первый вариант (class BufferTo) функционалом ограничен. Удаление элементов буфера происходит за счет добавления новых
# элементов в массив. Во второй же реализации (class BUFET) присутствует возможность напрямую удалять элементы буфера.
# В первой реализации элемент i (i ∈ [0,n-1] ) добавляется в конец,при этом эkементы [n,n+n-1] соответственно перезаписыавют
# элементы [0,n-1].
# Во второй реализации каждый последующий элемент добавляется в конец массива, однако при добавлении эдемента n, осуществляется
# сдвиг массива влево, где n --> n-1, n-1 --> n-2, ....., 1 --> 0, 0 эл. удаляется.

class BufferTo:
    def __init__(self,SIZE):
        self.list = {}
        self.last_pos = 0
        self.size = SIZE

    def add(self, *inp):
        for num in range(len(inp)):
            #self.list.append( [ num, inp[num] ] )
            self.list[(self.last_pos+num) % self.size  ] =  inp[num]
        self.last_pos =  ( self.last_pos + len(inp) ) % self.size
        print(f"{self.list.values()} --- len:{len(self.list)}")


class BUFET:
    def __init__(self,SIZE):
        self.list = []
        self.size = SIZE

    def __hell(self, num):
        if len(self.list) < self.size:
            self.list.append(num)
        else:
            self.list.pop(0)
            self.list.append(num)

    def add(self, *inp):
        for num in inp:
            self.__hell(num)
        print(self.list)

    def dell(self,count):
        for i in range(count):
            self.list.pop(0)
        print(self.list)


print("\n")

bufT = BufferTo(10)
bufT.add(1,2,3,4,5)
bufT.add(6, 7, 8,9,11)
bufT.add(61, 52, 33,4,5,678,7,48,9,10,141,12,13,145,15,16,417,18,19,20)
for i in range(1,11):
    bufT.add(i*5)


bf = BUFET(10)

bf.add(1,2,3,4,5)
bf.add(6, 7, 8,9,11)
bf.add(61, 52, 33,4,5,678,7,48,9,10,141,12,13,145,15,16,417,18,19,20)
for i in range(1,11):
    bf.add(i*5)
bf.dell(4)
bf.add(3,6,8,2,84,5)



# Задание №3.
print("Задание №3.\n")
# Наиболее оптимальным решением стало написание всеми известной QuckSort. Из всех сортировок, используемых только для собеседований,
# (а также мною изученных) она наиболее эффективна, ввиду своей скорости обработки информации, а также применимости для
# сортировки больших массивов данных, а также имеющую средненюю временную сложность O(n log(n)).
"""
Для 10к эл.

selectoin
2.4555318355560303

qsort
0.023935556411743164

bubble
9.724833488464355

Bubble and selectoin при 100к и более не эффективны.

"""
def bubble_sort(data: list[int]):
    while True:
        check = 0
        for i in range(len(data)):
            if i == len(data) - 1:
                break
            if data[i] > data[i+1]:
                check += 1
                mp = data[i]
                data[i] = data[i+1]
                data[i+1] = mp
        if check == 0:
            break
    return data

def selection_sort(num_list:list) -> list:
    for i in range(len(num_list)):
        min = i
        for j in range(i+1,len(num_list)):
            if num_list[j] < num_list[min]:
                min = j
        num_list[min],num_list[i] = num_list[i],num_list[min]

    return num_list


def qsort(num_list:list) -> list:

    if len(num_list) < 1:
        return num_list
    mid = num_list[len(num_list) // 2]
    left_list = []
    right_list = []
    for i in range(len(num_list)):
        if num_list[i] < mid:
            left_list.append(num_list[i])
        if num_list[i] > mid:
            right_list.append(num_list[i])
    return qsort(left_list) + [mid]*num_list.count(mid) + qsort(right_list)

def tt(test:list):
    test.sort()
    return test




test = [x+random.randint(1,1000) for x in range(1000000)]
#test.sort()

old = time.time()
#p = selection_sort(test.copy())
print(time.time() - old)
#print(test==p)


old = time.time()
p1 = qsort(test.copy())
print(time.time() - old)
print(test==p1)
#print(p)

old = time.time()
#p2 = bubble_sort(test.copy())
print(time.time() - old)
#print(test==p2)

#print(p == p1 == p2)





#old = time.time()

#print(time.time() - old)
#print(p == test)

# Черновые работы
"""
class Butter:
    def __init__(self,SIZE):
        #self.summ = 0
        self.list = []
        self.place = 0
        self.size = SIZE

    def add(self, *inp):

        if len(self.list) < self.size:
            if len(self.list) + len(inp) < self.size:
                for num in inp:
                    self.list.append(num)
                    #self.count+=1
            else:
                count = 0
                while len(self.list) != self.size:
                    self.list.append(inp[count])
                    count += 1
                for i in range(len(inp) - count):
                    if i == len(self.list) - 1:
                        self.list[i] = inp[count + i]
                        self.place = i
                        self.add(inp[count + i + 1:])
                        pass
                    self.list[i] = inp[count + i]
                    self.place = i

        elif len(self.list) == self.size :
            count = 0
            for k,num in enumerate(inp):
                if self.place + 1 == len(self.list):
                    self.add(inp[k+1:])
                    pass
                self.list[self.place+1] = num



            pass
        print(f"{self.list} --- len:{len(self.list)} --- place {self.place}")
        #print(f"{self.list} --- len:{len(self.list)}")

"""
"""
class Buffer:

    def __init__(self, SIZE):
        self.list = []
        self.place = 0
        self.size = SIZE
        self.flag = 0

    def add(self, *inp):

        def test(count):
            mp = 0
            while mp != len(self.list): #self.size
                if count == len(inp):
                    self.place = mp
                    break
                self.list[mp] = inp[count]
                mp += 1
                count += 1
                if mp == len(self.list):
                    test(count)


        if len(self.list) < self.size:
            count = 0
            while  len(self.list) != self.size:
                if count == len(inp):
                    break
                self.list.append(inp[count])
                count += 1
                if len(self.list) == self.size:
                    test(count)

        elif len(self.list) == self.size:
            count = 0
            while self.place != len(self.list):  # self.size
                if count == len(inp):
                    break
                self.list[self.place] = inp[count]
                self.place += 1
                count += 1
                if self.place == len(self.list):
                    test(count)
                    break

        print(f"{self.list} --- len:{len(self.list)}")

"""