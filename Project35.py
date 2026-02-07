num = int(input("Enter a number: "))

temp = num
digits = []
sum_disarium = 0


while temp > 0:
    digits.append(temp % 10)
    temp //= 10

digits.reverse()


for i in range(len(digits)):
    sum_disarium += digits[i] ** (i + 1)


if sum_disarium == num:
    print(num, "is a Disarium number")
else:
    print(num, "is not a Disarium number")