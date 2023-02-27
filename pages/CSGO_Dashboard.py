import streamlit as st
import pandas as pd
import plotly.express as px
import os
from matplotlib import image

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "csgo.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "player_stats.csv")

st.title("Dashboard - CS Competitive Players")
img = image.imread(IMAGE_PATH)
st.image(img, width=500)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

country_option = df['country'].unique().tolist()
country = st.selectbox("Select country: ", country_option,0)
df = df[df['country']==country]

col1, col2 = st.columns(2)

fig_1 = px.bar(df, x='name',y='total_rounds',color='name',title='Shows Players based on country:')
#st.write(fig_1)
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.pie(df, values='kd',names='name',title='Players performance:')
#st.write(fig_2)
col2.plotly_chart(fig_2, use_container_width=True)
