import pandas as pd
df = pd.read_csv("./day14/Fish.csv")
# 1) 이진 분류 실습하기 위한 정답지 2가지만 사용
df = df[ (df['Species'] == 'Bream')|(df['Species'] == 'Smelt') ]
X = df[ ['Weight','Length1','Length2','Length3','Height','Width'] ] # 6가지의 특성
Y = df['Species'] # Bream 또는 Smelt
# 2) 분리 , 분류 학습 모델 사용시 (타깃의 분리 비율 일정 만들기)
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(
    X , Y , test_size=0.2 , random_state=42 , stratify=Y
) # stratify=Y : 타깃 무작위 분리한 경우 클래스 비율 일정 유지 , 분류모델
# 3) 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)
# 4) 로지스틱 모델 사용
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train_scaled , Y_train)
Y_pred = model.predict(X_test_scaled)
print(Y_pred)
# ['Bream' 'Bream' 'Smelt' ]
# 5) 결과 속성
print(model.classes_) # 정답지 종류 # ['Bream' 'Smelt']
print(model.predict_proba(X_test_scaled[:3])) # 확률로 반환
# 6) 정확도 평가 : 결정계수 대신에 다양한 평가ㅣ
from sklearn.metrics import accuracy_score
# accuracy_score(테스트정답지, 테스트예측)
acc = accuracy_score(Y_test, Y_pred)
print(acc)
