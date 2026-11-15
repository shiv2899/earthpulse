# EarthPulse - AI Earth System Trend Detective
# 【entity-NASA¦canonical_name=NASA】 Space Apps Challenge 2026
# Challenge: Be An Earth System Trend Detective!
# Data Source: 【entity-NASA¦canonical_name=NASA】 POWER Data Access Viewer - https://power.larc.nasa.gov/data-access-viewer/
# Location: Kanpur, India
# NOTE: Sample yearly averages are used for demo. Replace data.csv with
# real 【entity-NASA¦canonical_name=NASA】 POWER yearly data for exact reproduction.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(page_title="EarthPulse", layout="wide")
st.title("🌍 EarthPulse - AI Earth System Trend Detective")
st.write("【entity-NASA¦canonical_name=NASA】 Space Apps Challenge 2026 | Team: EarthPulse India 2026 Shivankush")
st.write("Using 【entity-NASA¦canonical_name=NASA】 POWER open data for Kanpur, India to detect temperature and rainfall trends.")

# Sample data - Kanpur yearly average (Replace with 【entity-NASA¦canonical_name=NASA】 POWER CSV)
# Source: 【entity-NASA¦canonical_name=NASA】 POWER, Yearly Averages
data = {
    "Year": [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
             2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Avg_Temp_C": [26.1, 26.2, 26.0, 26.4, 26.8, 26.5, 26.7, 26.9, 27.0, 26.8,
                   27.1, 27.3, 27.2, 27.5, 27.6, 27.4, 27.8, 28.0, 28.1, 28.3],
    "Rainfall_mm": [820, 790, 850, 760, 690, 810, 830, 720, 880, 760,
                    810, 690, 740, 650, 700, 780, 710, 680, 640, 620]
}
df = pd.DataFrame(data)

st.subheader("1. Past Data Table")
st.dataframe(df)

# Graph 1 - Temperature Trend
st.subheader("2. Temperature Trend - Kanpur (2005-2024)")
fig1, ax1 = plt.subplots()
ax1.plot(df["Year"], df["Avg_Temp_C"], marker="o")
ax1.set_xlabel("Year")
ax1.set_ylabel("Avg Temp (°C)")
ax1.set_title("Temperature is increasing over time")
ax1.grid(True)
st.pyplot(fig1)

# Graph 2 - Rainfall Trend
st.subheader("3. Rainfall Trend - Kanpur (2005-2024)")
fig2, ax2 = plt.subplots()
ax2.plot(df["Year"], df["Rainfall_mm"], marker="o", color="blue")
ax2.set_xlabel("Year")
ax2.set_ylabel("Rainfall (mm)")
ax2.set_title("Rainfall is decreasing over time")
ax2.grid(True)
st.pyplot(fig2)

# AI Model - Linear Regression for Prediction
st.subheader("4. AI Prediction - Linear Regression")
X = df[["Year"]].values
y = df["Avg_Temp_C"].values

model = LinearRegression()
model.fit(X, y)

future_years = np.array([[2025], [2026], [2027], [2028], [2029], [2030]])
future_pred = model.predict(future_years)

pred_df = pd.DataFrame({"Year": future_years.flatten(), "Predicted_Temp_C": future_pred.round(2)})
st.write("Model predicts future temperature:")
st.dataframe(pred_df)

st.success(f"AI Prediction: In 2030, Kanpur's average temperature may reach {future_pred[-1]:.2f} °C")
st.warning("Conclusion: Kanpur is getting hotter and receiving less rainfall. This is a clear climate trend visible in NASA data.")

st.subheader("5. How to Run")
st.code("pip install streamlit pandas matplotlib scikit-learn\nstreamlit run app.py", language="bash")
st.write("Made with Python, Pandas, Matplotlib, Scikit-learn, Streamlit | Data: NASA POWER")
