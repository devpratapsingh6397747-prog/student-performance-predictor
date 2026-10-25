

import streamlit as st
import pandas as pd
import joblib

# Load the trained AI model
model = joblib.load("student_model.pkl")

# Website heading
st.title("Student Performance Predictor")
st.write("Predict your expected final marks using machine learning.")

# Student inputs
study_hours = st.number_input(
    "Daily study hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

previous_marks = st.number_input(
    "Previous marks (out of 100)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

st.subheader("Class Attendance")

total_classes = st.number_input(
    "Total classes conducted",
    min_value=1,
    value=100
)

classes_attended = st.number_input(
    "Classes attended",
    min_value=0,
    max_value=total_classes,
    value=min(80, total_classes)
)

attendance_percentage = (
    classes_attended / total_classes
) * 100

st.metric(
    "Attendance Percentage",
    f"{attendance_percentage:.1f}%"
)

# Make prediction
if st.button("Predict Performance"):

    if classes_attended > total_classes:
        st.error("Classes attended cannot exceed total classes.")
    else:
        student = pd.DataFrame({
            "Study_Hours": [study_hours],
            "Previous_Marks": [previous_marks],
            "Attendance_Percentage": [attendance_percentage]
        })

        prediction = model.predict(student)[0]
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
st.divider()

st.markdown("""
<div style="
    text-align: center;
    font-family: 'Times New Roman', serif;
    font-size: 28px;
    font-weight: bold;
    font-style: normal;
    padding: 15px;
    letter-spacing: 1px;
">
    AI Project by Anikta, Tanvi, Raunak &amp; Dev
</div>
""", unsafe_allow_html=True)
