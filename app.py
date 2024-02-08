
import time
import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import pickle
import pandas as pd
import numpy as np
from xgboost import XGBRegressor



teams = ['Australia',
         'India',
         'Bangladesh',
         'New Zealand',
         'South Africa',
         'England',
         'West Indies',
         'Afghanistan',
         'Pakistan',
         'Sri Lanka']

cities = ['Colombo',
          'Mirpur',
          'Johannesburg',
          'Dubai',
          'Auckland',
          'Cape Town',
          'London',
          'Pallekele',
          'Barbados',
          'Sydney',
          'Melbourne',
          'Durban',
          'St Lucia',
          'Wellington',
          'Lauderhill',
          'Hamilton',
          'Centurion',
          'Manchester',
          'Abu Dhabi',
          'Mumbai',
          'Nottingham',
          'Southampton',
          'Mount Maunganui',
          'Chittagong',
          'Kolkata',
          'Lahore',
          'Delhi',
          'Nagpur',
          'Chandigarh',
          'Adelaide',
          'Bangalore',
          'St Kitts',
          'Cardiff',
          'Christchurch',
          'Trinidad']

# #DCD0B7

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.set_page_config(page_title="T20i Score Predictor", page_icon="🏏", layout="wide")

def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


lottie_url_match = "https://lottie.host/c338ad2d-f0a4-4cf8-83e3-f099ed2d9cf6/4sw4rmCLZ7.json"
lottie_url_city = "https://lottie.host/b0bb8066-63d7-496d-a565-f05789e63f7a/g1lM8VQHlj.json"
lottie_url_score = "https://lottie.host/aa079bc7-c3b6-4c05-b2f3-c8906b430983/vSxBKni0Rt.json"
lottie_url_overs = "https://lottie.host/83edcb26-0a47-4238-be74-9e84ce310047/kxBv6gvxho.json"
lottie_url_wicket = "https://lottie.host/518e1c88-d7bc-4ccd-bdff-ddb2733ca283/Wu63Bu9VSI.json"
lottie_url_predicting = "https://lottie.host/02d960ed-50a3-4e03-821f-688f9da2e85b/y6gGCLQbvB.json"
lottie_match = load_lottieurl(lottie_url_match)
lottie_city = load_lottieurl(lottie_url_city)
lottie_score = load_lottieurl(lottie_url_score)
lottie_overs = load_lottieurl(lottie_url_overs)
lottie_wicket = load_lottieurl(lottie_url_wicket)
lottie_predicting = load_lottieurl(lottie_url_predicting)


st.sidebar.image('teams.jpeg', use_column_width=True)  



# def open_start():
#     subprocess.run(["streamlit", "run", "start.py"])
# if st.button("Go Back"):
#         open_start()

st.markdown("<h1 style='text-align: center; margin-top: -6vh;margin-bottom:3vh; color: #FF5733;'>T20i Cricket Score Predictor</h1>", unsafe_allow_html=True)


# Side bar inputs
col1, col2 = st.sidebar.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams)) 

city = st.sidebar.selectbox('Select city', sorted(cities)) 

col4, col5 = st.sidebar.columns(2)
with col4:
    current_score = st.number_input('Current Score')
with col5:
    overs = st.number_input('Overs done (overs > 5)')

wickets = st.sidebar.number_input('Wickets out')
last_five = st.sidebar.number_input('Runs scored in last 5 overs')


# Main content 
row1_col1, row1_col2, row1_col3 = st.columns([1.3, 0.65,1.15])
row2_col1, row2_col2, row2_col3 = st.columns([1.3, 0.65,1.15])
row3_col1, row3_col2, row3_col3 = st.columns([1.3, 0.65,1.15])
row4_col1, row4_col2, row4_col3 = st.columns([1.3, 0.65,1.15])
row5_col1, row5_col2, row5_col3 = st.columns([1.3, 0.65,1.15])


with row1_col1:
    # st.markdown("<h3 style=''> Items Selection </h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-size: 3.5vh;'>Batting And Bowling Team Selection</h3>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh;font-size: 2.5vh;'>Select batting and bowling team of the match from the sidebar. </p>", unsafe_allow_html=True)

with row2_col1:
    st.markdown("<h3 style='font-size: 3.5vh;margin-top: 3vh;'>City Selection</h3>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh;font-size: 2.5vh;'>Select the city where the match is played .</p>", unsafe_allow_html=True)

with row3_col1:
    st.markdown("<h3 style='font-size: 3.5vh;'>Current Score Input</h3>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh;font-size: 2.5vh;'>Input the current score using the sidebar.</p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh;font-size: 2.5vh;'>You can also use the slider to adjust the value.</p>", unsafe_allow_html=True)

with row4_col1:
    st.markdown("<h3 style='font-size: 3.5vh;'>Overs Input</h3>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh;font-size: 2.5vh;'>Input the overs done (works for overs > 5) from sidebar.</p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh;font-size: 2.5vh;'>You can also use the slider to adjust the value.</p>", unsafe_allow_html=True)

with row5_col1:
    st.markdown("<h3 style='font-size: 3.5vh; '>Wickets Input</h3>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh;font-size: 2.5vh;'>Input the number of wickets out using the sidebar.</p>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top: -2vh; margin-bottom: 4vh; font-size: 2.5vh;'>You can also use the slider to adjust the value.</p>", unsafe_allow_html=True)

with row1_col2:
    st_lottie(lottie_match,height=100)

with row2_col2:
    st_lottie(lottie_city,height=100)

with row3_col2:
    st_lottie(lottie_score,height=100)

with row4_col2:
    st_lottie(lottie_overs,height=100)

with row5_col2:
    st_lottie(lottie_wicket,height=120)



with row1_col3:
    # st.markdown("<h3 style=''> Selected Items </h3>", unsafe_allow_html=True)s
    st.markdown(f"<p style='margin-top:1vh ;font-size: 3vh; '><b>Batting Team:</b> {batting_team}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top: -3vh ;font-size: 3vh;'><b>Bowling Team:</b> {bowling_team}</p>", unsafe_allow_html=True)

with row2_col3:
    st.markdown(f"<p style='margin-top: 4vh ;font-size: 3vh;'><b>City:</b> {city}</p>", unsafe_allow_html=True)

with row3_col3:
    st.markdown(f"<p style='margin-top: 4vh ;font-size: 3vh;'><b>Current Score:</b> {current_score}</p>", unsafe_allow_html=True)

with row4_col3:
    st.markdown(f"<p style='margin-top: 2.8vh;font-size: 3vh;'><b>Selected Overs: </b>{overs}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='margin-top: -3vh;font-size: 3vh;'><b>Last Five Overs Runs:</b> {last_five}</p>", unsafe_allow_html=True)
    
with row5_col3:
    st.markdown(f"<p style='margin-top: 4.5vh;font-size: 3vh;'><b>Selected Wickets: </b>{wickets}</p>", unsafe_allow_html=True)


if st.button('Predict Score'):

    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score / overs
    
    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city,
         'current_score': [0], 'balls_left': [balls_left], 'wickets_left': [wickets],
         'crr': [crr], 'last_five': [last_five]})
    result = pipe.predict(input_df)
    final_Prediction = str(int(result[0]))

    st.markdown(f"<p style='font-size: 5vh; color: #FF5733;'><b>Score Prediction:  </b> {final_Prediction}</p>", unsafe_allow_html=True)