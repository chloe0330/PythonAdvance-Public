# Entry 위젯
Entry(입력창)는 사용자의 입력을 받을 수 있는 한 줄로 된 문자열 박스입니다.        
한줄의 입력만을 받을 수 있으며 만약 여러줄의 입력을 원한다면 Text 위젯을 사용해야 합니다.     
Entry 옵션은 [다음](https://076923.github.io/posts/Python-tkinter-4/)에서 확인할 수 있습니다.

### Entry 사용
```python
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("Entry 사용")
# 화면 크기 변경 불가능
# window.resizable(False, False)

# 엔터를 입력하면 실행할 함수
def enter(event):
    # entry에 입력된 문자열을 가져와서 출력
    # get 함수는 input 함수와 마찬가지로 숫자를 입력해도 자료형은 항상 문자열입니다.
    print(entry.get())

entry = Entry(win)
# Entry.bind()를 이용하여 key나 mouse 등의 event를 처리하여 메서드나 함수를 실행시킬 수 있습니다.    
# Return 은 Entry 안에서 엔터를 쳤을때 발생하는 이벤트 입니다.
entry.bind("<Return>", enter)
entry.pack()

win.mainloop()
```
<img width="410" alt="스크린샷 2022-01-26 오전 10 59 43" src="https://user-images.githubusercontent.com/48852104/151091016-7fe9e31d-a6f9-432c-9b3d-d5ecb703e66f.png">     

### 문자열을 입력하고 그대로 출력
Entry 위젯에 입력한 문자열을 그대로 Lable에 출력하는 프로그램을 만들어봅시다.     
출력하는 시점은 '클릭' 버튼을 눌렀을때로 하겠습니다.     
```python
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("Entry 사용")

def change(): 
    # entry1의 text 가져오기
    txt1 = entry1.get() 
    label3.config(text = txt1) 
    
label1 = Label(win, text = "문자열 입력1 ") 
label1.grid(row=0, column=0) 
entry1 = Entry(win, width = 20, bg = "light green") 
entry1.grid(row=0, column = 1) 
button = Button(win, text = "클 릭", command = change) 
button.grid(row=2, column=1) 
label3 = Label(win, text = "입력받은 문자열이 여기에 출력됩니다") 
label3.grid(row=3, column=1)

win.mainloop()
```
<img width="400" alt="스크린샷 2022-01-26 오전 10 51 06" src="https://user-images.githubusercontent.com/48852104/151089908-1fc383b8-d163-4dcd-bace-9e4b24d5bb96.png">      
문자열을 하나 더 입력할 수 있도록 label2, entry2 를 추가하고 label3 에 이어서 출력해보세요.      
문자열을 더하기를 사용합니다.

```python
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("Entry 사용")

def change(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    label3.config(text = txt1 + " " + txt2 ) 
    
label1 = Label(win, text = "문자열 입력1 ") 
label1.grid(row=0, column=0) 
entry1 = Entry(win, width = 20, bg = "light green") 
entry1.grid(row=0, column = 1) 
label2 = Label(win, text = "문자열 입력2 ") 
label2.grid(row=1, column=0) 
entry2 = Entry(win, width = 20, bg = "light blue") 
entry2.grid(row=1, column = 1) 
button = Button(win, text = "클 릭", command = change) 
button.grid(row=2, column=1) 
label3 = Label(win, text = "입력받은 문자열이 여기에 출력됩니다") 
label3.grid(row=3, column=1)

win.mainloop()
```
<img width="403" alt="스크린샷 2022-01-26 오전 10 54 08" src="https://user-images.githubusercontent.com/48852104/151090489-7980b571-3d85-43f0-916b-54bb03c4e24c.png">     
### 사칙연산
두 수를 입력받아서 더하기(+), 빼기(-), 곱하기(\*), 나누기(/)를 계산하는 프로그램을 만들어 봅시다.           

먼저 화면을 아래처럼 만들어 보겠습니다.       

<img width="405" alt="스크린샷 2022-01-26 오전 11 09 06" src="https://user-images.githubusercontent.com/48852104/151091785-e3cdb491-0471-4a8f-9f2f-d4d8d9048bea.png">.   
3개의 label, 2개의 entry, 6개의 button이 필요합니다.    
화면 배치할때는 pack 함수를 사용해도 되지만, 이번에는 grid 함수를 사용해보겠습니다.     

```python
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("사칙 연산 프로그램")

label1 = Label(win, text = "입력 1 ") 
label1.grid(row=0, column=0) 
entry1 = Entry(win, width = 10, bg = "light green") 
entry1.grid(row=0, column = 1) 
label2 = Label(win, text = "입력 2 ") 
label2.grid(row=1, column=0) 
entry2 = Entry(win, width = 10, bg = "light blue") 
entry2.grid(row=1, column = 1) 
button1 = Button(win, text = " + ",width = 8) 
button1.grid(row=2, column=0) 
button2 = Button(win, text = " - ",width = 8) 
button2.grid(row=2, column=1) 
button3 = Button(win, text = " X ", width = 8) 
button3.grid(row=2, column=2) 
button4 = Button(win, text = " / ",width = 8) 
button4.grid(row=2, column=3) 
label3 = Label(win, text = "두 수의 계산 결과는?") 
label3.grid(row=3, column=1, columnspan=3) 
button5 = Button(win, text = " 지우기 ",width = 8) 
button5.grid(row=4, column=2) 
button5 = Button(win, text = " 종 료 ",width = 8) 
button5.grid(row=5, column=2)

win.mainloop()
```

화면은 잘 배치되었으니 버튼을 클릭할때 이벤트를 추가해봅시다.     

```python
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("사칙 연산 프로그램")

def click1(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) + int(txt2) 
    label3.config(text = (txt1) + " + " + (txt2) + " = " + str(answer)) 
def click2(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) - int(txt2) 
    label3.config(text = (txt1) + " - " + (txt2) + " = " + str(answer)) 
def click3(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) * int(txt2) 
    label3.config(text = (txt1) + " x " + (txt2) + " = " + str(answer)) 
def click4(): 
    txt1 = entry1.get() 
    txt2 = entry2.get() 
    answer = int(txt1) / int(txt2) 
    label3.config(text = (txt1) + " / " + (txt2) + " = " + str(answer)) 
def click5(): 
    label3.config(text = "두 수의 계산 결과는?") 
    # 지우기 함수
    entry1.delete(0, END) 
    entry2.delete(0, END) 
def click6(): 
    # 종료
    win.destroy() 

label1 = Label(win, text = "수 입력 1 ") 
label1.grid(row=0, column=0) 
entry1 = Entry(win, width = 10, bg = "light green") 
entry1.grid(row=0, column = 1) 
label2 = Label(win, text = "수 입력 2 ") 
label2.grid(row=1, column=0) 
entry2 = Entry(win, width = 10, bg = "light blue") 
entry2.grid(row=1, column = 1) 
button1 = Button(win, text = " + ",width = 8, command = click1) 
button1.grid(row=2, column=0) 
button2 = Button(win, text = " - ",width = 8, command = click2) 
button2.grid(row=2, column=1) 
button3 = Button(win, text = " X ", width = 8, command = click3) 
button3.grid(row=2, column=2) 
button4 = Button(win, text = " / ",width = 8, command = click4) 
button4.grid(row=2, column=3) 
label3 = Label(win, text = "두 수의 계산 결과는?") 
label3.grid(row=3, column=1, columnspan=3) 
button5 = Button(win, text = " 지우기 ",width = 8, command = click5) 
button5.grid(row=4, column=2) 
button5 = Button(win, text = " 종 료 ",width = 8, command = click6) 
button5.grid(row=5, column=2)

win.mainloop()
```
다양한 나만의 연산자 버튼을 추가해보세요.      

### 연습문제
- 아이디와 비밀번호를 입력하고 로그인 버튼을 누르면 메시지 박스에 출력되는 프로그램을 만들어보세요.
  - 비밀번호는 '\*' 로 표시하기 위해서 `show='*'` 속성을 사용합니다.     
<img width="602" alt="스크린샷 2022-01-26 오전 11 20 15" src="https://user-images.githubusercontent.com/48852104/151093084-25ee1086-88e4-49a1-ab08-6bb28b29ef9b.png">


```python
from tkinter import *
from tkinter import messagebox as msg 
win = Tk()

win.geometry("350x200") 
win.title("Login") 
def click(): 
    st1 = id2.get() 
    st2 = pw2.get() 
    msg.showinfo("로그인", "아이디 : " + st1 + "\n비밀번호 : " + st2) 

id = Label(win, text="아 이 디") 
id.place(x=60, y=40) 
id2 = Entry(win, width=20) 
id2.place(x=130, y=40) 
pw = Label(win, text="비밀번호") 
pw.place(x=60, y=80) 
pw2 = Entry(win, width = 20, show='*') 
pw2.place(x=130, y=80) 
button = Button(win, text="로그인", command = click)
button.place(x=60, y=130)

win.mainloop()
```

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


