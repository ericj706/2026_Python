# p.383
list_number = [52, 273, 32, 72, 100]
try :
    number_input = int(input("정수 입력: "))
    print(list_number[number_input])
    raise NotImplementedError # 강제 예외 던지기
    # java: throws new 예외클래스()
except ValueError as e :
    print( e )  
except IndexError as e :
    print( e )
except Exception as e :
    print( e )

# 
a = 10
def 함수( ) :
    # global a  
    # 단순 호출이면 global 생략가능,
    # 전역변수 수정하면 global 필수
    global a
    a = a+1
    print (a)
    b = 20
함수 ()

