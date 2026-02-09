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
st.markdown("## Submit Your Health Data")

if st.button("Submit"):

    st.success("Data Submitted Successfully!")

    st.write("### Your Submitted Details:")

    st.write("Age:", age)
    st.write("Mood:", mood)
    st.write("Heart Rate:", heart_rate)

    if heart_rate < 60:
        st.warning("⚠️ Low Heart Rate Warning!")
    elif heart_rate > 100:
        st.error("⚠️ High Heart Rate Warning!")
    else:
        st.success("✅ Heart Rate Normal")


if heart_rate < 60:
    st.warning("Low Heart Rate Warning!")
elif heart_rate > 100:
    st.warning("High Heart Rate Warning!")
else:
    st.success("Heart Rate is Normal")
# ---------------- Digital Avatar ----------------

st.markdown("## 🧍 Digital Health Avatar")

status = ""
color = ""

if heart_rate >= 60 and heart_rate <= 100 and mood == "Happy":
    status = "GOOD HEALTH"
    color = "green"

elif heart_rate >= 50 and heart_rate <= 110:
    status = "NORMAL HEALTH"
    color = "orange"

else:
    status = "RISK LEVEL"
    color = "red"

st.markdown(
    f"""
    <div style="padding:20px; border-radius:10px; background-color:{color}; color:white; text-align:center;">
        <h2>🧍 {status}</h2>
    </div>
    """,
    unsafe_allow_html=True
)



