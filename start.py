import subprocess
import time
import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def open_second_app():
    subprocess.run(["streamlit", "run", "app.py"])

def main():
    # Set page title and icon
    st.set_page_config(page_title="T20i Score Predictor", page_icon="🏏", layout="wide")

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_url_download = "https://lottie.host/b7951fbf-0e54-4698-86c6-da17ce4e62e6/TzA1r8LrDd.json"
    lottie_url_main = "https://lottie.host/bbae91ee-561f-440c-bfc4-571ff9c1f1b6/EnsLy9J0ej.json"
    lottie_url_hello = "https://lottie.host/49a51a90-c31e-41b6-9a96-602ee48204af/Bc8QyUsjQm.json"
    lottie_download = load_lottieurl(lottie_url_download)
    lottie_main = load_lottieurl(lottie_url_main)
    lottie_hello = load_lottieurl(lottie_url_hello)



    # Sidebar
    # st.sidebar.markdown("<h1 style='color: #3366FF; font-size: 4vh; margin-top:-10vh;'>Series Information</h1>", unsafe_allow_html=True)s
     # Current Matches Links
    current_matches = st.sidebar.markdown("<p style='font-weight: bold; font-size: 2.5vh; color: #F0122D'>Current Series</p>", unsafe_allow_html=True)

    st.sidebar.markdown("<div style='display: flex; align-items: center; '><a href='https://www.cricbuzz.com/cricket-series/6927/england-tour-of-india-2024/matches' target='_blank'><img src='https://tse1.mm.bing.net/th?id=OIF.zY1kLT%2f3sQqk7cGmOLqCWQ&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px; '><a href='https://www.cricbuzz.com/cricket-series/6927/england-tour-of-india-2024/matches' target='_blank' style='color: #708090; font-weight: 800;'>England tour of India</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>Jan 25 - Mar 11, 2024</span></div></div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.cricbuzz.com/cricket-series/6892/south-africa-tour-of-new-zealand-2024/matches' target='_blank'><img src='https://tse3.mm.bing.net/th?id=OIP.c35cNAe1slxW10dVAKBvMgHaE4&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.cricbuzz.com/cricket-series/6892/south-africa-tour-of-new-zealand-2024/matches' target='_blank' style='color: #708090; font-weight: 800;'>South Africa VS New Zealand</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;>Jan 29 - Feb 17, 2024</span></div></div>", unsafe_allow_html=True)

    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.cricbuzz.com/cricket-series/7481/afghanistan-tour-of-sri-lanka-2024/matches' target='_blank'><img src='https://tse4.mm.bing.net/th?id=OIP.JKEjp0QO-Icry2jyuQTuUQHaEK&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.cricbuzz.com/cricket-series/7481/afghanistan-tour-of-sri-lanka-2024/matches' target='_blank' style='color: #708090; font-weight: 800;'>Afghanistan tour of Sri Lanka</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>Feb 02 - Feb 21, 2024</span></div></div>", unsafe_allow_html=True)

    st.sidebar.markdown("<a href='https://www.cricbuzz.com/cricket-match/live-scores' style='color: #708090; font-weight: 700; font-size: 14px;'>See More</a>", unsafe_allow_html=True)


    # Recent Matches Links
    recent_matches = st.sidebar.markdown("<p style='font-weight: bold; font-size: 2.5vh; color: #F0122D'>Recent Series</p>", unsafe_allow_html=True)

    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.espncricinfo.com/series/pakistan-in-new-zealand-t20is-2023-24-1388185/match-schedule-fixtures-and-results' target='_blank'><img src='https://tse4.mm.bing.net/th?id=OIP.EEZCs-6c_tLWPOjoVmZbjwHaD4&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.espncricinfo.com/series/pakistan-in-new-zealand-t20is-2023-24-1388185/match-schedule-fixtures-and-results' target='_blank' style='color: #708090; font-weight: 800;'>New Zealand vs Pakistan</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>Jan 12 - Jan 21, 2024</span></div></div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.espncricinfo.com/series/afghanistan-in-india-2023-24-1389384' target='_blank'><img src='https://tse1.mm.bing.net/th?id=OIP.GoHZrAmbgSaolASUwr1GxgHaE7&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.espncricinfo.com/series/afghanistan-in-india-2023-24-1389384' style='color: #708090; font-weight: 800;'>India vs Afghanistan</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>Jan 11 - Jan 17, 2024</span></div></div>", unsafe_allow_html=True)

    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.espncricinfo.com/series/zimbabwe-in-sri-lanka-2023-24-1412536' target='_blank'><img src='https://tse4.mm.bing.net/th?id=OIF.CJHzScyEjdaa8cYV%2fwzzeA&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.espncricinfo.com/series/zimbabwe-in-sri-lanka-2023-24-1412536' target='_blank' style='color: #708090; font-weight: 800;'>Sri Lanka vs Zimbabwe</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>Jan 06 - Jan 18, 2024</span></div></div>", unsafe_allow_html=True)

    st.sidebar.markdown("<a href='https://www.espncricinfo.com/cricket-fixtures/#recent' style='color: #708090; font-weight: 700; font-size: 14px;'>See More</a>", unsafe_allow_html=True)

    # Future Matches Linkss
    future_matches = st.sidebar.markdown("<p style='font-weight: bold; font-size: 2.5   vh; color: #F0122D;'>Future Series</p>", unsafe_allow_html=True)

    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.cricbuzz.com/cricket-series/6899/australia-tour-of-new-zealand-2024/matches' target='_blank'><img src='https://tse2.mm.bing.net/th?id=OIP.qoFSb0UPFA9aM9ItjLPAbwHaEK&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.cricbuzz.com/cricket-series/6899/australia-tour-of-new-zealand-2024/matches' style='color: #708090; font-weight: 800;'>Australia v New Zealand</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>Feb 21 - Mar 24, 2024</span></div></div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.cricbuzz.com/cricket-series/7485/afghanistan-v-ireland-in-uae-2024/matches' target='_blank'><img src='https://tse3.mm.bing.net/th?id=OIP.E0ehUcLEXdmtL-uzfr2iEAHaFB&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.cricbuzz.com/cricket-series/7485/afghanistan-v-ireland-in-uae-2024/matches' target='_blank' style='color: #708090; font-weight: 800;'>Afghanistan v Ireland in UAE</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>Feb 28 - Mar 18, 2024</span></div></div>", unsafe_allow_html=True)


    st.sidebar.markdown("<div style='display: flex; align-items: center;'><a href='https://www.cricbuzz.com/cricket-series/6773/pakistan-tour-of-england-2024/matches' target='_blank'><img src='https://tse1.mm.bing.net/th?id=OIP.OVfl7nO7IOSEa_2FAFPf6QHaEZ&pid=Api&P=0&h=220' width='40' height='40'></a> <div style='margin-left: 10px;'><a href='https://www.cricbuzz.com/cricket-series/6773/pakistan-tour-of-england-2024/matches' target='_blank' style='color: #708090; font-weight: 800;'> Pakistan tour of England, 2024</a> <br> <span style='font-size: 10px; color: 6F5F5F; font-weight: 600;'>May 22 - May 30, 2024</span></div></div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<a href='https://www.cricbuzz.com/cricket-schedule/series' style='color: #708090; font-weight: 700; font-size: 14px;'>See More</a>", unsafe_allow_html=True)

    st.sidebar.markdown("<p style='margin-top:2vh; font-weight: bold; font-size: 2.5vh; color: #F0122D; '>Upcoming Worldcup</p>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<img src='https://tse2.mm.bing.net/th?id=OIP.XxWIYjc9nRlxjCpD7YiOEgHaFj&pid=Api&P=0&h=220' width='250' height='200' style='border: 3px solid #c5e1a5;'>", unsafe_allow_html=True)

    st.sidebar.markdown("<p style='margin-top:1vh;font-weight: bold; font-size: 2vh; color: #708090; '>Next Men's T20 World Cup set to be played from June 4 to 30, 2024</p>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='margin-top:-2vh;font-weight: 800; font-size: 2vh; color: 6F5F5F'>Florida, Morrisville, Dallas and New York among shortlisted venues inspected by ICC, with USA set to co-host tournament with West Indies</p>", unsafe_allow_html=True)

    st.sidebar.markdown("<a href='https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/match-schedule-fixtures-and-results' style='color: #708090;  font-size: 14px; font-weight: 700;'>T20 World Cup 2024 Schedule</a>", unsafe_allow_html=True)

    st.sidebar.markdown("<a href='https://www.geo.tv/latest/525865-icc-unveils-t20-world-cup-2024-schedule#:~:text=Groups%20for%20T20%20World%20Cup%202024%20Group%20A%3A,D%3A%20South%20Africa%2C%20Sri%20Lanka%2C%20Bangladesh%2C%20Netherlands%2C%20Nepal' style='color: #708090; font-weight: 700; font-size: 14px;'>ICC Men's T20 World Cup 2024 Teams</a>", unsafe_allow_html=True)

    st.sidebar.markdown("<a href='https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/teams' style='color: #708090;; font-size: 14px; font-weight: 700;'> T20 World Cup 2024 Groups</a>", unsafe_allow_html=True)


    # Center part
    row1_col1, row1_col2,row1_col3 = st.columns([0.6,1.7,0.7])  


    with row1_col1:
        st_lottie(lottie_hello,height=180)

    row1_col2.markdown("<h1 style='text-align: center; margin-top: -7vh; margin-bottom: 3vh; color: #F0122D; font-size: 36px;'>T20i Cricket Score Predictor</h1>", unsafe_allow_html=True)
    row1_col2.markdown("<p style='text-align: center; font-size: 18px; margin-top: -3vh; '>Welcome to the T20 International Cricket Score Predictor! This app leverages advanced machine learning with an XGBoost model to provide accurate predictions for T20 International cricket scores. Whether you're a cricket enthusiast or just curious about the outcome of a match, this app allows you to input key details such as batting and bowling teams, the city where the match is played, current score, overs, wickets, and runs scored in the last five overs.</p>", unsafe_allow_html=True)

    with row1_col3:
        st_lottie(lottie_main,height=220)
    

    row2_col1, row2_col2 = st.columns([0.83, 1.18])  


    row2_col1.markdown("<h1 style='margin-top: -2vh; margin-bottom: 3vh; color: #F0122D; font-size: 30px;'>How To Use:</h1>", unsafe_allow_html=True)
    row2_col1.markdown("<p style='text-align: left; font-size: 18px; margin-top: -1vh;'><b>Team & City Selection:</b> Choose the batting and bowling teams from a list of international cricket teams.Then select the city.</p>", unsafe_allow_html=True)
    row2_col1.markdown("<p style='text-align: left; font-size: 18px; margin-top: -1vh;'><b>Match Progress:</b> Input the current score, overs completed, wickets, and runs scored in the last five overs.</p>", unsafe_allow_html=True)
    row2_col1.markdown("<p style='text-align: left; font-size: 18px; margin-top: -1vh;'><b>Predict Score:</b> Click the (Predict Score) button to get the predicted T20 International cricket score.</p>", unsafe_allow_html=True)
    row2_col1.markdown("<p style='text-align: center; font-size: 18px; margin-top: -1vh;'>The app takes into account various factors to provide an insightful and data-driven prediction for the upcoming cricket score. It's your go-to tool for anticipating the outcome of T20 International matches.</p>", unsafe_allow_html=True)
    row2_col1.markdown("<p style='text-align: center; font-size: 18px; margin-top: -1vh; margin-bottom: 3vh;'>Enjoy predicting and stay tuned for exciting cricket action!🏏</p>", unsafe_allow_html=True)


    row2_col2.markdown("<h1 style='margin-top: -2vh; margin-bottom: 3vh; color: #F0122D; font-size: 30px;'>See The Video To Understand  How It Work's</h1>", unsafe_allow_html=True)
    row2_col2.video("project-video.mp4", start_time=0)
    
   
    # row2_col2.markdown("<h1 style='text-align: center; margin-top: -2vh; margin-bottom: 3vh; color: #FF5733; font-size: 36px;'>MEN'S T20I TEAM RANKINGS</h1>", unsafe_allow_html=True)

    # row2_col2.image("standings.jpeg", output_format='JPEG')

    if row2_col1.button("Get Started"):
        with row2_col1:
            with st_lottie_spinner(lottie_download, height=70, width=100, key="download"):
                time.sleep(6)
            st.balloons()
            open_second_app()

if __name__ == "__main__":
    main()
