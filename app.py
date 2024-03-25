import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm

# Function to count rows
def count_rows(rows):
    return len(rows)

# Load the data
@st.cache
def load_data():
    df_apr14=pd.read_csv(r'C:\Users\Lenovo\Downloads\uber-raw-data-sep14.csv.zip')
    df_may14=pd.read_csv(r'C:\Users\Lenovo\Downloads\uber-raw-data-may14.csv.zip')
    df_jun14=pd.read_csv(r'C:\Users\Lenovo\Downloads\uber-raw-data-jun14.csv.zip')
    df_jul14=pd.read_csv(r'C:\Users\Lenovo\Downloads\uber-raw-data-jul14.csv.zip')
    df_aug14=pd.read_csv(r'C:\Users\Lenovo\Downloads\uber-raw-data-aug14.csv.zip')
    df_sep14=pd.read_csv(r'C:\Users\Lenovo\Downloads\uber-raw-data-sep14.csv.zip')
    df = pd.concat([df_apr14, df_may14, df_jun14, df_jul14, df_aug14, df_sep14], ignore_index=True)
    return df

df = load_data()

# Visualizations
st.title('Uber Trips Analysis')

# 1. Trips by Hour
st.header('Trips by Hour')
df_hour_grouped = df.groupby(['Hour']).count()
df_hour = pd.DataFrame({'Number_of_trips':df_hour_grouped.values[:,0]}, index = df_hour_grouped.index)
st.bar_chart(df_hour)

# 2. Trips by Month
st.header('Trips by Month')
df_month_grouped = df.groupby(['Month'], sort=False).count()
df_month = pd.DataFrame({'Number_of_trips':df_month_grouped.values[:,0]}, index = df_month_grouped.index)
st.bar_chart(df_month)

# 3. Trips by Weekday
st.header('Trips by Weekday')
df_weekday_grouped = df.groupby(['Weekday'], sort=False).count()
df_weekday = pd.DataFrame({'Number_of_trips':df_weekday_grouped.values[:,0]}, index = df_weekday_grouped.index)
st.bar_chart(df_weekday)

# 4. Trips by Day
st.header('Trips by Day')
df_day_grouped = df.groupby(['Day']).count()
df_day = pd.DataFrame({'Number_of_trips':df_day_grouped.values[:,0]}, index = df_day_grouped.index)
st.bar_chart(df_day)

# 5. Heatmap by Hour and Day
st.header('Heatmap by Hour and Day')
df_hour_day = df.groupby(['Hour', 'Day']).apply(count_rows).unstack()
plt.figure(figsize=(10, 8))
sns.heatmap(df_hour_day, cmap=cm.YlGnBu, linewidth=.5)
st.pyplot()

# 6. Heatmap by Hour and Weekday
st.header('Heatmap by Hour and Weekday')
df_hour_weekday = df.groupby(['Hour', 'Weekday'], sort=False).apply(count_rows).unstack()
plt.figure(figsize=(10, 8))
sns.heatmap(df_hour_weekday, cmap=cm.YlGnBu, linewidth=.5)
st.pyplot()

# 7. Heatmap by Day and Month
st.header('Heatmap by Day and Month')
df_day_month = df.groupby(['Day', 'Month'], sort=False).apply(count_rows).unstack()
plt.figure(figsize=(10, 8))
sns.heatmap(df_day_month, cmap=cm.YlGnBu, linewidth=.5)
st.pyplot()

# 8. Heatmap by Month and Weekday
st.header('Heatmap by Month and Weekday')
df_month_weekday = df.groupby(['Month', 'Weekday'], sort=False).apply(count_rows).unstack()
plt.figure(figsize=(10, 8))
sns.heatmap(df_month_weekday, cmap=cm.YlGnBu, linewidth=.5)
st.pyplot()

