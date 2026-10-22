# p.363
# 구문 오류 : 실행 전 오류, 실행 자체 불가능
# 런타임 오류 : 실행 중 오류, 예외
# 예외 처리 : 예외를 해결하는 모든 것을

# 조건문 또는 try
# 예1] 조건문 예외
input_a = input("정수입력: ")
# int( input_a ) # ValueError: # int( ) 정수로 변환 함수 
if input_a.isdigit() :  # 문자열.isdigit() : 문자열타입의 값이 숫자이면 true 
    int( input_a )
else : 
    print("정수가 아닙니다.")
# 예2] try 예외
try :
    int( input_a ) # 예외가 발생할 것 같은 코드 
except : 
    print("정수가 아닙니다.")
# 예3] pass 키워드 , 예외 어떻게 처리할지 모른경우 일단 넘어가기 
try : 
    int( input_a )
except :
    pass
# 예4] else , 예외가 발생하지 않았을 떄
try :   # 예외가 발생할 가능성이 있는 코드 
    int( input_a )
except :# 예외가 발생했을 떄 실행코드 
    print( "정수가 아닙니다.")
else : # 예외가 발생하지 않았을 떄 실행코드
    print( "정수가 맞습니다.")
# 에5] finally , 예외가 발생하든 발생하지 않든 무조건 실행 코드 
try : 
    int( input_a )
except :
    print( "정수가 아닙니다.")
else : 
    print( "정수가 맞습니다.")
finally : # 무조건 실행되는 코드
    print( "코드가 끝났습니다.")