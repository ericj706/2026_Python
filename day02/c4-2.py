# p.217딕셔너리
# 딕셔너리란? { }중괄호 선언하고 키:값 형태로 쉼표로 연결
# {key:value, key:value, key:value}
# key중복X / value중복O

# 1. 선언
dict_a = { 'name': '어벤저스', 'type': '히어로무비' }
# 2. 값 호출
print(dict_a['name'])
print(dict_a['type'])

# 3. 값추가 , 딕셔너리명['새로운key'] = 새로운값
dict_a['price'] = 5000
print(dict_a)
# 4. 속성값 수정
dict_a['type'] = '호러무비' # 이미 존재하는 키는 값 수정
print(dict_a)
# 5. 속성 삭제, del
del dict_a['price']
print(dict_a)
# 6. 딕셔너리내부확인, 찾을키 in 딕셔너리명
print('price' in dict_a)
print('name' in dict_a)
# 7. 속성값 호출, 방법1: 딕셔너리명['key'], 방법2: 딕셔너리명.get(key)
# 차이점 : 방법1은 존재하지 않으면 예외발생, 방법2는 존재하지 않으면 None반환
print(dict_a.get('name'))   # 정상값 반환
print(dict_a.get('price'))  # None 반환
# 8. for 반복문과 딕셔너리, 딕셔너리내 key하나씩 for에서 순회
# for key반복변수 in 딕셔너리명:
#       실행코드.
for key in dict_a:
    print(dict_a.get(key)) # 방법1
    print(dict_a[key])     # 방법2
