import requests
import os

start_over=None


while start_over!='N':
    os.system("cls")
    
    print("Welcome to IsItDown.py!")
    url = input('please write a URL or URLs you wnat to check.\n') #url input
    
    url_list = url.split(',') #쉼표를 기준으로 문자열 나누기
    url_list=[check.strip() for check in url_list] #공백 제거

    for check in url_list:
        http_check=check[:7]
        try:
            if http_check != 'http://':
                check=f'http://{check}'
                result = requests.get(check)
            
            else:
                result = requests.get(check)

            if result.status_code == requests.codes.ok:
                print(f"{check} is up!")
        except:
            print(f"{check} is down!")

    start_over = input("Do you want to start over? (Y/N)")
    start_over.lower()
    
    while True:
        if start_over != 'y' and start_over != 'n':
            print('Please input again [Only use Y or N]')
            start_over = input("Do you want to start over? (Y/N)")
            start_over.lower()
        else:
            break
    
    if start_over == 'n':
        print("\n Goob Bye")
        break

#result.status_code == requests.codes.ok:
#print(result.status_code)


