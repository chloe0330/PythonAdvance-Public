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

entry = Entry(win)
entry.pack()

win.mainloop()
```
<img width="401" alt="스크린샷 2022-01-26 오전 10 39 25" src="https://user-images.githubusercontent.com/48852104/151088837-19caf154-2c20-42f4-90dd-b594a8702de6.png">

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







