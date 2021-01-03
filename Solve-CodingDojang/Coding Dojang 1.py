"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
"""

sum=sum([x for x in range(1,1000) if x%3==0 or x%5==0])
print(sum)