# p.115 변수
pi = 3.14159265 # 변수명 = 값
r = 10          # 변수명 = 값
#r2             # 초기값이 없으면 NameError:
print(pi, r, r2)# 변수의 참조
print( 2*pi*r ) 

# p.116 복합대입연산자
number = 100
number += 10
number -= 10
number *= 2
number /= 2
number %= 3
number **= 3
number  = "안녕하세요"
number += "!" 
number *= 3
print(number)

# p.118 입력함수, 반환타입 : 문자열 str
input("인사말을 입력하세요>")
string = input("입력>")
print (type(string))

# p.121타입변환 , str -> int / float
string_int = int(string)
string_float = float(string)
print(type(string_int), type(string_float))

# p.125 누적예제
raw_input = input("inch 입력: ")    # 1. 입력받아 변수에 저장
inch = int(raw_input)              # 2. 연산 전에 str -> int 변환
cm = inch * 2.54                   # 3. 연산
print(cm)                          # 4. 출력
