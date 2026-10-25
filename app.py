
import streamlit as st
import pandas as pd
import joblib

# Load our trained AI model
model = joblib.load("student_model.pkl")

# Website heading
st.title("Student Performance Predictor")
st.write("Predict your expected final marks using ML.")

# Input 1: Daily study hours
study_hours = st.number_input(
    "Daily study hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

# Input 2: Previous marks
previous_marks = st.number_input(
    "Previous marks (out of 100)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

# Run prediction when the button is clicked
if st.button("Predict Performance"):

    student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Previous_Marks": [previous_marks]
    })

    prediction = model.predict(student)[0]

    # Keep the displayed result between 0 and 100
    prediction = max(0, min(100, prediction))

    st.success(
        f"Predicted final marks: {prediction:.2f}/100"
    )

    if prediction < 40:
        st.write("Estimated category: Needs improvement")
    elif prediction < 70:
        st.write("Estimated category: Moderate")
    else:
        st.write("Estimated category: High")
