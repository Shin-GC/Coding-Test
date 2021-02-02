def find_generator(number):
    return sum([int(i) for i in str(number)])+number

print(find_generator(91))

