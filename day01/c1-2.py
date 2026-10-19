print("hello world") # 실행 : shift + Enter

import keyword
print(keyword.kwlist)

# 여러 개 출력, 주의할 점 : ,쉼표 기준으로 공백 자동 포함
print( "여러개", "출력합니다")
print( ) # 한줄 공백 , 제어문자 \n

print((type("안녕하세요")))
print(type(123))
print(type(1.23))
print(type(True))
print(type(None))
print(type( [] ))
print(type({}))
print(type( () ))

print("ABC") # """ 여러줄 감싸기 """
print("A'B'C")
print('A"B"C')

print("\"A\'B\nC\tD\\E")
