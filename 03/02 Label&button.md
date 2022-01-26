# Label 위젯
Label은 텍스트 혹은 이미지를 표시하기 위한 위젯입니다.     
Label 옵션은 [다음](https://076923.github.io/posts/Python-tkinter-2/)에서 확인할 수 있습니다.    

### label 사용
```python
from tkinter import *
win = Tk()

win.geometry("400x400")
win.title("Label 사용")

# label 생성
label1 = Label(win, text = "파이썬 공부하기", font=("궁서체","24"), 
               width=25, height=4, anchor=S, 
               foreground="red", background="blue") 
label1.pack() 

win.mainloop()
```
label 위젯을 생성하고 다양한 옵션을 추가해주었습니다.        
<img width="402" alt="스크린샷 2022-01-19 오전 11 03 50" src="https://user-images.githubusercontent.com/89170523/150049767-025fef73-723a-4440-a550-3e769ae8dc78.png">
text에 원하는 문자열을 넣고, 궁서체 24크기로 폰트를 설정해 주었습니다.    
그리고 가로 24, 세로 4, 글씨색은 빨간색, 배경색은 파란색으로 해주었습니다.    
그리고 anchor는 위치를 잡아주는 옵션입니다.     
amchor 옵션은 사용되지 않은 공간을 기준으로 합니다.    
즉, 우측에 빈공간이 생기면 이 빈공간의 중앙 상, 하, 좌 ,우에 위치합니다    
> S / E / N / W / SE / SW / NE / NW / CENTER 값이 들어갈 수 있습니다.     
> E는 오른쪽 S는 왼쪽, S는 아래, N은 위를 의미합니다. (동east 서west 남south 북north)

### 이미지 출력
```python
from tkinter import *

win = Tk()
win.geometry("800x600")
win.title("Label 사용")

label1 = Label(win, text= "귀여운 강아지 사진" ,font=("굴림체", "20")) 
label1.pack() 

img = PhotoImage(file = "dog.png") 
label2 = Label(win, image = img) 
label2.pack() 

win.mainloop()
```
<img width="808" alt="스크린샷 2022-01-19 오전 11 19 51" src="https://user-images.githubusercontent.com/89170523/150051388-31f68331-fb1a-4636-93cc-354d6ff21102.png">    
label1에는 '귀여운 강아지 사진' 이라는 문구를 출력하고, label2에는 강아지 이미지를 출력하였습니다.      
어려운 코드가 아니지요?     

# Button 위젯
Button은 말 그대로 버튼를 위한 위젯입니다.      
버튼을 만드는 목적은 어떤 기능의 구현이고, 사용자에게 버튼의 기능에대해서 알려주기 위해서는 기능을 설명해주는 문구나 기호기 필요합니다.   

### label 사용
```python
from tkinter import *
win = Tk()

win.geometry("400x400")
win.title("Button 사용")

def alert():
    print("버튼이 눌림")

# 버튼 생성
btn = Button(win)
# 버튼 크기
btn.config(width = 20, height = 20)
# 버튼 내용
btn.config(text = "버튼")
# 버튼 기능
btn.config(command = alert)
# 버튼 배치
btn.pack() 

win.mainloop()
```
Button 위젯을 생성하고 다양한 옵션을 추가해주었습니다.        
버튼 크기는 가로 20, 세로 20으로 정하고 text에 원하는 문자열을 넣어 버튼에 나오게 만들어 주었습니다.     
command 라는 속성은 버튼을 눌렀을때 발생할 일을 미리 함수 형태로 넣어줄 수 있습니다.    
alert이라는 이름의 함수를 생성하였는데요, 함수에서는 '버튼이 눌림' 문자열을 출력하게 합니다.    
실행을 하면 버튼을 눌렀을때 문구가 출력되는것을 확인할 수 있습니다.

![스크린샷 2022-01-19 오후 12 41 50](https://user-images.githubusercontent.com/89170523/150059894-8f3bf412-3c12-49de-88fb-8a652f99bc7f.png)

### 현재 시간 출력
```python
from tkinter import *
# 현재 시각을 출력하기위한 모듈
from datetime import datetime

win = Tk()
win.geometry("400x400")
win.title("현재 시각")

def time():
    print(datetime.now())

# 버튼 생성
btn = Button(win)
btn.config(width = 20, height = 10)
btn.config(text = "현재 시각")
btn.config(command = time)
# 버튼 배치
btn.pack() 

win.mainloop()
```
```python
# 필요시 설치
pip install datetime
```
![스크린샷 2022-01-19 오후 12 47 06](https://user-images.githubusercontent.com/89170523/150060400-07ea0600-a2e6-4861-b1c8-73d47e429ef6.png)     
잘 출력이 되는것을 확인할 수 있습니다.      
그런데 프로그램을 만들게 되면 아래 코드가 없는 상태에서 이 프로그램 내에서 해결을 해야겠지요?       
버튼을 클릭하면 버튼의 text에 현재 시각이 나오면 어떨까요?     
코드를 조금 수정하면 금방 적용할 수 있습니다.     
```python
from tkinter import *
from datetime import datetime

win = Tk()
win.geometry("400x400")
win.title("현재 시각")

def time():
    # 현재 시각 변수에 저장
    now = datetime.now()
    # 버튼의 text를 변경
    btn.config(text = now)

# 버튼 생성
btn = Button(win)
btn.config(width = 30, height = 5)
btn.config(text = "현재 시각")
btn.config(command = time)
# 버튼 배치
btn.pack() 

win.mainloop()
```
![스크린샷 2022-01-19 오후 12 52 27](https://user-images.githubusercontent.com/89170523/150060887-adec7da6-f53a-4144-99f2-ff6ddedf81f5.png)


# 이미지 변경 프로그램
조금 전에 코드에 버튼 위젯을 추가해서 버튼을 누르면 거북이 이미지로 변경되게 해보겠습니다.     

```python
from tkinter import *

win = Tk()
win.geometry("800x800")
win.title("이미지 변경")

# 이미지를 변경하는 함수 정의
def change(): 
    label1.config(text = "귀여운 거북이 사진") 
    label2.config(image = turtle)

label1 = Label(win, text= "귀여운 강아지 사진" ,font=("굴림체", "20")) 
label1.pack() 

# 강아지 사진
dog = PhotoImage(file = "dog.png") 
# 거북이 사진
turtle = PhotoImage(file = "turtle.png") 
# 처음은 강아지 사진
label2 = Label(win, image = dog) 
label2.pack() 

# 버튼을 클릭하면 change 함수 호출
button1 = Button(win, text="거북이 사진", command = change) 
button1.pack() 

win.mainloop()
```
label1, label2 의 값을 변경해주는 change 라는 함수를 추가했습니다.    
config 함수를 사용해서 label1은 문구를 변경해주고, label2는 이미지를 변경해 주었네요.     
그리고 강아지, 거북이 이미지를 불러오고 처음에는 강아지 이미지로 label2를 설정해줍니다.     
여기서 버튼을 보면 command 라는 옵션이 사용되었는데, 버튼을 클릭하면 command 에 있는 함수가 자동으로 실행이 되게 됩니다.      
즉, 버튼을 클릭하게 되면 위에 선언해준 change 함수가 실행되어 label1, label2의 속성을 변경하게 되는 것이지요.    
아래 실행 예시를 봅시다.       
<img width="798" alt="스크린샷 2022-01-19 오전 11 37 01" src="https://user-images.githubusercontent.com/89170523/150053159-586759af-bf91-4984-a71c-60617b5df148.png">
<img width="794" alt="스크린샷 2022-01-19 오전 11 37 09" src="https://user-images.githubusercontent.com/89170523/150053173-5056dae1-e946-475c-abaf-ee65d959dc49.png">

그러면 다시 강아지 사진으로 바꾸는 버튼도 추가로 코딩해보도록 하겠습니다.       
1. 강아지 사진으로 바꾸는 함수를 추가
2. button2 추가
3. button2 command 와 함수 연결
위 세 가지 작업만 해주면 되겠네요.    
```python
from tkinter import *

win = Tk()
win.geometry("800x800")
win.title("Label 사용")

# 이미지를 변경하는 함수 정의
def changeDog(): 
    label1.config(text = "귀여운 강아지 사진") 
    label2.config(image = dog)
def changeDog(): 
    label1.config(text = "귀여운 거북이 사진") 
    label2.config(image = turtle)

label1 = Label(win, text= "귀여운 강아지 사진" ,font=("굴림체", "20")) 
label1.pack() 

dog = PhotoImage(file = "dog.png") 
turtle = PhotoImage(file = "turtle.png") 
label2 = Label(win, image = dog) 
label2.pack() 

# 버튼을 클릭하면 change 함수 호출
button1 = Button(win, text="거북이 사진", command = changeDog) 
button1.pack() 
button2 = Button(win, text="강아지 사진", command = changeDog) 
button2.pack() 

win.mainloop()
```

#### 이미지를 불러올때 오류가 발생한다면?
png 이미지가 아닌 경우 이미지를 가져오는데 실패할 수 있습니다.   
이때는 추가로 모듈을 불러와서 사용해야합니다.     
아래는 PIL 모듈을 사용한 예제입니다.
> ```python
> # jpg 이미지일 경우
> # PIL 사용하기 위해 설치
> pip install pillow
> 
> # 코드
> from tkinter import *
> from PIL import ImageTk, Image
> 
> win = Tk()
> 
> win.geometry("400x400")
> win.title("Label 사용")
> 
> label1 = Label(win, text= "귀여운 강아지 사진" ,font=("굴림체", "20")) 
> label1.pack() 
> 
> img = ImageTk.PhotoImage(Image.open("dog.png"))  # PIL solution
> label2 = Label(win, image = img) 
> label2.pack() 
> 
> win.mainloop()
> ```

### 연습문제
- 버튼을 클릭하여 배경색을 바꾸는 프로그램을 작성해보세요.
  - 아래 코드의 빈칸을 채워봅시다.
```python
from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("배경색 바꾸기")

#버튼1 함수 
def click1(): 
    win.configure(background='red') 
#버튼2 함수 

#버튼3 함수 

#버튼4 함수 

#레이블 출력 
Label1 = Label(win, text = "버튼을 클릭해서 바탕화면의 색을 바꿔보세요!") 
Label1.pack() 

#버튼1 
Button1 = Button(win, text="빨간색", width=7, command=click1) 
Button1.pack() 
#버튼2 

#버튼3

#버튼4 


#메인 반복문 실행
win.mainloop()
```

<img width="406" alt="스크린샷 2022-01-19 오전 11 45 42" src="https://user-images.githubusercontent.com/89170523/150054147-d7d1c28d-8e4c-4802-820b-3c20fff80756.png">

- 위에서 코딩한 현재 시간 출력 프로그램에서 현재 시각이 button이 아니라 label 에 출력되도록 수정해보세요.
  - 아래 코드의 빈칸을 채워봅시다.
```python
from tkinter import *
from datetime import datetime

win = Tk()
win.geometry("400x400")
win.title("현재 시각")

def time():
    # 현재 시각 변수에 저장
    now = datetime.now()
    # label의 text 변경


btn = Button(win)
btn.config(width = 30, height = 5)
btn.config(text = "현재 시각")
btn.config(command = time)
btn.pack() 

# label 생성

win.mainloop()
```

- 1주차에 만들었던 음식 추천 프로그램을 활용하여 GUI 프로그래밍을 해봅시다.
   - 추천이 가능한 음식 종류가 label 위젯에 출력됩니다.
   - '추천' 버튼을 누르면 랜덤으로 음식 하나가 선택되어 화면에 노출됩니다.
