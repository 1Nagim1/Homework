sum_1=0
maximum=0
MINIMUM=0

while True:
    num_1=int(input("Введите число"))
    if num_1 == 7:
        print("Good bye!")
        break
    else:
        sum_1+=num_1
        maximum=sum_1
    print(f"Максималное значение и сумма: ",sum_1,sum_1)
    print(f'Минимальное значение:',num_1)