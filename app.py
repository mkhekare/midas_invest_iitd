import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page layout to wide mode for better alignment
st.set_page_config(layout="wide")

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

# Main container for fixed one-window layout
with st.container():
    # Divide the layout into 3 equal columns
    col1, col2, col3 = st.columns([1, 1, 1])  # Equal proportions

    # Column 1: Input Sliders
    with col1:
        st.title("📊 Investability Index Calculator")
        st.write("Adjust the sliders to rate each parameter (1-10).")

        # User Input Sliders
        market_growth = st.slider("Market Growth Potential", 1, 10, 5)
        profitability = st.slider("Profitability", 1, 10, 5)
        competitive_advantage = st.slider("Competitive Advantage", 1, 10, 5)
        management_quality = st.slider("Management Quality", 1, 10, 5)
        innovation_rd = st.slider("Innovation and R&D", 1, 10, 5)
        regulatory_env = st.slider("Regulatory Environment", 1, 10, 5)
        financial_stability = st.slider("Financial Stability", 1, 10, 5)
        sustainability_esg = st.slider("Sustainability and ESG", 1, 10, 5)

        # Compute Investability Index
        input_values = [
            market_growth, profitability, competitive_advantage, management_quality,
            innovation_rd, regulatory_env, financial_stability, sustainability_esg
        ]
        investability_index = sum(input_values[i] * list(allocated_credits.values())[i] for i in range(len(input_values))) / sum(allocated_credits.values())

        # Display Calculated Investability Score
        st.success(f"**📊 Investability Index Score:** {investability_index:.2f}")

        # Overall Recommendation
        st.subheader("🔍 Investment Readiness Insights")
        if investability_index > 7.0:
            st.write("✅ **High Investability:** This startup has strong potential. Investors should consider further due diligence.")
        elif investability_index > 5.0:
            st.write("⚠️ **Moderate Investability:** Needs improvement in certain areas before serious investment consideration.")
        else:
            st.write("❌ **Low Investability:** Business model needs significant improvements before it becomes investable.")

    # Column 2: Radar Chart
    with col2:
        st.subheader("📊 Parameter Ratings Visualization (Radar Chart)")

        def plot_radar_chart(scores):
            categories = list(allocated_credits.keys())
            values = scores + scores[:1]  # Close the radar chart loop
            angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(2.5, 2.5), subplot_kw=dict(polar=True))  # Compact size
            ax.fill(angles, values, color="skyblue", alpha=0.4)
            ax.plot(angles, values, color="blue", linewidth=1.5)
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories, fontsize=8, color="black")
            ax.set_yticks([])
            ax.grid(color="gray", linestyle="dotted", linewidth=0.5)
            ax.set_facecolor("#f9f9f9")

            st.pyplot(fig)

        plot_radar_chart(input_values)

    # Column 3: Detailed Recommendations
    with col3:
        st.subheader("📌 Detailed Parameter-Based Recommendations")

        # Function to generate insights dynamically
        def generate_insights(parameter, value):
            if value >= 8:
                return f"✅ **{parameter}:** Strong! Leverage this as a key strength for investors."
            elif value >= 5:
                return f"⚠️ **{parameter}:** Moderate. Improve this area to strengthen investment appeal."
            else:
                return f"❌ **{parameter}:** Weak. Requires significant improvement to boost investability."

        # Display insights for each parameter dynamically
        for i, param in enumerate(allocated_credits.keys()):
            st.write(generate_insights(param, input_values[i]))
