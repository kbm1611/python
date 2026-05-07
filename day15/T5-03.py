import pandas as pd
import matplotlib.pyplot as plt
import koreanfont
import json

# [1] T5_data.json 파일내 'patient_status_data'
with open( './T5_data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['patient_status_data'] )
print( df )

# [2] 막대차트: 상태별 환자수 비교
plt.bar(
    df['상태'],
    df['환자 수'],
    label = '환자 수',
    color = "#C52525"
)
plt.title('상태별 환자 수 비교')
plt.xlabel('상태')
plt.ylabel('환자 수')
plt.legend()
plt.show()

# [3] 원형차트: 전체대비 각 상태의 환자수 비율
# plt.pie( 값, labels='', autopct='%.nf%%', startangle='시작각도' )
plt.pie( df['환자 수'], labels=df['상태'], autopct='%.2f%%')
plt.title('환자 상태 비율')
plt.show()