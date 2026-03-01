import streamlit as st

st.set_page_config(page_title="Human Digital Twin", page_icon="🧍")

# ---------------- SESSION VARIABLES ----------------

if "users" not in st.session_state:
    st.session_state.users = {}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

if "heart_history" not in st.session_state:
    st.session_state.heart_history = []

# ---------------- LOGIN SYSTEM ----------------

if not st.session_state.logged_in:

    st.title("🔐 Login System - Human Digital Twin")

    option = st.radio("Select Option:", ["Login", "Register"])

    # -------- REGISTER --------
    if option == "Register":
        st.subheader("Create New Account")

        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")

        if st.button("Register"):
            if new_user in st.session_state.users:
                st.error("Username already exists!")
            elif new_user == "" or new_pass == "":
                st.warning("Please fill all fields")
            else:
                st.session_state.users[new_user] = new_pass
                st.success("Account created successfully! Please login.")

    # -------- LOGIN --------
    if option == "Login":
        st.subheader("Login to Your Account")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username in st.session_state.users and \
               st.session_state.users[username] == password:

                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

    st.stop()

# ---------------- MAIN DASHBOARD ----------------

st.sidebar.write(f"👤 Logged in as: {st.session_state.current_user}")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.rerun()

st.title("🧍 Human Digital Twin Dashboard")
st.write("Welcome! This is your AI-based Health Monitoring Digital Twin.")

# ---------------- USER INPUTS ----------------

age = st.number_input("Enter your Age:", min_value=1, max_value=120)

if age < 25:
    st.success("Category: Young Adult")
elif age < 60:
    st.success("Category: Adult")
else:
    st.success("Category: Senior")

# ---------------- MOOD ----------------

st.markdown("## 😊 Mood Input")

mood = st.selectbox(
    "Select your Mood Today:",
    ["Happy", "Stressed", "Tired", "Normal"]
)

# ---------------- BMI ----------------

st.markdown("## 🏋 Body Mass Index (BMI) Calculator")

weight = st.number_input("Enter your Weight (kg):", min_value=1.0, step=0.5)
height = st.number_input("Enter your Height (meters):", min_value=0.5, step=0.01)

bmi = None

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

# ---------------- HEART RATE ----------------

heart_rate = st.number_input(
    "Enter Heart Rate:",
    min_value=30,
    max_value=200
)

# ---------------- SUBMIT ----------------

if st.button("Submit Health Data"):

    st.success("✅ Data Submitted Successfully!")

    st.session_state.heart_history.append(heart_rate)

    st.write("### 📋 Submitted Details:")
    st.write("Age:", age)
    st.write("Mood:", mood)
    st.write("Heart Rate:", heart_rate)

    if bmi:
        st.write("BMI:", round(bmi, 2))

    # Heart Rate Alert
    if heart_rate < 60:
        st.warning("⚠️ Low Heart Rate Warning!")
    elif heart_rate > 100:
        st.error("⚠️ High Heart Rate Warning!")
    else:
        st.success("✅ Heart Rate Normal")

    # AI Suggestion
    st.markdown("## 🤖 AI Health Suggestion")

    if mood == "Happy" and 60 <= heart_rate <= 100:
        advice = "Great! Your health looks good. Keep maintaining a healthy lifestyle 😊"
    elif mood == "Stressed":
        advice = "You seem stressed. Try meditation or deep breathing 🧘"
    elif mood == "Tired":
        advice = "Get proper sleep and stay hydrated 😴"
    elif heart_rate > 100:
        advice = "Your heart rate is high. Take rest ❤️"
    elif heart_rate < 60:
        advice = "Your heart rate is low. Maintain balanced diet 🍎"
    else:
        advice = "Your health is normal. Maintain good habits 👍"

    st.info(advice)

# ---------------- HEART RATE GRAPH ----------------

st.markdown("## 📊 Heart Rate History")

if len(st.session_state.heart_history) > 0:
    st.line_chart(st.session_state.heart_history)
