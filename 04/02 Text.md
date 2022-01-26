
# Text 위젯
Text(텍스트)는 여러 줄로 된 문자열을 출력하기 위한 박스입니다.        
여러줄의 입력도 가능합니다.     
Text 옵션은 [다음](https://076923.github.io/posts/Python-tkinter-18/)에서 확인할 수 있습니다.

### Text 사용
```python
from tkinter import *
win = Tk()

win.geometry("350x200") 
win.title("Text 위젯") 

def click1(): 
    # entry에 입력된 문자열을 가져와서 출력
    # get 함수는 input 함수와 마찬가지로 숫자를 입력해도 자료형은 항상 문자열입니다.
    result1 = txt.get("1.0", "end") 
    print(result1) 
def click2(): 
    txt.delete(0.0, END) 
def click3(): 
    win.destroy() 

label1= Label(win, text="텍스트 박스에 문자열 입력이 가능합니다.") 
label1.pack() 
# 텍스트 위젯 생성
txt = Text(win, height=5, foreground="blue", background="light green", font="궁서체") 
txt.pack() 
button1 = Button(win, text="출 력", height=1, width=10, command=click1) 
button1.pack() 
button2 = Button(win, text="지우기", height=1, width=10, command=click2) 
button2.pack() 
button3 = Button(win, text="종 료", height=1, width=10, command=click3) 
button3.pack()

win.mainloop()
```

<img width="357" alt="스크린샷 2022-01-26 오전 11 39 33" src="https://user-images.githubusercontent.com/48852104/151094894-006599ae-5035-4150-b38d-b96a4f91e3be.png">

### 연습문제
- 제목과 본문을 모두 입력하고 '등록' 버튼을 누르면 그대로 label에 출력되는 게시판 프로그램을 만들어보세요.
  - 제목은 Entry 위젯, 본문은 Text 위젯, 등록버튼은 Button 위젯입니다.
  - 제목이 비어있다면 '제목을 입력해주세요.' 문자열을 메시지 박스로 출력해주세요.
  - 본문이 비어있다면 '본문을 입력해주세요.' 문자열을 메시지 박스로 출력해주세요.
  - 문자열이 비어있는지 확인하기 위해서 `not` 키워드를 사용합니다.
<img width="352" alt="스크린샷 2022-01-26 오전 11 54 55" src="https://user-images.githubusercontent.com/48852104/151096320-dd5db1e6-e409-4728-a1f4-18d6c61d198b.png">      

```python
from tkinter import *
from tkinter import messagebox as msg 

win = Tk()
win.geometry("350x800") 
win.title("Text 위젯") 

def click1(): 
    title = entry.get() 
    contents = txt.get("1.0", "end").strip()
    if not title:
        msg.showinfo("메시지박스","제목을 입력해주세요.") 
        return
    elif not contents :
        msg.showinfo("메시지박스","본문을 입력해주세요.") 
        return
    label2.config(text = title) 
    label3.config(text = contents) 

def click2(): 
    entry.delete(0, END) 
    txt.delete(0.0, END) 

def click3(): 
    win.destroy() 

label1= Label(win, text="제목과 본문을 모두 입력하세요.") 
label1.pack() 
entry = Entry(win, width=100, foreground="blue", background="light blue", font="궁서체") 
entry.pack() 
txt = Text(win, height=5, foreground="green", background="light green") 
txt.pack() 
button1 = Button(win, text="출 력", height=1, width=10, command=click1) 
button1.pack() 
button2 = Button(win, text="본문 지우기", height=1, width=10, command=click2) 
button2.pack() 
button3 = Button(win, text="종 료", height=1, width=10, command=click3) 
button3.pack()

label2= Label(win, text="제목출력", background="light blue") 
label2.pack() 
label3= Label(win, text="본문출력", background="light green") 
label3.pack() 

win.mainloop()
```

- 사칙연산 프로그램을 확장하여 나만의 계산기 프로그램을 만들어보세요.   
  - ![스크린샷 2022-01-26 오후 12 01 10](https://user-images.githubusercontent.com/48852104/151096888-f57fd128-fe48-4238-9a92-9d5a28670730.png)      
