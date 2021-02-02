"""
A씨는 게시판 프로그램을 작성하고 있다.

A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
출력 : 총페이지수

A씨가 필요한 프로그램을 작성하시오.
"""
"""
m=int(input("총 게시글 수 :"))
n=int(input("한 페이지에 보여줄 게시글 수 :"))
try:
    page=m//n  #몫을 int 로 저장
    if m%n!=0: #나머지가 0이 아닐 경우
        page+=1 #page값 1 증가   
    print(page) 
except ZeroDivisionError: #n값이 1보다 작을경우 예외처리
    print("n값이 1보다 작습니다.")
"""
import math
m=int(input("총 게시글 수 :"))
n=int(input("한 페이지에 보여줄 게시글 수 :"))
try:
    page=math.ceil(m/n)
    print(page)
except ZeroDivisionError: #n값이 1보다 작을경우 예외처리
    print("n값이 1보다 작습니다.")
