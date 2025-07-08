
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
df = pd.read_csv('/content/data.csv')

season_max = df.groupby(by='season_x')['count_x'].mean()
season_name = ['springer', 'summer', 'fall', 'winter']

st.header('Dashboard Dataset Bike Sharing :bike:')

# Pertanyaan 1
st.subheader('Pada Hari Apa Penggunaan Sepeda Mengalami Trend Tertinggi?')
data_hari = plt.figure(figsize=(10, 5))
sns.lineplot(x='weekday_x', y='count_x', data=df, ci=None)
plt.title('Trend Penggunaan Sepeda Berdasarkan Hari')
plt.xlabel('Hari')
plt.ylabel('Jumlah Penggunaan Sepeda')
st.pyplot(data_hari)

# Pertanyaan 2
st.subheader('Di Musim Apakah Pengguna Paling Banyak Memakai/menyewa Sepeda?')
season_max = df.groupby(by='season_x')['count_x'].mean()
season_name = ['springer', 'summer', 'fall', 'winter']
musim_data = plt.figure(figsize=(10, 5))
plt.bar(season_name, season_max)
plt.title('Penggunaan Sepeda Berdasarkan Musim')
plt.xlabel('Season')
plt.ylabel('Count')
st.pyplot(musim_data)
