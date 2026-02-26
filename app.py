import streamlit as st

st.set_page_config(page_title="Human Digital Twin", page_icon="🧍")

st.title("🧍 Human Digital Twin Project")
st.write("Welcome! This is your AI-based Health Monitoring Digital Twin.")

# ---------------- User Inputs ----------------

age = st.number_input("Enter your Age:", min_value=1, max_value=120)

if age < 25:
    st.success("Category: Young Adult")
elif age < 60:
    st.success("Category: Adult")
else:
    st.success("Category: Senior")

mood = st.selectbox("Select your Mood Today:", 
                    ["Happy", "Stressed", "Tired", "Normal"])

# 👇👇 PASTE BMI CODE HERE 👇👇

st.markdown("## 🏋 Body Mass Index (BMI) Calculator")

weight = st.number_input("Enter your Weight (kg):", min_value=1.0, step=0.5)
height = st.number_input("Enter your Height (meters):", min_value=0.5, step=0.01)

if height > 0:
    bmi = weight / (height ** 2)
    st.write("### Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.warning("Category: Underweight")
    elif bmi < 25:
        st.success("Category: Normal Weight")
    elif bmi < 30:
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")

# 👆👆 BMI END HERE 👆👆

heart_rate = st.number_input("Enter Heart Rate:", min_value=30, max_value=200)

st.markdown("## Submit Your Health Data")
heart_rate = st.number_input("Enter Heart Rate:", 
                             min_value=30, max_value=200)

st.markdown("## Submit Your Health Data")

# ---------------- Submit Button ----------------

if st.button("Submit"):

    st.success("✅ Data Submitted Successfully!")

    st.write("### 📋 Your Submitted Details:")
    st.write("Age:", age)
    st.write("Mood:", mood)
    st.write("Heart Rate:", heart_rate)

    # ---------------- Heart Rate Alert ----------------

    if heart_rate < 60:
        st.warning("⚠️ Low Heart Rate Warning!")
    elif heart_rate > 100:
        st.error("⚠️ High Heart Rate Warning!")
    else:
        st.success("✅ Heart Rate Normal")

    # ---------------- AI Health Suggestion ----------------

    st.markdown("## 🤖 AI Health Suggestion")

    if mood == "Happy" and 60 <= heart_rate <= 100:
        advice = "Great! Your health looks good. Keep maintaining a healthy lifestyle 😊"

    elif mood == "Stressed":
        advice = "You seem stressed. Try deep breathing, meditation, or listening to calm music 🧘"

    elif mood == "Tired":
        advice = "You look tired. Get enough sleep and stay hydrated 😴"

    elif heart_rate > 100:
        advice = "Your heart rate is high. Avoid stress and take some rest ❤️"

    elif heart_rate < 60:
        advice = "Your heart rate is low. Eat well and stay active 🍎"

    else:
        advice = "Your health is normal. Maintain good habits 👍"

    st.info(advice)

    # ---------------- Digital Avatar ----------------

    st.markdown("## 🧍 Digital Health Avatar")

    if 60 <= heart_rate <= 100 and mood == "Happy":
        status = "GOOD HEALTH"
        color = "green"

    elif 50 <= heart_rate <= 110:
        status = "NORMAL HEALTH"
        color = "orange"

    else:
        status = "RISK LEVEL"
        color = "red"

    st.markdown(
        f"""
        <div style="padding:20px; border-radius:10px; background-color:{color}; 
        color:white; text-align:center;">
            <h2>{status}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )







