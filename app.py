import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

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

st.set_page_config(layout="wide")  # Prevents scrolling

# Main Container for UI
with st.container():

    # Create 3 columns for better alignment
    col1, col2 = st.columns([2, 3])

    # Left Column: Input Sliders
    with col1:
        st.title("Investability Index Prediction")
        st.write("Adjust the sliders to set ratings for each parameter (1-10).")

        # User Input Sliders
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

        # Predict using Model
        prediction = model.predict(input_data)[0]
        st.success(f"**Predicted Investability Index Score:** {prediction:.2f}")

        # Recommendations Based on Score
        st.subheader("Overall Investment Insight:")
        if prediction > 7.0:
            st.write("✅ **High Investability:** Strong potential for investment. Consider moving forward with due diligence.")
        elif prediction > 5.0:
            st.write("⚠️ **Moderate Investability:** The startup has moderate potential. Needs improvement in key areas.")
        else:
            st.write("❌ **Low Investability:** Consider revising the business model before investment.")

    # Right Column: Radar Chart
    with col2:
        st.subheader("Parameter Ratings Visualization")

        # Radar Chart
        def plot_radar_chart(scores):
            categories = list(allocated_credits.keys())
            values = scores + scores[:1]  # Close the radar chart loop
            angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
            ax.fill(angles, values, color="blue", alpha=0.25)
            ax.plot(angles, values, color="blue", linewidth=2)
            ax.set_yticklabels([])
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories, fontsize=9)
            ax.set_title("Startup Parameter Ratings")

            st.pyplot(fig)

        plot_radar_chart([
            market_growth, profitability, competitive_advantage, management_quality,
            innovation_rd, regulatory_env, financial_stability, sustainability_esg
        ])

# Insights Section (Fixed Below)
st.subheader("Detailed Parameter-Based Recommendations")

insight_text = {
    "Market Growth Potential": "📈 Strong growth in your industry boosts investor confidence. Ensure market expansion plans are in place.",
    "Profitability": "💰 A high-profit margin makes your startup attractive. Focus on cost optimization and revenue scalability.",
    "Competitive Advantage": "🏆 Stand out by emphasizing unique strengths over competitors. Consider patents, brand power, or exclusive partnerships.",
    "Management Quality": "👥 Strong leadership drives success. Ensure an experienced and adaptable team with clear strategic direction.",
    "Innovation and R&D": "🔬 Continuous innovation ensures long-term viability. Secure intellectual property rights and increase R&D investment.",
    "Regulatory Environment": "⚖️ A stable regulatory environment reduces investment risk. Ensure compliance with industry-specific laws.",
    "Financial Stability": "📊 Solid financial health reassures investors. Maintain strong cash flow and reduce liabilities.",
    "Sustainability and ESG": "🌍 Social and environmental responsibility attracts ethical investors. Improve sustainability practices and corporate governance."
}

for key, value in insight_text.items():
    st.write(f"**{key}:** {value}")