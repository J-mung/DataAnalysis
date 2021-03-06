import pandas as pd
import matplotlib.pyplot as plt

'''파일 불러오기'''
biden_df = pd.read_csv('data/likes_joebiden.csv', lineterminator='\n')
'''
gdp_df = pd.read_csv('data/GDP_per_capita.csv', lineterminator='\n')

# GDP 리스트에서 국가명 추출
country_list = gdp_df['Country']

# GDP 리스트에서 추출한 국가명과 동일한 국가명 데이터추출
country_gdp_df = biden_df.loc[biden_df['country'] == country_list[0], :]
count = 1
for idx in range(1, len(gdp_df)):
    count += 1
    print(country_list[idx] + " | " + str(count))
    likes_sri = biden_df.loc[biden_df['country'] == country_list[idx], :]
    country_gdp_df = country_gdp_df.append(likes_sri)
    print(": " + str(country_gdp_df.shape))

# 생성한 데이터프레임 확인
print('==================== country_gdp_df ====================')
print(country_gdp_df.head())

# 대륙별로 구별하기 위해 continent country likes 정보만 남겨서 데이터프레임화
biden_df = country_gdp_df[['continent', 'country', 'tweet', 'user_description','likes']]
biden_df = biden_df.set_index('continent')
# 생성한 데이터프레임 확인
print('======================= biden_df =======================')
'''

biden_df = biden_df.set_index('continent')
print(biden_df.head())

#biden_df.to_csv('data/likes_joebiden.csv')

# 각 대륙 별로 데이터프레임 구성
continent_list = []
Africa_df = biden_df.loc['Africa']
continent_list.append(Africa_df)
Asia_df = biden_df.loc['Asia']
continent_list.append(Asia_df)
Europe_df = biden_df.loc['Europe']
continent_list.append(Europe_df)
NorthAmerica_df = biden_df.loc['North America']
continent_list.append(NorthAmerica_df)
Oceania_df = biden_df.loc['Oceania']
continent_list.append(Oceania_df)
SouthAmerica_df = biden_df.loc['South America']
continent_list.append(SouthAmerica_df)

# 생성한 데이터프레임 확인
print('====================== Europe_df =======================')
print(continent_list[2])

# 대륙별로 좋아요 수의 평균을 구하고, 평균이 5.0을 넘는 국가만 남겨서 리스트에 저장
for idx in range(len(continent_list)):
    likes_avrg = continent_list[idx].groupby(continent_list[idx]['country'])['likes'].mean().to_frame()
    continent_list[idx] = pd.DataFrame({
        'country' : likes_avrg.index,
        'likes' : likes_avrg['likes']
    })
    continent_list[idx] = continent_list[idx][continent_list[idx]['likes']>5.0]
# 생성된 데이터프레임 확인
print('================== Europe_likes_avrg ==================')
print(continent_list[2])

# 그래프 그리기
plt.plot(continent_list[2]['country'], continent_list[2]['likes'])
plt.ylabel('likes number')
plt.xlabel('Europe\'s countries')
plt.title('Joe Biden')
plt.show()
