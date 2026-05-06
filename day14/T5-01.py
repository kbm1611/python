
import matplotlib.pyplot as plt # 맷플롯립( 시각화 라이브러리 )
import pandas as pd      # 판다스( 데이터 표 관리 )
import koreanfont        # 그래프 한글 깨짐 방지
import json # JSON 파일 load용도

# [1] JSON 파일에서 특정한 열("customer_data")만 가져와서 데이터프레임 구성
with open( './T5_data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load( json_file )
df_customer = pd.DataFrame( data_json['customer_data'] )
print( df_customer.head() )

# [2] 데이터 분석 / 시각화
# (1) 성별과 연령대로 그룹화, df.groupby( ['그룹기준', '그룹기준'] )
# (2) 다수 통계,  df.agg( { '열이름' : '함수명' } )
# (3) 여러개 그룹화할 경우에는 .reset_index() 함수 이용하여 행번호 붙인다.
newDf = df_customer.groupby( ['성별','연령대'] ).agg( {'고객 수' : 'sum' , '평균 구매 금액' : 'mean'}).reset_index()
print( newDf ) # 성별 + 연령대 별 총고객수(합계)와 평균구매금액의 평균
print( newDf['연령대'] )
print( newDf['연령대'].unique() )
print( newDf.groupby(['연령대']).agg({'고객 수' : 'sum' }) )

# 1. 연령대별 총 고객수 세로막대그래프
# (1) plt.bar( x축값, y축값 )
plt.bar( newDf['연령대'].unique(),
        newDf.groupby(['연령대']).agg({'고객 수' : 'sum'})['고객 수'],
        color = '#FFEA00',
        label = '누적 고객 수' )
plt.xlabel( '연령대' )  # x축 제목
plt.ylabel( '총 고객 수' )  # y축 제목
plt.legend() # 범례
plt.title('연령대별 누적 고객 수')
plt.show()
# 차트확인: 30대가 비중이 가장 크고, 50대 고객이 가장 작다.

# 2. 성별 + 연령대별 세로막대그래프
# (왼쪽) 세로축, (오른쪽) 세로축
male_data = newDf[ newDf['성별'] == '남성' ]
print( male_data )
female_data = newDf[ newDf['성별'] == '여성' ]
print( female_data )
plt.bar( male_data['연령대'], male_data['고객 수'], label ='남성 수', color = '#0000ff' )
# 만약에 겹쳐 나오는 경우 : 아래 순서로 변경할 막대에 bottom
plt.bar( female_data['연령대'],
        female_data['고객 수'],
        label='여성 수',
        color='#ffff00',
        bottom=male_data['고객 수']
        )
plt.xlabel('연령대')
plt.ylabel('총 고객 수')
plt.legend()
plt.title('성별 및 연령대별 누적 고객 수')
plt.show()
# 차트 확인: 남성/여성 모두 30대에서 고객 수가 확연히 크다, 또한 40~50대 여성 비율이 더 높다
 

# 3. 연령대별 '평균 구매 금액' 가로막대그래프
plt.barh(
    newDf['연령대'].unique(),
    newDf.groupby(['연령대']).agg({'평균 구매 금액' : 'mean' })['평균 구매 금액'],
    label="평균 구매 금액",
    color="#ff0000"
)
plt.xlabel('평균 구매 금액')
plt.ylabel('연령대')
plt.legend()
plt.title('연령대 별 평균 구매 금액')
plt.show()