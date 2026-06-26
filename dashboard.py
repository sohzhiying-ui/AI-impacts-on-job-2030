import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load dataset and model
df = pd.read_csv("AI_Impact_on_Jobs_2030.csv")
model = joblib.load("best_model.pkl")

st.title("AI Impacts on Jobs 2030 Dashboard")
st.write("Decision support using Linear Regression predictions")

# --- Visualization 1: Histogram ---
st.subheader("Distribution of Salaries")
fig, ax = plt.subplots()
sns.histplot(df['salary'], bins=20, ax=ax)
st.pyplot(fig)

# --- Visualization 2: Scatter plot ---
st.subheader("Experience vs Salary")
fig, ax = plt.subplots()
sns.scatterplot(x='years_experience', y='salary', data=df, ax=ax)
st.pyplot(fig)

# --- Visualization 3: Correlation Heatmap ---
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# --- Interactive Feature 1: Dropdown ---
st.subheader("Custom Feature Distribution")
feature = st.selectbox("Select feature to visualize:", df.columns)
fig, ax = plt.subplots()
sns.histplot(df[feature], bins=20, ax=ax)
st.pyplot(fig)

# --- Interactive Feature 2: Slider ---
st.subheader("Predict Future Salary")
years_exp = st.slider("Years of Experience", 0, 40, 5)

# --- Predictive Output ---
if st.button("Run Prediction"):
    input_data = pd.DataFrame([[years_exp]], columns=['years_experience'])
    prediction = model.predict(input_data)[0]
    st.write(f"Predicted Salary: {prediction:.2f}")
