"""
A씨는 개발된 소스코드를 특정업체에 납품하려고 한다. 개발된 소스코드들은 탭으로 들여쓰기가 된것, 공백으로 들여쓰기가 된 것들이 섞여 있다고 한다. A씨는 탭으로 들여쓰기가 된 모든 소스를 공백 4개로 수정한 후 납품할 예정이다.

A씨를 도와줄 수 있도록 소스코드내에 사용된 탭(Tab) 문자를 공백 4개(4 space)로 바꾸어 주는 프로그램을 작성하시오.
"""

filename=input("input your file name: ")
#unicode error : unicodeescape 발생 시 "앞에 r 추가 또는 경로 입력시 \\ 두번 사용 
tempfile=open(filename)
tempfile=tempfile.read()
tempfile_str=tempfile.replace("\t","    ")
tempfile=open(filename,'w')
tempfile.write(tempfile_str)

tempfile.close()
