import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

# [1] T5_data.json 파일내 'risk_return_data'
with open( './T5_data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['risk_return_data'] )
print( df )

# [2] 산점도: 리스크 대비 수익률, 값에 따른 계산식별로 원형크기 조정 -> 버블차트
# plt.scatter( x축, y축, s = 원형크기(계산식), alpha = 투명도 )
plt.scatter(
    df['리스크'],
    df['수익률(%)'],
    s = df['수익률(%)']  * 100, 
    alpha= 0.5,
    color='#000000'
)
plt.title('리스크 대비 수익률 산점도')
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.show()

# [3] 산점도: 자산별 리스크 대비 수익률
categories = df['자산'].unique()    # 중복제거 리스트
colors = [ "#0bc798", '#ff0000', '#fc7525', '#0f2f31', '#533333']
for i, category in enumerate( categories ):
    subset = df[ df['자산'] == category ] # 동일한 자산 정보 가져오기.
    plt.scatter( subset['리스크'], subset['수익률(%)'], color = colors[i], label = category )
plt.legend()
plt.show()
    