import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("investability_model.pkl")

# Define allocated credits for each parameter
allocated_credits = {
    "Market Growth Potential": 12,
    "Profitability": 10,
    "Competitive Advantage": 10,
    "Management Quality": 8,
    "Innovation and R&D": 8,
    "Regulatory Environment": 6,
    "Financial Stability": 4,
    "Sustainability and ESG": 2
}

st.title("Investability Index Prediction App")
st.write("Enter the startup's parameter ratings to calculate its Investability Index.")

# User input fields
market_growth = st.slider("Market Growth Potential", 1, 10, 5)
profitability = st.slider("Profitability", 1, 10, 5)
competitive_advantage = st.slider("Competitive Advantage", 1, 10, 5)
management_quality = st.slider("Management Quality", 1, 10, 5)
innovation_rd = st.slider("Innovation and R&D", 1, 10, 5)
regulatory_env = st.slider("Regulatory Environment", 1, 10, 5)
financial_stability = st.slider("Financial Stability", 1, 10, 5)
sustainability_esg = st.slider("Sustainability and ESG", 1, 10, 5)

# Create input DataFrame
input_data = pd.DataFrame(
    [[market_growth, profitability, competitive_advantage, management_quality,
      innovation_rd, regulatory_env, financial_stability, sustainability_esg]],
    columns=list(allocated_credits.keys())
)

# Corrected Manual Calculation (Ensures accurate Investability Index computation)
manual_index_score = sum(input_data.iloc[0][param] * allocated_credits[param] for param in allocated_credits) / sum(allocated_credits.values())

# Predict using Model
if st.button("Predict Investability Index"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Investability Index Score: {prediction:.2f}")

    # Display Corrected Investability Index Calculation
    st.write(f"📊 **Manual Calculation (For Debugging):** {manual_index_score:.2f}")

    # Recommendations
    st.subheader("Insights & Recommendations")
    if prediction > 7.0:
        st.write("✅ **High Investability:** Strong potential for investment.")
    elif prediction > 5.0:
        st.write("⚠️ **Moderate Investability:** Requires further assessment.")
    else:
        st.write("❌ **Low Investability:** Consider revising the business model.")
