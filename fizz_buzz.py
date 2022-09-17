def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizz_buzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    
    else:
        print(input)

x = 10
y = 11
emp_list = []
emp_list.append(x)
emp_list.append(y)
y = emp_list[0]
x = emp_list[1]
print(x)
print(y)

    