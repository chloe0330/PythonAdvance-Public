# turtle
### turtle 모듈
turtle 모듈은 파이썬에서 기본적으로 제공하는 기본 모듈로 코드에 따라 그림을 그려주는 모듈입니다.       
random 모듈과 마찬가지로 turtle 모듈도 기본 모듈이므로, 별도의 설치과정 없이 import 만으로 바로 사용할 수 있습니다.       
turtle 모듈을 사용하여 다양한 그림을 그려보겠습니다.

### 사용방법
random 모듈을 사용하기 위해서 어떻게 했는지 기억 나나요?     
맞아요! 맨 윗부분에 import turtle을 입력해 줍니다.      
turtle 모듈안의 코드들을 사용하겠다고 맨 처음 알려주는 것입니다.     

```python
import turtle
turtle.shape('triangle')

# turtle 이라는 모듈을 t라는 이름으로 사용할 수 있습니다.
import tutle as t
t.shape('triangle')

# turtle 모듈을 앞에 붙이고 싶지 않다면 아래 형태로도 사용이 가능합니다.
from turtle import *
shape('triangle')
```

### 간단한 프로젝트
turtle 모듈을 임포트했으니 이제 프로그램을 코딩해 보겠습니다.    
간단하게 원을 그리는 코드를 작성해 볼게요.

```python
import turtle

# 원 그리기(괄호 안의 숫자는 반지름)
turtle.circle(100)
```
실행하면 원이 그려지는 것을 확인할 수 있습니다.

그런데 그림이 생성되고 나서 바로 창이 닫혀서 사라져 버리네요.       
프로그램도 `while True`(무한루프)를 넣지 않으면 검은 창에서 바로 끝나버리게 되지요?      
우리가 만든 간단한 이 프로그램도 마찬가지입니다.     
코드의 맨 마지막에 mainloop() 를 추가하면 창이 닫히지 않습니다.     
`while True`와 비슷하게 프로그램이 종료되어 창이 닫히지 않게 하는 역할을 합니다.      
> turtle.done() 도 사용이 가능합니다.     

```python
import turtle

turtle.circle(100)

# 창 닫힘 방지
turtle.mainloop()
```
코드로 그린 원이 잘 남아있게 보이게 되었습니다!     
이제부터 다양한 함수들을 사용해 보겠습니다.     
  
### turtle 함수
#### turtle 펜 모양 변경
모양 종류
- 기본 모양 : 'classic' 
- 삼각형 모양 : 'triangle'
- 원 모양 : 'circle'
- 거북이 모양 : 'turtle'
- 화살표 모양 : 'arrow'

```python
# 모양 변경
turtle.shape('turtle')

# 크기 변경
# shapesize(w, h, b) : 세로 w, 가로 h, 윤곽선 b 배로 변경
turtle.shapesize(3, 4, 2)
```

#### turtle 펜 이동하기(이동하는 방향은 화살표 방향(거북이 머리))
```python
# 앞으로 이동
turtle.forward(100)
turtle.fd(100)

# 뒤로 이동
turtle.backward(100)
turtle.back(100)

# 왼쪽으로 회전
turtle.left(90)
turtle.lt(90)

# 오른쪽으로 회전
turtle.right(90)
turtle.rt(90)

# 지금 현재 방향 기준으로 왼쪽 방향으로 각도를 계산하여 회전
turtle.setheading(60)

# 원그리기 (괄호안의 숫자는 반지름)
turtle.circle(100)

# (x, y) 좌표로 이동하기
turtle.goto(x, y)
turtle.setposition(x, y)

# 현재 좌표
turtle.position()
```

![스크린샷 2022-01-12 오전 11 13 39](https://user-images.githubusercontent.com/89170523/149051677-1dc7f436-e010-4498-8373-719f19e4beab.png)     

#### turtle 색, 크기, 속도 지정하기
```python
# 펜과 칠하는 색 모두 지정하기
turtle.color('red')
turtle.color('red', 'blue')  #펜의 색은 빨강, 칠하는 색은 파랑

# 펜만 색 지정하기
turtle.pencolor('red')

# 도형 내부를 칠하는 색 지정 (순서와 begin_fill, end_fill을 모두 써줘야 한다.)
turtle.fillcolor('red')
turtle.begin_fill()
#색을 넣을 도형을 그린다.
turtle.end_fill() 

# 배경화면 색 지정
turtle.bgcolor('red')

# 펜 크기 지정 (픽셀 단위)
turtle.pensize(12)

# 펜 속도 지정
# 1~10 입력 가능 (0은 10과 동일 - 가장 빠른 속도)
turtle.speed(0)
```

#### turtle 펜 들기, 내리기
up()은 펜을 들고 있는 것을 down() 함수는 펜을 내려놓은 것을 뜻하여,       
up()을 통해 펜을 들고 있는 상태에서는 아무리를 goto() 등의 함수를 이용하여 펜을 움직여도 그림이 그려지지 않습니다. 
```python
# 펜 들기 penup과 up은 같은 것이다.
turtle.penup()
turtle.up()

# 펜 내리기
turtle.pendown()
turtle.down()

# 펜의 상태
# 펜이 내려가 있으면 True, 내려가 있지 않으면 False 반환
turtle.isdown()
```
예제
```python
# 선을 그리는 상태로 50만큼 이동
turtle.forward(50)

# 선을 그리지 않는 상태로 100만큼 이동
turtle.penup()
turtle.forward(100)
```

#### turtle 화면 지우기
```python
# 화면은 지우고 turtle은 그대로
turtle.clear()

# 화면도 지우고 turtle 위치도 초기화
turtle.reset()

# 화면은 그대로 두고 turtle 위치는 초기화
turtle.home()
```

#### turtle 입출력
```python
# 실행창의 이름 쓰기
turtle.title("고래코딩")

# turtle 위치에 문자를 출력
turtle.write("원하는 문자")
# 문법 : turtle.write("문자열", move, align, font("font_name",font_size))
turtle.write("문자열", False, "center", ("굴림", 20))
# move가 True이면 문자열 끝으로 turtle 이동
# 왼쪽정렬은 left, 오른쪽 정렬은  right, 가운데 정렬은 center

# 문자열 입력받기
value = turtle.textinput("title", "문자열 입력 ")

# 숫자 입력받기
value = int(turtle.textinput("title", "숫자 입력 ")) #형변환
```

### 사각형 그리기
turtle 모듈을 사용하여 간단한 그림들을 그려볼 수 있습니다.     
사각형을 그리는 예제를 볼까요?       

![스크린샷 2022-01-12 오전 10 31 07](https://user-images.githubusercontent.com/89170523/149047940-6ebb4b3d-98a8-4e1a-80b5-0fb4fd6825db.png)     
위 그림을 그려봅시다.    

```python
import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

mainloop()
```
코드를 한 줄 한 줄 읽어보겠습니다.    
먼저 turtle 모듈을 임포트 한 후에 앞으로 100만큼 이동합니다.     
그러면 사각형의 한 변이 완성이 됩니다.          
그리고 사각형의 다른 변을 그리기 위해서 오른쪽으로 머리를 90도 돌린 후에 앞으로 100만큼 이동합니다.     
사각형의 두 변이 완성이 됩니다.     
남은 두 변도 비슷한 방법으로 완성합니다.        
머리를 90도 돌린 후에 앞으로 100만큼 이동하는 방식으로 사각형을 완성할 수 있습니다.    

그럼 위 사각형 그리기를 활용해서 다른 그림을 더 그려볼 수 있겠네요.     

```python
import turtle

# 8번 반복
# range 는 0부터 7(8-1)까지의 숫자를 가지고 있는 list를 반환합니다.
for i in range(8):
  # 사각형 그리기
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  # 사각형을 그린 후 몇 도를 돌릴지 지정
  turtle.right(45)

turtle.mainloop()
```
<img width="329" alt="사각형8" src="https://user-images.githubusercontent.com/89170523/149048185-898e3eca-92ba-432e-9e0e-2e4644d02f36.png">        
사각형을 각도를 돌려가며 그리니 조금 더 멋있는 모양이 나타났나요?       
45도만큼 돌아가며 사각형을 그리기 때문에 360/45 값인 8번 그리면 한 바퀴를 다 돌수 있어서 총 8번 반복해 주었습니다.      
각도와 사각형을 그리는 횟수를 조절해서 더 다양한 그림을 그려볼 수 있답니다.      

```python
import turtle

# 20번 반복
for i in range(20):
  # 사각형 그리기
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  # 사각형을 그린 후 72 도 돌림
  turtle.right(72)

turtle.mainloop()
```

### 동서남북 출발
이번에는 동서남북 4 방향으로 가는 거북이를 만들어서 출발시켜 보겠습니다.      
머리 방향을 잘 보기 위해서 거북이 4 마리를 각각 움직여 봅시다.      

```python
# turtle을 매번 앞에 붙이지 않기 위해 import * 사용
from turtle import *

# Turtle 객체를 만들어서 사용
t1 = Turtle()
# 거북이 모양
t1.shape("turtle")
# 오렌지색
t1.color("orange")
# 거북이가 보는 방향 90
t1.seth(90)
# 100만큼 이동
t1.forward(100)
# 펜으로 그리기 멈춤
t1.penup()
# 거북이가 보는 방향인 90이라는 숫자 쓰기
t1.write("90   ", left)
```
거북이가 위로 올라가는 코드가 완성이 되었습니다.     
그러면 다른 방향으로도 뻗어나가게 마저 코딩해볼까요?     

```python
from turtle import *

# 북
t1 = Turtle()
t1.shape("turtle")
t1.color("orange")
t1.seth(90)
t1.forward(100)
t1.penup()
t1.write("90   ", left)

# 서
t2 = Turtle()
t2.shape("turtle")
t2.color("orange")
t2.seth(180)
t2.forward(100)
t2.penup()
t2.write("180  ", left)

# 남
t3 = Turtle()
t3.shape("turtle")
t3.color("orange")
t3.seth(270)
t3.forward(100)
t3.penup()
t3.write("270' ", left)

# 동
t4 = Turtle()
t4.shape("turtle")
t4.color("orange")
t4.seth(0)
t4.forward(100)
t4.penup()
t4.write("0   ", left)

mainloop()
```

### 마무리
turtle 모듈의 기본 사용법을 익혀보았습니다.     
해당 모듈을 사용해서 자유롭게 그림을 그려볼 수 있습니다.      

조금 더 심화된 내용들을 실습을 통해 익혀봅시다.


