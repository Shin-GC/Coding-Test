import re

def solution(new_id):
    answer = ''

    lower=new_id.lower() #1단계 소문자 치환 
    #special=re.sub('..[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '',lower)
    #lower=re.sub(r'[{}=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\']', '',lower) # 2단계 알파벳,숫자,-,_,. 를 뺀 나머지 제외
    for c in lower:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer+=c

    arr=list(answer)
    
    new_arr=[]
    for i in range(len(arr)):#..이 붙어 있을시 한개로 바꾸기 3단계   
        if i == len(arr)-1 or len(arr)==1:
            new_arr.append(arr[i])
            break
        if arr[i]=='.':
            if arr[i+1]=='.':
              continue
            else:
                new_arr.append(arr[i])
        else:
            new_arr.append(arr[i])
    
    answer=''.join(new_arr) 
  
    answer=answer.rstrip('.')
    answer=answer.lstrip('.')
    #처음이나 끝에 .이 있을 시 제거
    if answer=='': #공백일시 aaa 넣기 5단계
        answer='aaa'
    

    if len(answer) > 15:  #16글자 이상일시 자르기
        answer=answer[:15]
    answer=answer.rstrip('.') #자르고 난 후 마침표 제거  
    while(True): #아이디가 2자 이하일시 3이 될때까지 반복해서 붙임 7단계
        if len(answer)<=2:
            answer+=answer[len(answer)-1]
        else:
            break
    return answer