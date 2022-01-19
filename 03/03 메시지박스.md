# Messagebox
메시지 박스는 사용자에게 추가 정보나 경고, 오류 발생여부에 대해서 피드백을 제공하기 위해서 기존의 윈도우에서 독립적인 추가 윈도우를 말합니다.        
이는 messagebox 모듈을 임포트 하기만 하면 간단하게 생성하고 조작할 수 있습니다.      

### messagebox 사용
```python
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("Messagebox 사용")

# 상자 종류와 내용만 바꾸며 메시지 상자가 바뀌게 됩니다.
# tkinter.messagebox.상자종류("제목","내용")
tkinter.messagebox.showinfo("제목", "메시지 내용")

win.mainloop()
```
<img width="269" alt="스크린샷 2022-01-19 오전 11 55 30" src="https://user-images.githubusercontent.com/89170523/150055245-15ad1d78-a890-4420-8796-24af48ce1ad9.png">

### messagebox 종류
- showinfo : 평범한 정보
- showwarning : 경고
- showerror : 오류
- askquestion : 사용자에게 질문
- askokcancel : 사용자에게 질문 (대답 ok / cancel)
- askyesno : 사용자에게 질문 (대답 yes / no)
- askretrycancel : 사용자에게 질문 (대답 retry / cancel)
<img width="554" alt="스크린샷 2022-01-19 오전 11 56 48" src="https://user-images.githubusercontent.com/89170523/150055399-28a294d7-06c4-4e8b-98ba-813f964610a5.png">
<img width="553" alt="스크린샷 2022-01-19 오전 11 57 13" src="https://user-images.githubusercontent.com/89170523/150055444-2503a6cb-66cc-49b7-a693-d1047cf03f41.png">

버튼을 생성하여 다양한 메시지 박스를 사용해봅시다.      
```python
from tkinter import * 
from tkinter import messagebox as msg 
window = Tk() 
window.geometry('300x500') 
window.title("메세지박스") 
#버튼1 함수 
def msg1(): 
    msg.showinfo("메시지박스","메세지박스 \n연습입니다\n(파란 느낌의 아이콘)") 
#버튼2 함수 
def msg2(): 
    msg.showwarning("메시지박스","메세지박스 \n연습입니다\n(노란 느낌의 아이콘)") 
#버튼3 함수 
def msg3(): 
    msg.showerror("메시지박스","메세지박스 \n연습입니다\n(빨강 엑스 아이콘)") 
#버튼4 함수 
def msg4(): 
    msg.askquestion("메시지박스","메세지박스 \n연습입니다\n(파란 물음표)\n (Yes/No)") 
#버튼5 함수 
def msg5(): 
    msg.askokcancel("메시지박스","메세지박스 \n연습입니다\n(파란 물음표)\n (Yes/Cancel)") 
#버튼6 함수 
def msg6(): 
    msg.askyesno("메시지박스","메세지박스 \n연습입니다\n(파란 물음표)\n (Yes/No)") 
#버튼7 함수 
def msg7(): 
    msg.askretrycancel("메시지박스","메세지박스 \n연습입니다\n(파란 물음표)\n (Try/Cancel)") 
#버튼8 함수 
def msg8(): 
    # 프로그램 창 종료
    window.destroy()
    window.quit() 
    
#버튼 만들기1 
Bu1=Button(window, text="클릭(info)", width = 10, command=msg1) 
Bu1.pack(pady=5) 
#버튼 만들기2 
Bu2=Button(window, text="클릭(warning)", width = 10, command=msg2) 
Bu2.pack(pady=5) 
#버튼 만들기3 
Bu3=Button(window, text="클릭(error)", width = 10, command=msg3) 
Bu3.pack(pady=5) 
#버튼 만들기4 
Bu4=Button(window, text="클릭(question)", width = 15, command=msg4) 
Bu4.pack(pady=5) 
#버튼 만들기5 
Bu5=Button(window, text="클릭(Yes/Cancel)", width = 15, command=msg5) 
Bu5.pack(pady=5) 
#버튼 만들기6 
Bu6=Button(window, text="클릭(Yes/No)", width = 15, command=msg6) 
Bu6.pack(pady=5) 
#버튼 만들기7 
Bu7=Button(window, text="클릭(Try)", width = 10, command=msg7) 
Bu7.pack(pady=5) 
#버튼 만들기8 
Bu8=Button(window, text="종료", width = 10, command=msg8) 
Bu8.pack(pady=5) 
#메인 반복문 실행 
window.mainloop()
```
<img width="304" alt="스크린샷 2022-01-19 오후 12 05 33" src="https://user-images.githubusercontent.com/89170523/150056306-8e09c1cb-8f2a-49b8-8e6f-90e3ba437fd7.png">

### ask messagebox 응답
ask 메시지박스는 사용자의 응답을 return 해주는 기능도 가지고 있습니다.     
'파이썬을 종료할까요?' 문구를 띄우고, '예' 버튼을 누르면 파이썬이 종료되고 '아니오' 버튼을 누르면 아무 동작도 하지 않도록 코딩해봅시다.     
askquestion 메시지박스를 사용하도록 하겠습니다.    
```python
from tkinter import * 
from tkinter import messagebox as msg 

window = Tk() 
window.geometry('300x500') 
window.title("메세지박스") 

def msg1(): 
    # return받은 사용자의 응답을 str 변수에 저장
    str = msg.askquestion("메시지상자","파이썬을 종료할까요?") 
    if str == 'yes': 
        window.destroy() 
    else: 
        msg.showinfo("메시지상자","취소버튼을 \n누르셨습니다") 

def msg2(): 
    window.destroy() 
    window.quit() 

#버튼 만들기1 
Bu1=Button(window, text="클릭", width = 10, command=msg1) 
Bu1.pack(pady=5) 
#버튼 만들기2 
Bu2=Button(window, text="종료", width = 10, command=msg2)
Bu2.pack(pady=5)

#메인 반복문 실행 
window.mainloop()
```
<img width="314" alt="스크린샷 2022-01-19 오후 12 24 19" src="https://user-images.githubusercontent.com/89170523/150058214-4a6e7c45-42b4-4f33-8748-e135cccf4a1b.png">


