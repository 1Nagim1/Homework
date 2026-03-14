start_range=int(input("Введите начало диапазона"))
stop_range=int(input("Введите конец диапазона"))

sum_chet = 0
count_chet = 0

for i in range(start_range,stop_range):
    if i % 2 == 0:
        count_chet +=1
        sum_chet += i
print(sum_chet)
print(sum_chet / count_chet)

sum_nechet = 0
count_nechet = 0


for i in range(start_range,stop_range):
    if i % 2 > 0:
        sum_nechet +=1
        count_nechet +=i
print(sum_nechet)
print(sum_nechet/count_nechet)

sum_nine=0
count_nine=0

for i in range(start_range,stop_range):
    if i%9==0:
        count_nine+=1
        sum_nine=+i
print(sum_nine)
print(sum_nine/count_nine)

