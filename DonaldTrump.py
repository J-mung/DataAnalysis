import pandas as pd
import matplotlib.pyplot as plt

'''파일 불러오기'''
trump_df = pd.read_csv('data/hashtag_donaldtrump.csv', lineterminator='\n')
gdp_df = pd.read_csv('data/GDP_per_capita.csv', lineterminator='\n')

# GDP 리스트에서 국가명 추출
country_list = gdp_df['Country']

# GDP 리스트에서 추출한 국가명과 동일한 국가명 데이터추출
country_gdp_df = trump_df.loc[trump_df['country'] == country_list[0], :]
count = 1
for idx in range(1, len(gdp_df)):
    count += 1
    print(country_list[idx] + " | " + str(count))
    likes_sri = trump_df.loc[trump_df['country'] == country_list[idx], :]
    country_gdp_df = country_gdp_df.append(likes_sri)
    print(": " + str(country_gdp_df.shape))

# 생성한 데이터프레임 확인
print('==================== country_gdp_df ====================')
print(country_gdp_df.head())

# 대륙별로 구별하기 위해 continent country likes 정보만 남겨서 데이터프레임화
trump_df = country_gdp_df[['continent', 'country', 'tweet', 'user_description','likes']]
trump_df = trump_df.set_index('continent')
# 생성한 데이터프레임 확인
print('======================= trump_df =======================')
print(trump_df.head())

#trump_df.to_csv('data/likes_donaldtrump.csv')

# 각 대륙 별로 데이터프레임 구성
continent_list = []
Africa_df = trump_df.loc['Africa']
continent_list.append(Africa_df)
Asia_df = trump_df.loc['Asia']
continent_list.append(Asia_df)
Europe_df = trump_df.loc['Europe']
continent_list.append(Europe_df)
NorthAmerica_df = trump_df.loc['North America']
continent_list.append(NorthAmerica_df)
Oceania_df = trump_df.loc['Oceania']
continent_list.append(Oceania_df)
SouthAmerica_df = trump_df.loc['South America']
continent_list.append(SouthAmerica_df)

# 생성한 데이터프레임 확인
print('====================== Africa_df =======================')
print(continent_list[0])

# 대륙별로 좋아요 수의 평균을 구하고, 평균이 5.0을 넘는 국가만 남겨서 리스트에 저장
for idx in range(len(continent_list)):
    likes_avrg = continent_list[idx].groupby(continent_list[idx]['country'])['likes'].mean().to_frame()
    continent_list[idx] = pd.DataFrame({
        'country' : likes_avrg.index,
        'likes' : likes_avrg['likes']
    })
    continent_list[idx] = continent_list[idx][continent_list[idx]['likes']>5.0]
# 생성된 데이터프레임 확인
print('================== Africa_likes_avrg ==================')
print(continent_list[0])

# 그래프 그리기
plt.plot(continent_list[5]['country'], continent_list[5]['likes'])
plt.ylabel('likes number')
plt.xlabel('South America\'s countries')
plt.title('Donald Trump')
plt.show()
