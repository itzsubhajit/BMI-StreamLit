import streamlit as st
st.title("BMI Calculator")
st.info("This app calculates your Body Mass Index (BMI) based on your weight and height.")
weight = st.number_input("Enter your weight in kilograms (kg):", min_value=1.0, max_value=500.0, step=0.1)
height = st.number_input("Enter your height in meters (m):", min_value=0.5, max_value=3.0, step=0.01)
if st.button("Calculate BMI"):
    if height <= 0:
        st.error("Height must be greater than zero.")
    else:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
            st.balloons()
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
st.success("Thank you for using the BMI Calculator! Please consult a healthcare professional for personalized advice.")
