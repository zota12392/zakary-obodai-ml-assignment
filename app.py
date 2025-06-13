import streamlit as st
import joblib
import numpy as np

# Load model and column names
model = joblib.load("titanic_model.pkl")
columns = joblib.load("model_columns.pkl")

st.title("\nMY MODEL")

st.write("\nPREDICTION:")

# User input form
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", min_value=0, max_value=100, value=30)
sibsp = st.slider("Siblings/Spouses Aboard", 0, 8, 0)
parch = st.slider("Parents/Children Aboard", 0, 6, 0)
fare = st.number_input("Fare Paid", min_value=0.0, value=32.0)
embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

# Convert inputs to model-ready format
sex = 0 if sex == "male" else 1
embarked_map = {"S": 0, "C": 1, "Q": 2}
embarked = embarked_map[embarked]

input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
input_df = dict(zip(columns, input_data.flatten()))

# Predict
if st.button("Predict"):
    prediction = model.predict([list(input_df.values())])[0]
    if prediction == 1:
        st.success("✅ Survived!")
    else:
        st.error("❌ Did not survive.")
