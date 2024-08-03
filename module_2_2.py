first = input('')
second = input('')
third = input('')
if int(first) == int(second) and int(second) == int(third) and int(first) == int(third):
    print(3)
elif int(first) != int(second) and int(second) != int(third) and int(first) != int(third):
    print(0)
else:
    print(2)