import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("investability_model.pkl")

# Streamlit UI
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

# Prepare input data
input_data = pd.DataFrame(
    [[market_growth, profitability, competitive_advantage, management_quality,
      innovation_rd, regulatory_env, financial_stability, sustainability_esg]],
    columns=[
        "Market Growth Potential", "Profitability", "Competitive Advantage",
        "Management Quality", "Innovation and R&D", "Regulatory Environment",
        "Financial Stability", "Sustainability and ESG"
    ]
)

# Predict Investability Index
if st.button("Predict Investability Index"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Investability Index Score: {prediction:.2f}")

    # Recommendations
    st.subheader("Insights & Recommendations")
    if prediction > 7.0:
        st.write("✅ **High Investability:** Strong potential for investment.")
    elif prediction > 5.0:
        st.write("⚠️ **Moderate Investability:** Requires further assessment.")
    else:
        st.write("❌ **Low Investability:** Consider revising the business model.")