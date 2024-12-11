num_1= int(input("Введите начало диапазона: "))
num_2= int(input("Введите конец диапазона: "))

for i in range(num_1,num_2):
        print(i)
for i in range(num_2,num_1,-1):
    print(i)

for i in range(num_1,num_2):
    if i%7 == 0:
        print(i)

for i in range(num_1,num_2):
    if i%5 == 0:
        print(i)
