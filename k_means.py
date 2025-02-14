# -*- coding: utf-8 -*-
"""K-Means.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uuv3D6XSBx54QKhdqSeAunXFp1qBkbHg
"""

from google.colab import drive
drive.mount('/content/drive')

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import pandas as pd
import numpy as np

df = pd.read_excel('/content/drive/MyDrive/통계 데이터.xlsx')

df.head()

df.info()

df['당뇨병 진단경험률(30세이상)'] = df['당뇨병 진단경험률(30세이상)'].astype(str).str.extract(r'(\d+\.\d+)')[0].astype(float)

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



# 필요한 열을 선택하여 새로운 데이터프레임을 만듭니다.
x_columns = ['병원 수', '2022 의료인수']
y_columns = ['고혈압 진단경험률(30세이상)', '당뇨병 진단경험률(30세이상)', '뇌졸중(중풍) 조기증상 인지율', '심근경색 조기증상 인지율', '진료실인원수 (명)']

x_data = df[x_columns]
y_data = df[y_columns]

# 데이터 전처리: 결측값 제거 및 스케일링
x_data = x_data.dropna()
y_data = y_data.dropna()
gu_names = df['구']  # 구 이름을 따로 저장

x_scaler = StandardScaler()
y_scaler = StandardScaler()

x_scaled_data = x_scaler.fit_transform(x_data)
y_scaled_data = y_scaler.fit_transform(y_data)

# 데이터프레임 확인
print(x_data.head())
print(y_data.head())

# X축 변수에 대해 PCA 수행
x_pca = PCA(n_components=1)
x_principal_components = x_pca.fit_transform(x_scaled_data)

# X축 PCA 결과를 데이터프레임으로 변환
x_pca_df = pd.DataFrame(data=x_principal_components, columns=['X_PC'])


# Y축 변수에 대해 PCA 수행
y_pca = PCA(n_components=1)
y_principal_components = y_pca.fit_transform(y_scaled_data)

# Y축 PCA 결과를 데이터프레임으로 변환
y_pca_df = pd.DataFrame(data=y_principal_components, columns=['Y_PC'])

# PCA 결과 결합
combined_pca_df = pd.concat([x_pca_df, y_pca_df], axis=1)
combined_pca_df['구'] = gu_names.values

# 데이터프레임 확인
print(combined_pca_df.head())

from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(x_principal_components)
visualizer.show()

# 최적의 k 값을 찾기 위한 엘보우 시각화 (Y축 PCA 결과)
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(y_principal_components)
visualizer.show()

# K-means 클러스터링 수행
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(combined_pca_df[['X_PC', 'Y_PC']])

# 클러스터 결과를 데이터프레임에 추가
combined_pca_df['Cluster'] = clusters

# 데이터프레임 확인
print(combined_pca_df.head())

# PCA와 클러스터링 결과 시각화
plt.figure(figsize=(10, 6))
plt.rc('font', family='NanumBarunGothic')
plt.scatter(combined_pca_df['X_PC'], combined_pca_df['Y_PC'], c=combined_pca_df['Cluster'], cmap='viridis')
for i, txt in enumerate(combined_pca_df['구']):
    plt.annotate(txt, (combined_pca_df['X_PC'][i], combined_pca_df['Y_PC'][i]), fontsize=8)
plt.xlabel('X_PC')
plt.ylabel('Y_PC')
plt.title('PCA and K-means Clustering')
plt.colorbar(label='Cluster')
plt.show()

combined_pca_df

df.info()

# 필요한 열을 선택하여 새로운 데이터프레임을 만듭니다.
x_columns = ['2023(독거노인현황)', '2022(기초생활수급자)', '2023(장애인수)']
y_columns = ['월 평균 총 소득 금액']

x_data = df[x_columns]
y_data = df[y_columns]

# 데이터 전처리: 결측값 제거 및 스케일링
x_data = x_data.dropna()
y_data = y_data.dropna()
gu_names = df['구']  # 구 이름을 따로 저장

x_scaler = StandardScaler()
y_scaler = StandardScaler()

x_scaled_data = x_scaler.fit_transform(x_data)
y_scaled_data = y_scaler.fit_transform(y_data)

# 데이터프레임 확인
print(x_data.head())
print(y_data.head())

# X축 변수에 대해 PCA 수행
x_pca = PCA(n_components=1)
x_principal_components = x_pca.fit_transform(x_scaled_data)

# X축 PCA 결과를 데이터프레임으로 변환
x_pca_df = pd.DataFrame(data=x_principal_components, columns=['X_PC'])


# Y축 변수에 대해 PCA 수행
y_pca = PCA(n_components=1)
y_principal_components = y_pca.fit_transform(y_scaled_data)

# Y축 PCA 결과를 데이터프레임으로 변환
y_pca_df = pd.DataFrame(data=y_principal_components, columns=['Y_PC'])

# PCA 결과 결합
combined_pca_df = pd.concat([x_pca_df, y_pca_df], axis=1)
combined_pca_df['구'] = gu_names.values

# 데이터프레임 확인
print(combined_pca_df.head())

from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(x_principal_components)
visualizer.show()

# 최적의 k 값을 찾기 위한 엘보우 시각화 (Y축 PCA 결과)
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(y_principal_components)
visualizer.show()

# K-means 클러스터링 수행
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(combined_pca_df[['X_PC', 'Y_PC']])

# 클러스터 결과를 데이터프레임에 추가
combined_pca_df['Cluster'] = clusters

# 데이터프레임 확인
print(combined_pca_df.head())

# PCA와 클러스터링 결과 시각화
plt.figure(figsize=(10, 6))
plt.rc('font', family='NanumBarunGothic')
plt.scatter(combined_pca_df['X_PC'], combined_pca_df['Y_PC'], c=combined_pca_df['Cluster'], cmap='viridis')
for i, txt in enumerate(combined_pca_df['구']):
    plt.annotate(txt, (combined_pca_df['X_PC'][i], combined_pca_df['Y_PC'][i]), fontsize=8)
plt.xlabel('X_PC')
plt.ylabel('Y_PC')
plt.title('PCA and K-means Clustering')
plt.colorbar(label='Cluster')
plt.show()

combined_pca_df

