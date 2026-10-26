import numpy as np

# 1] 배열의 인덱싱
x = np.array( [10,20,30,40,50] )
print(x[0])
print(x[-2])
print(x[ [0,2] ]) #[ [특정인덱스,특정인덱스] ]
print(x[x>20])

# 2] 2차원 인덱싱
x = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
print( x[0,0] )
print( x[1,2] )
print( x[-1,-2] )
print( x[x>5] )

# 3] 슬라이싱
x = np.array( [10,20,30,40,50] )
print( x[1:4] )
print( x[ :3] )
print( x[-3: ] )

# 4] 
x = np.array([ [1,2,3], [4,5,6], [7,8,9] ])
# print( x[행슬라이싱] )
print( x[ : , 1 ] )
print( x[ 1 , : ] )
print( x[0:2 , 1:3] )

# 5]
x = np.array( [10,20,30,40,50] )
y = x[ 1 : 4 ]
print(y)
y[0] = 100
print(x)  # 원본 확인 했더니. 원본도 같이 변경 (파괴적)
y2 = x[ 1 : 4 ].copy()
y2[0] = 1000
print(x)

# 6] 배열의 연산
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y)
print(x*y)
print(x**2)
print(x-2)
print(np.sqrt(x)) # 루트/제곱근 
print(x>2) # 불리안 타입으로
print( (x>1) & (x<3) ) # (조건1) & (조건2), AND
print( (x==1) | (x==3) ) # | , OR
print( x > y ) # 같은 위치끼리 비교

# 배열 간 비교/연산 : 같은 위치끼리 연산 / 비교
# 스칼라(단일숫자)와 배열 비교/연산 : T/F 또는 결과

