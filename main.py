import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
# 데이터 파일 경로
file_path = '202406_202406_연령별인구현황_월간 (1).csv'

# 데이터 로드
data = pd.read_csv(file_path, encoding='cp949')

# 데이터 전처리
data = data.replace(',', '', regex=True)  # 쉼표 제거
data.iloc[:, 2:] = data.iloc[:, 2:].astype(int)  # 숫자 형변환

# 사용자 입력
region = st.selectbox('지역을 선택하세요:', data['행정구역'].unique())

# 선택한 지역의 데이터 필터링
region_data = data[data['행정구역'] == region]

# 중학생 인구 계산 (13세~15세)
total_population = region_data.iloc[:, 1:2].values[0][0]
middle_school_population = region_data[['2024년06월_계_13세', '2024년06월_계_14세', '2024년06월_계_15세']].sum(axis=1).values[0]

# 원 그래프 그리기
labels = ['중학생 인구', '기타 인구']
sizes = [middle_school_population, total_population - middle_school_population]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
