# Radiobutton 위젯
Radiobutton(라디오버튼)을 이용하여 옵션 등을 단일 선택하기 위한 라디오버튼을 생성할 수 있습니다.           
여러 선택사항 중에서 하나만 선택이 가능합니다.     
Radiobutton 옵션은 [다음](https://076923.github.io/posts/Python-tkinter-7/)에서 확인할 수 있습니다.

### Radiobutton 사용
```python
from tkinter import *

win = Tk()
win.geometry("350x400") 
win.title("Radiobutton 위젯") 

def check():
    label.config(text= "radioVariable1 = " + str(radioVariable1.get()) + "\n" +
                       "radioVariable2 = " + str(radioVariable2.get()) + "\n\n" +
                       "Total = "          + str(radioVariable1.get() + radioVariable2.get()))

# IntVar() 그룹이 같을 경우 하나의 묶음으로 간주
# radio1, radio2, radio3은 radioVariable1로 설정된 variable 속성
# radio4, radio5는 radioVariable2로 설정된 variable 속성
# 선택된 라디오버튼의 value 값이 여기에 저장됨
radioVariable1=IntVar()
radioVariable2=IntVar()

# Radiobutton 버튼 생성
# command 를 이용하여 check 함수 실행
radio1=Radiobutton(win, text="1번", value=3, variable=radioVariable1, command=check)
radio1.pack()
# value를 이용하여 라디오버튼의 값을 설정할 수 있음(value의 값이 겹치는 경우 같이 선택)
radio2=Radiobutton(win, text="2번(1번)", value=3, variable=radioVariable1, command=check)
radio2.pack()
radio3=Radiobutton(win, text="3번", value=9, variable=radioVariable1, command=check)
radio3.pack()

label=Label(win, text="None", height=5)
label.pack()

# value 가 3이지만 IntVar가 다르기 때문에 하나의 묶음이 아니어서 같이 선택 안됨
radio4=Radiobutton(win, text="4번", value=3, variable=radioVariable2, command=check)
radio4.pack()
radio5=Radiobutton(win, text="5번", value=15, variable=radioVariable2, command=check)
radio5.pack()

win.mainloop()
```
<img width="355" alt="스크린샷 2022-01-26 오후 12 25 40" src="https://user-images.githubusercontent.com/48852104/151098977-501e4300-73e2-4eb6-9ee2-939e58de1b3a.png">

### 좋아하는 동물 선택하는 프로그램
```python
from tkinter import *

win = Tk()
win.geometry("350x400") 
win.title("좋아하는 동물 선택") 

def select1(): 
    if r1.get() == 1: 
        str1 = "고양이" 
    elif r1.get() == 2: 
        str1 = "강아지" 
    elif r1.get()==3: 
        str1 = "토끼" 
    elif r1.get()==4: 
        str1 = "햄스터" 
    select = "당신의 선택은 " + str1 +"입니다." 
    show1.config(text = select) 

r1= IntVar() 

label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물은 ? ") 
label1.pack() 
r11 = Radiobutton(win, text = "1. 고양이", variable=r1, value="1", command = select1) 
r11.pack(anchor= W) 
r12 = Radiobutton(win, text = "2. 강아지", variable=r1, value="2", command = select1) 
r12. pack(anchor= W) 
r13 = Radiobutton(win, text = "3. 토끼", variable=r1, value="3", command = select1) 
r13.pack(anchor= W) 
r14 = Radiobutton(win, text = "4. 햄스터", variable=r1, value="4", command = select1) 
r14.pack(anchor= W) 
show1=Label(win) 
show1.pack() 
line1 = Label(win, text = "---------------------------------------") 
line1.pack() 

win.mainloop()
```
<img width="352" alt="스크린샷 2022-01-26 오후 12 30 04" src="https://user-images.githubusercontent.com/48852104/151099357-0d0fad50-73be-48cb-8958-0b880ea1fb75.png">

### 좋아하는 동물/과목/음식 프로그램 
```python
from tkinter import *

win = Tk()
win.geometry("350x500") 
win.title("좋아하는 동물/과목/음식 선택") 

def select1(): 
    if r1.get() == 1: 
        str1 = "고양이" 
    elif r1.get() == 2: 
        str1 = "강아지" 
    elif r1.get()==3: 
        str1 = "토끼" 
    elif r1.get()==4: 
        str1 = "햄스터" 
    select = "당신의 선택은 " + str1 + "입니다." 
    show1.config(text = select) 
def select2(): 
    # 동물처럼 선택한 과목이 나오도록 수정해주세요.
    select = "당신의 선택은 " + str(r2.get()) + "입니다." 
    show2.config(text = select) 
def select3(): 
    # 동물처럼 선택한 음식이 나오도록 수정해주세요.
    select = "당신의 선택은 " + str(r3.get()) + "입니다." 
    show3.config(text = select) 
def end1(): 
    win.destroy() 

r1= IntVar() 
r2= IntVar() 
r3= IntVar() 

label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물은 ? ") 
label1.pack() 
r11 = Radiobutton(win, text = "1. 고양이", variable=r1, value="1", command = select1) 
r11.pack(anchor= W) 
r12 = Radiobutton(win, text = "2. 강아지", variable=r1, value="2", command = select1) 
r12. pack(anchor= W) 
r13 = Radiobutton(win, text = "3. 토끼", variable=r1, value="3", command = select1) 
r13.pack(anchor= W) 
r14 = Radiobutton(win, text = "4. 햄스터", variable=r1, value="4", command = select1) 
r14.pack(anchor= W) 
show1=Label(win) 
show1.pack() 
line1 = Label(win, text = "---------------------------------------") 
line1.pack() 

label2 = Label(win, text = "[2번 문제] 당신이 가장 좋아하는 과목은 ? ") 
label2.pack() 
r21 = Radiobutton(win, text = "1. 국어", variable=r2, value="1", command = select2) 
r21.pack(anchor= W) 
r22 = Radiobutton(win, text = "2. 수학", variable=r2, value="2", command = select2) 
r22. pack(anchor= W) 
r23 = Radiobutton(win, text = "3. 영어", variable=r2, value="3", command = select2) 
r23.pack(anchor= W) 
r24 = Radiobutton(win, text = "4. 과학", variable=r2, value="4", command = select2) 
r24.pack(anchor= W) 
r25 = Radiobutton(win, text = "5. 코딩", variable=r2, value="5", command = select2) 
r25.pack(anchor= W) 
show2=Label(win) 
show2.pack() 
line2 = Label(win, text = "---------------------------------------") 
line2.pack() 

label3 = Label(win, text = "[3번 문제] 당신이 가장 좋아하는 음식은 ? ") 
label3.pack() 
r31 = Radiobutton(win, text = "1. 치킨", variable=r3, value="1", command = select3) 
r31.pack(anchor= W) 
r32 = Radiobutton(win, text = "2. 피자", variable=r3, value="2", command = select3) 
r32.pack(anchor= W) 
r33 = Radiobutton(win, text = "3. 스파게티", variable=r3, value="3", command = select3) 
r33.pack(anchor= W) 
r34 = Radiobutton(win, text = "4. 삼겹살", variable=r3, value="4", command = select3) 
r34.pack(anchor= W) 
show3=Label(win) 
show3.pack() 

end = Button(win, text ="종 료", width=10, command=end1) 
end.pack()

win.mainloop()
```

<img width="354" alt="스크린샷 2022-01-26 오후 12 34 53" src="https://user-images.githubusercontent.com/48852104/151099790-748c888c-13a5-42e2-a638-5c8d292c779b.png">

선택사항을 추가하고, 다양한 문제들을 추가해보세요.     

### 동물 선택 프로그램 최적화
좋아하는 동물의 선택지를 늘리고 싶을때 어떻게 해야하나요?      
라디오 버튼을 추가하고, 그에 맞는 옵션을 넣은 다음에 select1 함수에서 수정을 해주어야 합니다.     
선택사항을 추가하거나 삭제하거나, 수정할때마다 이런 코드들을 모두 변경하려면 어렵겠지요?    
그래서 구조를 조금 바꾸면 훨씬 간단하게 선택사항 관리를 할 수 있게 됩니다.      
list 나 map 을 활용할 수 있는데, 오늘은 map 을 활용하여 코딩해보도록 하겠습니다.      

먼저 선택사항 리스트를 가지고 있는 map 을 생성합니다.      
그리고 select1함수에서 해당 map 을 활용하여 결과를 주도록 수정해보겠습니다.
```python
# 기존
def select1(): 
    if r1.get() == 1: 
        str1 = "고양이" 
    elif r1.get() == 2: 
        str1 = "강아지" 
    elif r1.get()==3: 
        str1 = "토끼" 
    elif r1.get()==4: 
        str1 = "햄스터" 
    select = "당신의 선택은 " + str1 +"입니다." 
    show1.config(text = select) 

# 수정 후
animal = {1: '고양이', 2: '강아지', 3: '토끼', 4:'햄스터'}
def select1(): 
    str1 = animal[r1.get()]
    select = "당신의 선택은 " + str1 +"입니다." 
    show1.config(text = select) 
```
어떤가요? 훨씬 간단하지요?      
그리고 아래 radiobuttion 생성할때도 text를 넣을때 이 map 값을 활용할 수 있을것 같습니다.     

```python
# 기존
label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물은 ? ") 
label1.pack() 
r11 = Radiobutton(win, text = "1. 고양이", variable=r1, value="1", command = select1) 
r11.pack(anchor= W) 
r12 = Radiobutton(win, text = "2. 강아지", variable=r1, value="2", command = select1) 
r12. pack(anchor= W) 
r13 = Radiobutton(win, text = "3. 토끼", variable=r1, value="3", command = select1) 
r13.pack(anchor= W) 
r14 = Radiobutton(win, text = "4. 햄스터", variable=r1, value="4", command = select1) 
r14.pack(anchor= W) 

# 수정 후
label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물은 ? ") 
label1.pack() 
r11 = Radiobutton(win, text = "1. "+animal[1], variable=r1, value="1", command = select1) 
r11.pack(anchor= W) 
r12 = Radiobutton(win, text = "2. "+animal[2], variable=r1, value="2", command = select1) 
r12. pack(anchor= W) 
r13 = Radiobutton(win, text = "3. "+animal[3], variable=r1, value="3", command = select1) 
r13.pack(anchor= W) 
r14 = Radiobutton(win, text = "4. "+animal[4], variable=r1, value="4", command = select1) 
r14.pack(anchor= W) 
```
이러면 코드 내에 '고양이', '강아지' 같은 문자열은 들어가지 않고 map에 있는 데이터만 수정하면 그대로 반영되는 것을 확인할 수 있습니다.        

그런데 버튼을 만드는 코드도 계속 반복되는것이 보이나요?       
Radiobutton을 생성하고 화면에 붙이는 코드가 계속해서 반복이 되고 있습니다.      
중간에 숫자만 바뀌는것이 구구단을 출력하는 것과 크게 다르지 않습니다.     
조금 더 수정해보겠습니다.      
```python
# 1차 수정
label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물은 ? ") 
label1.pack() 
r11 = Radiobutton(win, text = "1. "+animal[1], variable=r1, value="1", command = select1) 
r11.pack(anchor= W) 
r12 = Radiobutton(win, text = "2. "+animal[2], variable=r1, value="2", command = select1) 
r12. pack(anchor= W) 
r13 = Radiobutton(win, text = "3. "+animal[3], variable=r1, value="3", command = select1) 
r13.pack(anchor= W) 
r14 = Radiobutton(win, text = "4. "+animal[4], variable=r1, value="4", command = select1) 
r14.pack(anchor= W) 

# 2차 수정
for i in range(1, 5, 1):
    r11 = Radiobutton(win, text = str(i)+". "+animal[i], variable=r1, value=i, command = select1) 
    r11.pack(anchor= W) 
```
버튼을 생성하는데에 반복문을 사용했습니다.      

> range 함수는 예전에 배웠는데 기억 나나요?
> range(초기값, ~하는 동안, 순환할 때마다 증가하는 값)
> 즉, 위 코드에서는 1부터 5가 되기 전까지 1씩 증가하는 숫자 리스트를 반복하게 됩니다.
> 1, 2, 3, 4 가 되겠지요.

훨씬 간단해졌습니다.    
아래는 전체 코드입니다.
```python
from tkinter import *

win = Tk()
win.geometry("350x400") 
win.title("좋아하는 동물 선택") 

animal = {1: '고양이', 2: '강아지', 3: '토끼', 4:'햄스터', 5:'새'}

def select1(): 
    str1 = animal[r1.get()]
    select = "당신의 선택은 " + str1 +"입니다." 
    show1.config(text = select) 

r1= IntVar() 

label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물은 ? ") 
label1.pack() 
# 파이썬의 len함수는 객체에 있는 총 항목 수를 반환하는 데 사용됩니다.
# animal 객체가 늘어나고 줄어든만큼 반복문을 돌리도록 해주었습니다.
for i in range(1, len(animal)+1, 1):
    r11 = Radiobutton(win, text = str(i)+". "+animal[i], variable=r1, value=i, command = select1) 
    r11.pack(anchor= W) 
show1=Label(win) 
show1.pack() 
line1 = Label(win, text = "---------------------------------------") 
line1.pack() 

win.mainloop()
```

### 연습문제
- 좋아하는 것을 선택하는 프로그램을 최적화해봅시다.
  - 과목, 음식도 같은 방법으로 만들어보세요.
```python
animal = ['고양이', '강아지', '토끼', '햄스터', '새']
```

- 좋아하는 것을 선택하는 프로그램을 최적화해봅시다.
  - list로 구현해보세요.
```python
animal = ['고양이', '강아지', '토끼', '햄스터', '새']
```

- 동물 선택사항을 추가할 수 있는 프로그램으로 발전시켜봅시다.
  - 동물을 입력할 수 있는 Entry 와 버튼이 필요합니다.
  - 버튼을 클릭하면 map 혹은 list에 항목을 추가하고, 그에 맞는 버튼을 추가합니다.
  - 그 외에 필요한 변수가 있다면 마음껏 추가해보세요.
  - <img width="354" alt="스크린샷 2022-01-26 오후 1 20 23" src="https://user-images.githubusercontent.com/48852104/151103398-1dda35ea-7981-459b-8cdb-89c4c74c77b2.png">
```python
# 참고
label = Label(win, text = "추가하고 싶은 동물을 입력해주세요.") 
label.pack() 
entry = Entry(win, width = 20, bg = "light green") 
entry.pack() 
button = Button(win, text = "클 릭", command = change) 
button.pack() 
```

- 컴퓨터와 하는 가위바위보 게임을 만들어보세요.
  - 화면은 상관 없습니다.
  - 시나리오
    - 가위, 바위, 보 세개 중 하나를 선택하라는 안내 문구를 label로 출력한다.
    - Radiobox 를 활용하여 가위, 바위, 보를 선택할 수 있도록 한다.
    - 사용자는 하나를 선택하여 '제출' Button을 누른다.
    - 컴퓨터의 값을 랜덤으로 선택하고 사용자에게 알려준다.
    - 승리했는지 패배했는지 검사한다.
    - 결과를 출력해준다.
  - 1주차때 했던 코드를 참고해봅시다.
  - 그림을 넣을 수도 있습니다.



