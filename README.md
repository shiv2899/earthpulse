# 🌍 EarthPulse - AI Earth System Trend Detective

**【entity-NASA¦canonical_name=NASA】 Space Apps Challenge 2026**
Challenge: *Be An Earth System Trend Detective!*
Team: EarthPulse India 2026 Shivankush
Location: Kanpur, India

> A simple AI dashboard that uses 【entity-NASA¦canonical_name=NASA】 open Earth data to detect temperature and rainfall trends and predict future climate for a city.

---

## 📸 What does it do?

EarthPulse answers one simple question in 1 minute:

> **"Mere sheher ka temperature badh raha hai ya nahi?"**

It takes 【entity-NASA¦canonical_name=NASA】 POWER open data for Kanpur, India, shows past 20 years trends with clear graphs, and uses Machine Learning to predict future temperature.

**Live Demo Slides:** [View Presentation](https://docs.google.com/presentation/d/YOUR_SLIDES_LINK_HERE)
**Space Apps Project Page:** https://www.spaceappschallenge.org

---

## 📊 Key Findings - Kanpur (2005-2024)

| Metric | 2005 | 2024 | Trend |
| :--- | :--- | :--- | :--- |
| Avg Temperature | 26.1°C | 28.3°C | ⬆️ Increasing |
| Rainfall | 820 mm | 620 mm | ⬇️ Decreasing |

**AI Prediction (Linear Regression):**
> In 2030, Kanpur's average temperature may reach **~28.8°C**

**Conclusion:** Kanpur is getting hotter and receiving less rainfall. This is a clear climate trend visible in NASA data.

---

## 🛠️ How it works

1. **Data Collection:** Yearly average temperature and rainfall data from 【entity-NASA POWER Data Access Viewer¦canonical_name=NASA】.
2. **Data Cleaning:** Python + Pandas is used to clean and structure the data.
3. **Visualization:** Matplotlib + Streamlit charts show Temperature and Rainfall trends.
4. **AI Prediction:** Scikit-learn `LinearRegression` model is trained on `Year -> Temperature` to predict 2025-2030 temperature.

**Tools Used:**
- Python, Pandas, Matplotlib, Scikit-learn
- Streamlit for Dashboard
- 【entity-NASA¦canonical_name=NASA】 POWER Data
- Google Slides for Demo

---

## 🚀 How to Run

```bash
# 1. Install dependencies
pip install streamlit pandas matplotlib scikit-learn

# 2. Run the app
streamlit run app.py
