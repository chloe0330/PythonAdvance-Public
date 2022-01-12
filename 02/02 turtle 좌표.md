# turtle 좌표
파이썬 turtle 의 forward 나 back, 그리고 goto 등 다양한 함수에서 숫자들이 사용되고 있습니다.     
여기서 중요한 개념은 거북이의 위치를 나타내는 '좌표'인데요.     
turtle의 좌표는 중심이 (0,0) 입니다.    
좌측으로 갈수록 x축 값이 작아지고 우측으로 갈수록 x축 값이 커집니다.        
위로 갈수록 y축 값이 커지고 아래로 갈수록 y축 값이 작아집니다.        
우리가 흔히 수학 시간에 배우는 좌표평면과 같은 구조를 갖고 있습니다.      

직접 그려보면서 좌표를 확인해보겠습니다.     
우리가 완성할 화면은 아래와 같습니다.     
<img width="714" alt="스크린샷 2022-01-12 오전 11 45 06" src="https://user-images.githubusercontent.com/89170523/149054561-462c0aa5-ea69-4e9f-96ae-1e6e7e207d9b.png">


### 좌표계 그리기
좌표계를 그리기 위해서 우선 직선을 그려보겠습니다.     
```python
import turtle as t

# 펜 올리기(그림 그려지지 않음)
t.up()
# (0,0) 좌표로 이동
t.goto(0,0)
# 펜 내리기(그림 그려짐)
t.down()
# (100,100) 좌표로 이동
t.goto(100,100)

# mainloop 와 동일
t.done()
```
대각선으로 선이 그어지게 됩니다.      
좌표계를 그리기 위해서는 여러 개의 직선을 그려야 합니다.       
이를 반복적으로 사용해야 하므로 직선을 그리는 4개의 명령을 함수로 만들어서 다시 같은 직선을 그려보도록 하겠습니다.       
```python
import turtle as t

# 함수 정의
# (x1, y1)에서 (x2, y2)로 이어지는 직선 그리는 함수
def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)

    return

# 직선 그리기
line(0,0,100,100)

t.done()
```
한 개의 직선을 사용하게 되면 이전보다 복잡하게 느껴질 수 있으나 2개 이상의 직선을 그려야 한다면 훨씬 간단하게 그릴 수 있습니다.       
함수를 사용하여 가로와 세로를 가르지르는 x축과 y축을 그려보도록 하겠습니다.     
```python
import turtle as t

def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)

    return

# x축 그리기
# (-500,0)에서 (500,0)까지 직선 그리기
line(-500,0,500,0)
# y축 그리기
# (0,-500)에서 (0,-500)까지 직선 그리기
line(0,-500,0,500)

t.done()
```
<img width="714" alt="스크린샷 2022-01-12 오전 11 50 00" src="https://user-images.githubusercontent.com/89170523/149055114-08798b45-7025-4aa0-8f24-7db9b8130419.png">
한 개의 함수를 이용하여 2개의 직선을 그리게 되면 훨씬 소스코드가 간단하게 됩니다.      

이번에는 좌표축에 눈금을 그려보도록 하겠습니다.      
```python
import turtle as t

# x1,y1 - x2,y2 직선 그리기
def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)

    return

# 좌표평면
line(-500,0,500,0)
line(0,-500,0,500)

# x축 눈금 그리기
i = -500
while i <= 500:
    i = i + 100
    line(i,-5,i,5)

t.done()
```
x축과 y축에 100단위로 눈금을 그릴 수 있습니다.        
i 가 -500 에서 시작해서 100씩 늘면서 500과 같을때까지 반복합니다.     
i 값에 따라서 line 함수가 돌면서 해당 좌표에 그림을 그리게 되네요.     
i가 -500 으로 첫 while 문에 들어가게 된다면 +100이 되어 i값은 400이 됩니다.    
그리고 `line(400, -5, 400, 5)`가 실행되면서 x좌표 400에 세로로 줄이 그어지게 되겠네요.    
이러한 과정을 i가 500이 될때까지 계속 반복합니다.      

마찬가지로 y축도 눈금을 그릴 수 있습니다.     
```python
import turtle as t

# x1,y1 - x2,y2 직선 그리기
def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)

    return

# 좌표평면
line(-500,0,500,0)
line(0,-500,0,500)

# x축 눈금 그리기
i = -500
while i <= 500:
    i = i + 100
    line(i,-5,i,5)

# y축 눈금 그리기
i = -500
while i <= 500:
    i = i + 100
    line(-5, i, 5, i)
    
t.done()
```
x축을 그리는것과 비슷하지만 `line(-5, i, 5, i)` 여기가 조금 다릅니다.      
x축에는 세로줄로 눈금을 그리고, y축에는 가로줄로 눈금을 그려야하기 때문에 다르게 코딩이 된것이겠죠?       

<img width="715" alt="스크린샷 2022-01-12 오전 11 57 03" src="https://user-images.githubusercontent.com/89170523/149055861-72287c82-c7f6-4343-827d-5e1fb91c2aee.png">

눈금이 그려졌습니다.      
이렇게 x축과 y축에 100단위로 눈금을 그릴 수 있습니다.     
눈금을 많이 그리고 싶거나 적게 그리고 싶으면 i = i + 100 명령행에서 i 변수의 증가 값을 조정하면 됩니다.       

마지막으로 좌표의 눈금에 해당 숫자를 적어보겠습니다.      
```python
import turtle as t

def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    return

# x,y에 텍스트 쓰기
# 선을 그리지 않고 원하는 위치로 이동하여 텍스트 입력
def write(x,y,text):
    t.up()
    t.goto(x,y)
    t.down()
    t.write(text)
    return

line(-500,0,500,0)
line(0,-500,0,500)

# x축 눈금과 값 그리기
i = -500
while i <= 500:
    i = i + 100
    line(i, -5, i, 5)
    write(i-10, -20, i)


# y축 눈금과 값 그리기
i = -500
while i <= 500:
    i = i + 100
    line(-5, i, 5, i)
    write(7, i-5, i)

t.done()
```
x축과 y축 눈금에 값을 여러 번 적어야 하므로 write라는 함수를 만들어 사용하도록 하였습니다.         
그런데 이렇게 하니 축의 중심에 0이 두 번 찍히게 되네요.       
축의 중심에는 0을 쓸 필요가 없으니 0일때는 write 함수를 호출하지 않도록 코드를 수정해 보겠습니다.

```python
import turtle as t

def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    return

# x,y에 텍스트 쓰기
# 선을 그리지 않고 원하는 위치로 이동하여 텍스트 입력
def write(x,y,text):
    t.up()
    t.goto(x,y)
    t.down()
    t.write(text)
    return

line(-500,0,500,0)
line(0,-500,0,500)

# x축 눈금과 값 그리기
i = -500
while i <= 500:
    i = i + 100
    line(i, -5, i, 5)
    if i != 0:
        write(i-10, -20, i)


# y축 눈금과 값 그리기
i = -500
while i <= 500:
    i = i + 100
    line(-5, i, 5, i)
    if i != 0:
        write(7, i-5, i)

t.done()
```
어떤가요?       
원하는 화면이 잘 나오나요?     
이렇게 좌표에 대해서 알아보았습니다.    


