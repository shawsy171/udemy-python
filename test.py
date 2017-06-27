# print('hello World test')
# name = input('please enter name again')
# print('Hello' + name)
#
# greeting = "There"
#
# age = 24
#
# print(greeting + age)

a = 10
b = 2

print(a / b)  # float

for i in range(0, a // b):  # int
    print(i)


print("my age is years {0} old".format(35))

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

age = 23
if 18 < age < 35:
    print('Congrats you can legally drink')
elif age < 45:
    print('this is prime time')
else:
    print('you old bastard')

    # none is a date type in pyhton

