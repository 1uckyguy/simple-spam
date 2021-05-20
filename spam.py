import os
import pyautogui
import time

#หวัดดีพวกแงะไฟล์5555555555

time.sleep(2)
print('พิมพ์ไทยไม่ได้นะ!! ผมก็ไม่รู้ว่าทำไม ผมโง่55')
time.sleep(2)
print('     Creadit : 1uckyguy     ')
print('     FB : pakasit           ')

time.sleep(2)
whattype = input('จะพิมพ์ว่าอะไร? : ')
time.sleep(2)
print("พิมพ์ว่า : " , whattype)
time.sleep(2)
message = int(input("ส่งกี่คำ? : "))
time.sleep(2)
print("ส่งจำนวน : " , message)


#ลูปแล้วนะ 
while message > 0:
    time.sleep(0.5)
    pyautogui.typewrite(whattype)
    pyautogui.press('enter')
    message = message - 1
    print('เหลืออีก : ' , message , ' คำ')

