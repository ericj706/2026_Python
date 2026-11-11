import pandas as pd
fish = pd.read_csv("./day15/Fish.csv")
# 1) 다중 분류 실습하기 위한 특성 / 타깃(여러개 어종) 구분
fish = fish[ (df['Species'] == 'Bream')|(fish['Species'] == 'Smelt') ]
X = fish[ ['Weight','Length1','Length2','Length3','Height','Width'] ] # 6가지의 특성
Y = fish['Species'] # Bream 또는 Smelt
# 2) 분리 , 분류 학습 모델 사용시 (타깃의 분리 비율 일정 만들기)
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(
    X , Y , test_size=0.2 , random_state=42 , stratify=Y)

# 3) 다항 특성들의 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train) # fit + transform
X_test_scaled = ss.transform(X_test)

# 4) 로지스틱 회귀 = 이진 또는 다중에서 자동 선택 된다.
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train_scaled , Y_train)
Y_pred = model.predict(X_test_scaled)
