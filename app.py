import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import requests

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

# Function to fetch real-time data (example: from APIs or websites)
def fetch_real_time_data(parameter):
    try:
        if parameter == "Market Growth Potential":
            # Example API for real-time CAGR data
            response = requests.get("https://api.example.com/industry-cagr")
            data = response.json()
            return f"{data['industry']} with a CAGR of {data['cagr']}%."
        elif parameter == "Profitability":
            return "Industry average net profit margin is 15%."
        elif parameter == "Sustainability and ESG":
            return "Significant focus on green initiatives with improving ESG scores."
        else:
            return f"Dynamic benchmark data for {parameter} not available."
    except:
        return f"Static insights for {parameter} due to no real-time data."

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
                f"**The final Investability Index Score is {manual_index:.2f}/10, indicating a relatively attractive investment opportunity. "
                f"Investors can use this score to compare with other industries or companies.**"
            )
        elif 5 <= manual_index <= 7:
            st.write(
                f"**The final Investability Index Score is {manual_index:.2f}/10, indicating a moderate investment opportunity. "
                f"Improving key areas could enhance investment attractiveness.**"
            )
        else:
            st.write(
                f"**The final Investability Index Score is {manual_index:.2f}/10, indicating a low investment potential. "
                f"Significant improvements are required before serious consideration by investors.**"
            )

    # Column 2: Radar Chart
    with col2:
        st.title("📊 Parameter Ratings Visualization")

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
        st.title("📌 Detailed Parameter-Based Recommendations")

        def generate_insights(parameter, value):
            real_time_data = fetch_real_time_data(parameter)
            if value >= 8:
                return f"✅ **{parameter}:** Strong! {real_time_data}"
            elif value >= 5:
                return f"⚠️ **{parameter}:** Moderate. {real_time_data}"
            else:
                return f"❌ **{parameter}:** Weak. {real_time_data}"

        for i, param in enumerate(allocated_credits.keys()):
            st.write(generate_insights(param, input_values[i]))
