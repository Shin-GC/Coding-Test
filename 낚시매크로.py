import pyautogui
import time
import pyperclip


time.sleep(2)
pyperclip.copy("!게임 지원금")
pyautogui.hotkey('ctrl', 'v') # 붙여넣기
pyautogui.press('enter',presses = 1)
add_time = 0
while True:
    if add_time >=121:
        pyperclip.copy("!게임 지원금")
        pyautogui.hotkey('ctrl', 'v') # 붙여넣기
        pyautogui.press('enter',presses = 1)
        add_time = 0
    
    start = time.time()
    
    time.sleep(3)
    
    pyperclip.copy("!게임 낚시")
    pyautogui.hotkey('ctrl', 'v') # 붙여넣기
    pyautogui.press('enter',presses = 1)
    #pos = pyautogui.position()
    
    end = time.time()
    add_time += (end - start)
    
    start = time.time()

    time.sleep(5)
    pyautogui.moveTo(403, 938) #게임 시작 체크
    pyautogui.click()
    time.sleep(3)

    end = time.time()
    add_time += (end - start)
    for i in range(1,12):
        start = time.time()
        time.sleep(2)
    
        pyautogui.moveTo(406, 936) #낚시 체크 좌표
        pyautogui.click()

        end = time.time()
        add_time += (end - start)
        
        if add_time >=122:
            pyperclip.copy("!게임 지원금")
            pyautogui.hotkey('ctrl', 'v') # 붙여넣기
            pyautogui.press('enter',presses = 1)
            add_time = 0

    print(add_time)

    if add_time >=122:
        pyperclip.copy("!게임 지원금")
        pyautogui.hotkey('ctrl', 'v') # 붙여넣기
        
        pyautogui.press('enter',presses = 1)
        add_time = 0

