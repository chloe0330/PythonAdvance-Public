# GUI란?
그래픽 사용자 인터페이스(**G**raphical **U**ser **I**nterface, GUI).     
사용자가 편리하게 사용 가능한 입출력 기능을 가진 프로그램을 아이콘, 그래픽등으로 나타낸 것입니다.         
사용자가 화면에 있는 여러 위젯(버튼, 텍스트 입력창, 라벨 등)을 이용하여 보다 편리하게 프로그램 사용이 가능합니다.      
> 컴퓨터를 사용하는 것도 그래픽으로 이루어진 화면이니 GUI 라고 할 수 있습니다.     
> 화면에 보여지는 것이 없고 텍스트로만 이루어져 있다고 생각하면 컴퓨터도 사용하기 무척 어렵겠지요.     

우리가 파이썬을 코딩하면 검은색 창에다 텍스트를 입력하는 것 외에 화면에 보이는 것이 없었지요?       
그렇게 프로그램을 제작하면 다른 사람들이 사용하기에 불편할 수 있습니다.      
GUI 프로그래밍을 통해 사용자 친화적인 프로그램을 코딩할 수 있습니다.        

<img width="779" alt="스크린샷 2022-01-19 오전 10 15 33" src="https://user-images.githubusercontent.com/89170523/150045101-231ee91f-b060-4af5-a021-6a9c32b6b515.png">

파이썬에서는 GUI 작업을 쉽게 하기 위해서 **tkinter(tk interface)** 를 제공합니다.        
Python 설치시 기본적으로 내장되어 있는 파이썬 표준 라이브러리이기 때문에 쉽고 간단한 GUI 프로그램을 만들 때 활용될 수 있습니다.       

### GUI 프로그래밍
GUI 프로그래밍은 프로그램의 겉모습을 만드는 것입니다.    
프로그램의 간단한 모습을 살펴보면, 프로그램을 켰을때 나오는 전체 창이 있습니다.     
그리고 그 안에 여러가지 기능을 가진 위젯이 들어가게 됩니다.     
위젯은 부품이라는 뜻을 가지고 있습니다.    
전체 창을 하나의 장치라고 본다면 위젯은 그 안에서 세부적인 기능을 하는 부품이 되겠죠.    

<img width="730" alt="스크린샷 2022-01-19 오전 10 19 10" src="https://user-images.githubusercontent.com/89170523/150045558-5740546d-2d9a-408c-847a-4d774ae5c086.png">    

### Window
아래 코드를 실행해 보겠습니다.    

```python
# tkinter 에서 제공하는 함수를 모두 들고오겠다.
from tkinter import *
# 창 생성
win = Tk()

# 만든 창 실행 (메인 반복문)
win.mainloop()
```
<img width="218" alt="스크린샷 2022-01-19 오전 10 22 18" src="https://user-images.githubusercontent.com/89170523/150045901-844f5adc-d397-4884-82c1-273ac5247f14.png">

위처럼 창으로 된 프로그램이 하나 생성되는 것을 확인할 수 있습니다.      
여기까지가 창을 만들기 위한 가장 기본적인 코드입니다.     
추가적으로 다양한 기능들을 추가할 수 있습니다.    
```python
from tkinter import *
win = Tk()

# 창 크기
win.geometry("1000x1000")
# 창 제목
win.title("고래코딩")
# 전체 폰트
win.option_add("*Font", "맑은고딕 25")
# 배경색 바꾸기
win.configure(background='purple')

win.mainloop()
```
<img width="1002" alt="스크린샷 2022-01-19 오전 10 39 03" src="https://user-images.githubusercontent.com/89170523/150047399-c238c96c-d0cf-412c-a748-5a29a0ab32ae.png">
이런 기능들을 모두 외울 필요는 없습니다.    
원하는 기능이 있다면 검색하여 찾아서 언제든 추가할 수 있습니다.        

### 간단한 다이얼로그 만들기
프로그램창을 만들었으니 이제 위젯으로 창 내부를 채워봅시다.    
아래와 같은 간단한 프로그램을 만들어 보겠습니다.    
이 프로그램은 하나의 레이블, 하나의 텍스트박스, 하나의 버튼을 가지고 있습니다.      
```python
from tkinter import *
win = Tk()

win.geometry("400x400")
win.title("고래코딩")
win.option_add("*Font", "맑은고딕 25")

# "이름" 이라는 레이블(Label 위젯)
lbl = Label(win, text="이름")
lbl.pack()

# 텍스트박스(Entry 위젯)
txt = Entry(win)
txt.pack()
 
# OK 버튼(Button 위젯)
btn = Button(win, text="OK")
btn.pack()

win.mainloop()
```
위젯들은 보통 win 객체 생성(win = Tk())과 win.mainloop() 사이에 생성합니다.     
<img width="405" alt="스크린샷 2022-01-19 오전 10 29 33" src="https://user-images.githubusercontent.com/89170523/150046511-ce6b3836-c197-40aa-8c9c-64fe56ef40c1.png">      
그 외에도 다양한 기능들을 추가할 수 있습니다.     
간단한 GUI 프로그래밍을 해보았습니다.     

### 위젯 배치
Tkinter에서 위젯들을 화면에 배치하는 방식에는 다음과 같은 3가지 방식이 있습니다.(Geometry Manager)     
- Place(absolute) : 위젯을 위치를 절대 좌표로 정하는 것으로, 윈도우 크기 변경에 따라 위젯들이 변경되지 않으므로 많이 사용되지 않습니다. 
   - 이 방식은 위젯.place() 메서드를 사용합니다.
- Pack : 위젯들을 부모 위젯에 모두 패킹하여 불필요한 공간을 없앱니다. 
   - 위젯.pack() 메서드를 사용합니다.
   - 하나의 위젯이 한 줄을 다 차지합니다.
- Grid : 위젯들을 테이블 레이아웃에 배치하는 것으로 지정된 row, column에 위젯을 놓습니다. 
   - 위젯.grid() 메서드를 사용합니다.
   - 공간을 나누어 한 줄에 여러개의 위젯을 배치할 수 있습니다.

위의 예제에서는 pack 방식을 사용하여 위젯들이 상하(디폴트)로 패킹되었음을 보았습니다.     
아래 예제는 grid 방식으로 위젯을 배치하는 예입니다.      
grid() 메소드에서 row와 column을 정해 주면, 해당 위치에 위젯이 놓이게 됩니다.

```python
from tkinter import *
win = Tk()

win.geometry("400x400")
win.title("고래코딩")
win.option_add("*Font", "맑은고딕 25")

# "이름" 이라는 레이블(Label 위젯)
lbl = Label(win, text="이름")
lbl.grid(row=0, column=0)

# 텍스트박스(Entry 위젯)
txt = Entry(win)
txt.grid(row=0, column=1)
 
# OK 버튼(Button 위젯)
btn = Button(win, text="OK")
btn.grid(row=1, column=1)

win.mainloop()
```
<img width="404" alt="스크린샷 2022-01-19 오전 10 44 17" src="https://user-images.githubusercontent.com/89170523/150047932-9885683f-f6f0-498f-b1e0-c4f310884f92.png">

pack 은 간단하게 화면을 구성하는 방식의 차이라는 것만 이해하고 넘어가도록 하겠습니다.      
화면을 직접 구성하면서 더 알아봅시다.   

### Tkinter 위젯
Tkinter는 제한된(Limited) 핵심 위젯들만을 제공하고 있습니다.     
아래는 Tkinter가 제공하는 주요 위젯들입니다.

|위젯|설명|
|------|---|
|Button	|단순한 버튼|
|Label	|텍스트 혹은 이미지 표시|
|CheckButton	|체크박스|
|Entry	|단순한 한 라인 텍스트 박스|
|ListBox	|리스트 박스|
|RadioButton	|옵션 버튼|
|Message	|Label과 비슷하게 텍스트 표시. Label과 달리 자동 래핑 기능이 있다.|
|Scale	|슬라이스 바|
|Scrollbar	|스크롤 바|
|Text	|멀티 라인 텍스트 박스로서 일부 Rich Text 기능 제공|
|Menu	|메뉴 Pane|
|Menubutton	|메뉴 버튼|
|Toplevel	|새 윈도우를 생성할 때 사용. Tk()는 윈도우를 자동으로 생성하지만 추가로 새 윈도우 혹은 다이얼로그를 만들 경우 Toplevel를 사용|
|Frame	|컨테이너 위젯. 다른 위젯들을 그룹화할 때 사용|
|Canvas	|그래프와 점들로 그림을 그릴 수 있으며, 커스텀 위젯을 만드는데 사용될 수도 있다|


