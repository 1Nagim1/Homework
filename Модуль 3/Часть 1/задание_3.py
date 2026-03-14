num_1 = int(input("Введите начало диапазона: "))
num_2 = int(input("Введите конец диапазона: "))

for i in range(num_1, num_2):
    if i % 5 == 0:
        print("Buzz")
    if i % 3 == 0:
        print("Fizz")
    if i % 3 and 5 == 0:
            print("Fizz Buzz")
