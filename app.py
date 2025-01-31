import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page layout
st.set_page_config(layout="wide")

# Define allocated credits
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

# Function to calculate Investability Index manually
def calculate_manual_index(input_values, allocated_credits):
    return sum(input_values[i] * list(allocated_credits.values())[i] for i in range(len(input_values))) / sum(allocated_credits.values())

# Main UI Layout
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])

    # Column 1: Input Sliders
    with col1:
        st.title("📊 Investability Index Calculator")
        st.write("Adjust the sliders to rate each parameter (1-10).")

        # Input sliders
        market_growth = st.slider("Market Growth Potential", 1, 10, 5)
        profitability = st.slider("Profitability", 1, 10, 5)
        competitive_advantage = st.slider("Competitive Advantage", 1, 10, 5)
        management_quality = st.slider("Management Quality", 1, 10, 5)
        innovation_rd = st.slider("Innovation and R&D", 1, 10, 5)
        regulatory_env = st.slider("Regulatory Environment", 1, 10, 5)
        financial_stability = st.slider("Financial Stability", 1, 10, 5)
        sustainability_esg = st.slider("Sustainability and ESG", 1, 10, 5)

        # Calculate manual Investability Index
        input_values = [
            market_growth, profitability, competitive_advantage, management_quality,
            innovation_rd, regulatory_env, financial_stability, sustainability_esg
        ]
        manual_index = calculate_manual_index(input_values, allocated_credits)
        st.success(f"**📊 Manual Investability Index Score:** {manual_index:.2f}/10")

        # Dynamic description based on score
        st.write("### Insights:")
        if manual_index > 7:
            st.write(
                f"The final Investability Index Score is {manual_index:.2f}/10, indicating a relatively attractive investment opportunity. "
                f"Investors can use this score to compare with other industries or companies."
            )
        elif 5 <= manual_index <= 7:
            st.write(
                f"The final Investability Index Score is {manual_index:.2f}/10, indicating a moderate investment opportunity. "
                f"Improving key areas could enhance investment attractiveness."
            )
        else:
            st.write(
                f"The final Investability Index Score is {manual_index:.2f}/10, indicating a low investment potential. "
                f"Significant improvements are required before serious consideration by investors."
            )

    # Column 2: Radar Chart
    with col2:
        st.subheader("📊 Parameter Ratings Visualization (Radar Chart)")

        def plot_radar_chart(scores):
            categories = list(allocated_credits.keys())
            values = scores + scores[:1]
            angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(2.5, 2.5), subplot_kw=dict(polar=True))
            ax.fill(angles, values, color="skyblue", alpha=0.4)
            ax.plot(angles, values, color="blue", linewidth=1.5)
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories, fontsize=8)
            ax.set_yticks([])
            ax.grid(color="gray", linestyle="dotted", linewidth=0.5)
            ax.set_facecolor("#f9f9f9")
            st.pyplot(fig)

        plot_radar_chart(input_values)

    # Column 3: Recommendations
    with col3:
        st.subheader("📌 Detailed Parameter-Based Recommendations")

        # Mock justifications for each parameter
        industry_benchmarks = {
            "Market Growth Potential": "Rated 8/10 (high growth industry with a CAGR of 12%).",
            "Profitability": "Rated 7/10 (above-average net profit margin of 15%).",
            "Competitive Advantage": "Rated 9/10 (strong brand and market leadership).",
            "Management Quality": "Rated 8/10 (experienced team with a proven track record).",
            "Innovation and R&D": "Rated 6/10 (moderate R&D spend but strong IP portfolio).",
            "Regulatory Environment": "Rated 5/10 (moderate regulatory risks).",
            "Financial Stability": "Rated 7/10 (low debt-to-equity ratio of 0.5).",
            "Sustainability and ESG": "Rated 4/10 (limited ESG initiatives but improving)."
        }

        def generate_insights(parameter, value):
            if value >= 8:
                return f"✅ **{parameter}:** Strong! {industry_benchmarks[parameter]}"
            elif value >= 5:
                return f"⚠️ **{parameter}:** Moderate. {industry_benchmarks[parameter]}"
            else:
                return f"❌ **{parameter}:** Weak. Significant improvement is required."

        for i, param in enumerate(allocated_credits.keys()):
            st.write(generate_insights(param, input_values[i]))
