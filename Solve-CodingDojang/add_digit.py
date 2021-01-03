def add_digit(number):
    new_str=str(number)
    add=0
    for i in range(len(new_str)):
        add+=int(new_str[i])
    return add

print(add_digit(91))