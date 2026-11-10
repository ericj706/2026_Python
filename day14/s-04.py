import pandas as pd
df = pd.read_csv("./Fish.csv") # 1) 자료 수집
X = df[ ['Length2','Height','Width'] ] # 2) 특성 선정/구성
Y = df[ ['Weight'] ] # 2) 타깃(정답) 선정/구성
# 3) 훈련 / 테스트 분리 , 8:2
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2, random_state=42)
# 4) 과소적합 방지 하고자 항 추가 PolynomaialFeatures # 제곱/곱셈
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False) # degree=2 기본값
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)
# 5) 항많아지면 항/특성 간에 단위 표준화 / 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train_poly)
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)
# 6) 모델 선택 = 단순선형회귀 , 규제(릿지 / 라쏘) alpha규제강도
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled,Y_train)
# 7) 결정계수
print('r2 : ', model.score(X_train_scaled , Y_train))
print('r2 : ', model.score(X_test_scaled, Y_test))

