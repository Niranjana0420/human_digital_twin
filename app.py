import streamlit as st

st.title("Human Digital Twin Project")

st.write("Welcome! This is your Health Monitoring Digital Twin.")

# Age Category Feature
age = st.number_input("Enter your Age:", min_value=1, max_value=120)

if age < 25:
    st.success("Category: Young Adult")
elif age < 60:
    st.success("Category: Adult")
else:
    st.success("Category: Senior")

# Mood Tracker Feature
mood = st.selectbox("Select your Mood Today:", ["Happy", "Stressed", "Tired", "Normal"])

st.write("Your mood is:", mood)

# Heart Rate Alert Feature
heart_rate = st.number_input("Enter Heart Rate:", min_value=30, max_value=200)

if heart_rate < 60:
    st.warning("Low Heart Rate Warning!")
elif heart_rate > 100:
    st.warning("High Heart Rate Warning!")
else:
    st.success("Heart Rate is Normal")

