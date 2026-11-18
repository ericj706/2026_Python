# 지도학습 : X특선(독립)과 Y타깃(종속) 모델에 학습하여 예측
# 비지도학습 : X특성(독립)


import pandas as pd
url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
df = pd.read_csv(url, sep=';')

X = df[['studytime', 'absences', 'G1', 'G2', 'G3']]

from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(X, test_size=0.02, random_state=42)

# 1) 스케일링/단위표준화 , 
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)
# 2) 군집 = 그룹만들기 = 클러스터, K개의 군집을 찾는 Kmeans 모델 , 
from sklearn.cluster import KMeans
model = KMeans(n_clusters=2) # 모델 생성 / 주의할점 : 데이터에 맞는 적당한 K클러스터 개수를 정해야함.
model.fit(X_train_scaled) # 군집 학습
train_labels = model.predict(X_train_scaled) # 군집 추론
print('앞에서 10명 그룹 확인: ', train_labels[ :10])
# 앞에서 10명 그룹 확인 : [ 1 0 0 1 2 0 0 1 1 0 ]  0또는1또는2 집합으로 클러스터링
print('테스트 학생: ', model.predict(X_test_scaled))
# 3) 시각화 : 특성 여러개이므로 2D 시각화 한계
# 복습
list_2 = [ [2,3], [4,5] ]
print(list_2[ : 1])
# print(list_2.iloc[: , 1])
# print(list_2[ : , 1])
import matplotlib.pyplot as plt
plt.scatter(X_train_scaled[ : ,4], X_train_scaled[ : ,1] , c=train_labels)
plt.scatter(X_test_scaled[ : ,4], X_test_scaled[ : ,1] , c="red", marker='*')
plt.show()

# 4) 최적의 K(군집/그룹) 수 찾기 vs 지도학습 (F1 분류 / R2 회귀)
from sklearn.metrics import silhouette_score
sse_list = []
sil_list = []
for k in range(2,20):
    k_temp = KMeans(n_clusters=k,random_state=42)   # K반복마다 학습 모델 생성
    preds = k_temp.fit_predict(X_train_scaled)      # 모델 학습/추록 동시에, fit + predict
    sse_list.append(k_temp.inertia_)    # 군집 결과에 각 샘플과 중심점 거리 제곱의 합 저장
    sil_list.append(silhouette_score(X_train , preds)) # 실루엣 점수를 저장
plt.plot(range(2,20), sse_list, marker='o')
plt.show()
plt.plot(range(2,20), sil_list, marker='o')
plt.show()
# sse : 엘보우 지점 (기울기가 완만하게 꺾이는 변곡점) 5~10
# 실루엣 : 높은 값일수록 이상적
# 두 차트 해석하여 최적의 K해석 , 
# 최적 K 군집하기
best_model = KMeans(n_clusters=5)
pred = best_model.fit_predict(X_train_scaled)
print(pred[:10])

# 5) HDBSCAN # k-means 다르게 밀도 기반으로 군집 , 이상치(-1) 자동 탐지
from sklearn.cluster import HDBSCAN
# HDBSCAN(min_cluster= 군집하기 위한 최소 데이터수, min_samples= 군집판별할때 계산되는 이웃 수)
model = HDBSCAN(min_cluster_size=15, min_samples=5)
pred = model.fit_predict( X_train_scaled )
print(pred) # 그룹 / 그룹 4개 , 이상치 -1개
