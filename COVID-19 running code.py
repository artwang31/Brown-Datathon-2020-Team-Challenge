# -*- coding: utf-8 -*-
"""Copy_of_fidelity_example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uksN7xOFIWPzKNdKoA9cU9ssqgedVkE5
"""

from google.colab import drive
drive.mount('/content/drive/', force_remount=True)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_visaType = pd.read_excel('/content/drive/My Drive/Team-HAM-Data/US_arrivals_data/Final COR Visa Type.xlsx',0,header=None)

df_visaType = df_visaType.drop(df_visaType.columns[[0, 10]], axis = 1)

df_visaType = df_visaType.iloc[1:]

df_visaType.head()

df_visaType.columns = df_visaType.iloc[0]
df_visaType = df_visaType.iloc[1:]
df_visaType.head()

df_visaType = df_visaType.dropna()
df_visaType.head()

columns = df_visaType.columns.tolist()
columns_new = ['World Region/Country of Residence (COR)',
 'Business',
 'Percent Change',
 'Pleasure',
 'Percent Change',
 'Student',
 'Percent Change',
 'Total Arrivals',
 'Percent Change ',
 'Total_Business',
 'Total_Pleasure',
 'Total_Student']
df_visaType.columns = columns_new
df_visaType.head()

fig, axs = plt.subplots(1, 3, figsize = (15,5))

df_visaType_world = df_visaType.head(10)
df_visaType_world = df_visaType_world.iloc[1:]

for ax in axs:
    plt.sca(ax)
    plt.xticks(rotation=45)
    
axs[0].scatter(x = df_visaType_world['World Region/Country of Residence (COR)'], y = df_visaType_world['Business'])
axs[0].set_ylabel('Business')
axs[0].set_xlabel('World Regions')
axs[1].scatter(x = df_visaType_world['World Region/Country of Residence (COR)'], y = df_visaType_world['Pleasure'])
axs[1].set_ylabel('Pleasure')
axs[1].set_xlabel('World Regions')
axs[2].scatter(x = df_visaType_world['World Region/Country of Residence (COR)'], y = df_visaType_world['Student'])
axs[2].set_ylabel('Student')
axs[2].set_xlabel('World Regions')

df_visaType_country = df_visaType.tail(40)
df_visaType_country.sort_values('Business',inplace=True)
df_visaType_country.plot(kind='barh',y = 'Business', x = 'World Region/Country of Residence (COR)', figsize=(10,10))

ind = np.arange(len(df_visaType_country))
width = 0.4

fig, ax = plt.subplots(figsize=(10,15))
ax.barh(ind - width, df_visaType_country['Business'], width, color='blue', label='Business')
ax.barh(ind, df_visaType_country['Pleasure'], width, color='red', label='Pleasure')
ax.barh(ind + width, df_visaType_country['Student'], width, color='green', label='Student')

ax.set(yticks=ind + width, yticklabels=df_visaType_country['World Region/Country of Residence (COR)'], ylim=[width - 1, len(df_visaType_country)])
ax.legend()

#plt.plot(figsize=(10,10))
plt.show()

df = pd.DataFrame()

for i in range(8):
  df_visaType = pd.read_excel('/content/drive/My Drive/Team-HAM-Data/US_arrivals_data/Final COR Visa Type.xlsx',i,header=None)
  df_visaType = df_visaType.drop(df_visaType.columns[[0, 10]], axis = 1)
  df_visaType = df_visaType.iloc[1:]
  df_visaType.columns = df_visaType.iloc[0]
  df_visaType = df_visaType.iloc[1:]
  df_visaType = df_visaType.dropna()
  columns = df_visaType.columns.tolist()
  columns_new = ['World Region/Country of Residence (COR)',
  'Business',
  'Percent Change',
  'Pleasure',
  'Percent Change',
  'Student',
  'Percent Change',
  'Total Arrivals',
  'Percent Change ',
  'Total_Business',
  'Total_Pleasure',
  'Total_Student']
  df_visaType.columns = columns_new
  df_visaType['year'] = 2019 - i
  df = pd.concat([df, df_visaType])

df.head()

temp_list = []
df['World Region/Country of Residence (COR)'] = df['World Region/Country of Residence (COR)'].str.rstrip()
for i, row in df.iterrows():
  if row['World Region/Country of Residence (COR)'] == 'China, PRC (EXCL HK)' or row['World Region/Country of Residence (COR)'] == 'China PRC (ex Hong Kong)':
    temp_list.append('China PRC')
  elif row['World Region/Country of Residence (COR)'] == 'Rissia':
    temp_list.append('Russia')
  elif row['World Region/Country of Residence (COR)'] == 'Hondorus':
    temp_list.append('Honduras')
  else:
    temp_list.append(row['World Region/Country of Residence (COR)'])
df['World Region/Country of Residence (COR)'] = temp_list
#set(df['World Region/Country of Residence (COR)'].tolist())

df_china = df.loc[df['World Region/Country of Residence (COR)'] == 'China PRC']
#df_china = pd.concat([df_china, df.loc[df['World Region/Country of Residence (COR)'] == 'China PRC (ex Hong Kong)']])
#df_china['World Region/Country of Residence (COR)'] = 'China (ex HKG)'

plt.plot(df_china['year'], df_china['Business'], label = 'Business')
plt.plot(df_china['year'], df_china['Pleasure'], label = 'Pleasure')
plt.plot(df_china['year'], df_china['Student'], label = 'Student')
plt.legend()
plt.show()

df_india = df.loc[df['World Region/Country of Residence (COR)'] == 'India']

plt.plot(df_india['year'], df_india['Business'], label = 'Business')
plt.plot(df_india['year'], df_india['Pleasure'], label = 'Pleasure')
plt.plot(df_india['year'], df_india['Student'], label = 'Student')
plt.legend()
plt.show()

df_asia = df.loc[df['World Region/Country of Residence (COR)'] == 'Asia']

plt.plot(df_asia['year'], df_asia['Business'], label = 'Business')
plt.plot(df_asia['year'], df_asia['Pleasure'], label = 'Pleasure')
plt.plot(df_asia['year'], df_asia['Student'], label = 'Student')
plt.legend()
plt.show()

df_we = df.loc[df['World Region/Country of Residence (COR)'] == 'Western Europe']

plt.plot(df_we['year'], df_we['Business'], label = 'Business')
plt.plot(df_we['year'], df_we['Pleasure'], label = 'Pleasure')
plt.plot(df_we['year'], df_we['Student'], label = 'Student')
plt.legend()
plt.show()

COR_list = set(df['World Region/Country of Residence (COR)'].tolist())
R_list = ['Western Europe', 'Eastern Europe', 'Africa', 'Asia', 'South America', 'Caribbean', 'Central America', 'Oceania', 'Middle East']
C_list = [x for x in COR_list if x not in R_list]

plt.rcParams["figure.figsize"] = (10,10)
for i in C_list:
  if i == 'Total Overseas':
    continue
  else:
    temp = df.loc[df['World Region/Country of Residence (COR)'] == i]
    plt.plot(temp['year'], temp['Total Arrivals'], label = i)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Year')
plt.ylabel('Total Arrivals')
plt.title('Total Arrivals tourists v/s Year')
plt.show()

c = ['United Kingdom', 'China PRC', 'Japan', 'France', 'South Korea', 'Brazil']

df1 = df.loc[df['World Region/Country of Residence (COR)']!='Total Overseas']
df1 = df1[df1['World Region/Country of Residence (COR)'].isin(c)]

plt.rcParams["figure.figsize"] = (10,10)
for i in c:
  temp = df1.loc[df1['World Region/Country of Residence (COR)'] == i]
  plt.plot(temp['year'], temp['Total Arrivals'], label = i)
  plt.scatter(temp['year'], temp['Total Arrivals'])
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Year')
plt.ylabel('Total Arrivals')
plt.title('Total Arrivals tourists v/s Year')
plt.show()

exchangeRates = pd.read_csv('/content/drive/My Drive/Team-HAM-Data/currency_exchange_rates.csv')

plt.rcParams["figure.figsize"] = (10,10)
for i in c:
  temp = df1.loc[df1['World Region/Country of Residence (COR)'] == i]
  temp['Total Arrivals'] = (temp['Total Arrivals'] - np.mean(temp['Total Arrivals']))/np.std(temp['Total Arrivals'])
  plt.plot(temp['year'], temp['Total Arrivals'], label = i)
  plt.scatter(temp['year'], temp['Total Arrivals'])
plt.plot(exchangeRates['Euro'], label = 'Euro')
plt.plot(exchangeRates['Chinese.Yuan'], label = 'Yuan')
plt.plot(exchangeRates['Indian.Rupee'], label = 'INR')
plt.plot(exchangeRates['Japanese.Yen'], label = 'Yen')
plt.plot(exchangeRates['U.K..Pound.Sterling'], label = 'Pound')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Year')
plt.ylabel('Total Arrivals')
plt.title('Total Arrivals tourists v/s Year')
plt.show()

exchangeRates_1 = exchangeRates[exchangeRates['Chinese Yuan'].notna()]
exchangeRates_1.head()

exchangeRates_1['Date_'] = pd.to_datetime(exchangeRates_1['Date'])

exchangeRates_2 = exchangeRates_1.loc[exchangeRates_1.Date_.dt.year <= 2003]
exchangeRates_2 = exchangeRates_2.loc[exchangeRates_2.Date_.dt.year >= 1996]

per = exchangeRates_2.Date_.dt.to_period("M")
g = exchangeRates_2.groupby(per)
exchangeRates_2 = g.mean()

cur = ['Australian Dollar', 'Chinese Yuan', 'Euro', 'Japanese Yen', 'Brazilian Real', 'Korean Won', 'U.K. Pound Sterling']
exchangeRates_3 = exchangeRates_2[cur]
exchangeRates_3.head()

exchangeRates_3['Euro'] = exchangeRates_3.fillna(exchangeRates_3['Euro'].mean())
exchangeRates_3['Brazilian Real'] = exchangeRates_3.fillna(exchangeRates_3['Brazilian Real'].mean())
exchangeRates_3['Japanese Yen'] = exchangeRates_3.fillna(exchangeRates_3['Japanese Yen'].mean())
exchangeRates_3['Korean Won'] = exchangeRates_3.fillna(exchangeRates_3['Korean Won'].mean())

exchangeRates_4 = exchangeRates_3.reset_index()

exchangeRates_4.head()

exchangeRates_4.to_csv('training.csv')
!cp training.csv "drive/My Drive/Team-HAM-Data"

test = exchangeRates_1.loc[exchangeRates_1.Date_.dt.year == 2004]

per = test.Date_.dt.to_period("M")
g = test.groupby(per)
test_1 = g.mean()

cur = ['Australian Dollar', 'Chinese Yuan', 'Euro', 'Japanese Yen', 'Brazilian Real', 'Korean Won', 'U.K. Pound Sterling']
test_2 = test_1[cur]

test_2 = test_2.reset_index()

test_2.isnull().sum()

test_2.to_csv('test.csv')
!cp test.csv "drive/My Drive/Team-HAM-Data"

test_2.head()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
cols = ['Australian Dollar', 'Chinese Yuan'	,'Euro',	'Japanese Yen',	'Brazilian Real',	'Korean Won',	'U.K. Pound Sterling']
exchangeRates_4[cols] = scaler.fit_transform(exchangeRates_4[cols])

plt.plot(exchangeRates_4['Euro'], label = 'Euro')
plt.plot(exchangeRates_4['Chinese Yuan'], label = 'Chinese Yuan')
plt.plot(exchangeRates_4['Australian Dollar'], label = 'Australian Dollar')
plt.plot(exchangeRates_4['Japanese Yen'], label = 'Japanese Yen')
plt.plot(exchangeRates_4['Brazilian Real'], label = 'Brazilian Real')
plt.plot(exchangeRates_4['Korean Won'], label = 'Korean Won')
plt.plot(exchangeRates_4['U.K. Pound Sterling'], label = 'U.K. Pound Sterling')
plt.title('Exchange Rates')
plt.legend()

exchangeRates_4

