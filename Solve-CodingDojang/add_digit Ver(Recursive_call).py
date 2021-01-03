def recursive_call(number):
    if number<10:
        return number;
    
    return (number%10)+recursive_call(number//10)
#number%10 = number을 10으로 나눈 나머지값
#number//10= number울 10으로 나눈 정수형 몫 값
print(recursive_call(91))


