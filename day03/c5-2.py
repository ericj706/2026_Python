# p.293 재귀함수, 재귀란 자기 자신을 호출하는것
# 1) 팩토리얼
def factorial1(n) :
    output = 1
    for i in range(1, n+1):
        output *= i
    return output
factorial1(2)    # 2! -> 2*1 = 2
factorial1(3)    # 3! -> 6

# 2) 팩토리얼 재구ㅏ
def factorial2(n) :
    if n == 0:
        return 1
    else : # 재귀함수
        return n*factorial2(n-1)
factorial2(2)
factorial2(3)

# 구구단 반복문
for 단 in range(2, 10, 1):
    for 곱 in range(1, 10, 1):
        print(단 * 곱)

# 구구단 재귀
def 구구단 ( 단 = 2, 곱 = 1):
    if 단 > 9:
        return
    if 곱 > 9:
        구구단(단+1) # 단마다 곱하기 9까지 했으면 단 올리기
        return
    print(단 * 곱)
    구구단(단, 곱+1) # 곱 올리기
구구단( )
# 3단 4곱까지의 반복문 순서도 작성

# 피보나치 수열 예제
dictionary = {  # 메모(1번값=1 , 2번값=1)
    1 : 1,
    2 : 1
}
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else :
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output
print("fibonacci(10): ",fibonacci(10))
print("fibonacci(30): ",fibonacci(30))
print("fibonacci(50): ",fibonacci(50))