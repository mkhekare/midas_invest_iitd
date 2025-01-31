import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page layout
st.set_page_config(layout="wide")

# Industry Benchmark Data
industry_data = {
    "Fintech": {
        "CAGR": "15-20% (Fintech CAGR)",
        "Market Size": "Projected to grow at 20% CAGR by 2030; strong credit demand and digital banking adoption.",
        "Growth Drivers": "Digital adoption, rising lending activity, robust credit demand."
    },
    "Pharma": {
        "CAGR": "~30%",
        "Market Size": "Expected to grow from $372 billion (2023) to $638 billion by 2025.",
        "Growth Drivers": "Medical tourism, telemedicine, AI diagnostics, rising incomes."
    },
    "FMCG": {
        "CAGR": "9.4%",
        "Market Size": "Projected to reach $220 billion by 2025; rural FMCG to hit $100 billion.",
        "Growth Drivers": "Rising disposable incomes, urbanization, online FMCG growth (31% CAGR)."
    },
    "Edtech": {
        "CAGR": "15-18%",
        "Market Size": "Edtech market expected to reach $10 billion by 2025.",
        "Growth Drivers": "Online learning penetration, skill-based courses, personalized learning."
    },
    "Quick Commerce": {
        "CAGR": "25-30%",
        "Market Size": "Projected to grow 10X by 2027, driven by 15-minute deliveries.",
        "Growth Drivers": "Consumer preference for instant groceries, urban logistics expansion."
    },
    "Infrastructure": {
        "CAGR": ">20% revenue CAGR",
        "Market Size": "₹111 lakh crore investment by 2025; growth in roads, railways, ports.",
        "Growth Drivers": "Government capex, NIP projects, PM Gati Shakti initiative."
    },
    "EV & Automobiles": {
        "CAGR": "66.52%",
        "Market Size": "Projected to reach $113.99 billion by 2029.",
        "Growth Drivers": "Government incentives, electric mobility transition."
    },
    "Renewable Energy": {
        "CAGR": "~25-30%",
        "Market Size": "Installed capacity reached 205 GW in 2024; target of 500 GW by 2030.",
        "Growth Drivers": "Solar and wind energy investments, sustainability focus."
    }
}

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

    # Column 1: Industry Selection & Input Sliders
    with col1:
        st.markdown("### 📊 Investability Index Calculator")
        st.write("Select an industry and adjust the sliders to rate each parameter (1-10).")

        # Industry Selection Dropdown
        industry = st.selectbox("Select Industry", list(industry_data.keys()))

        # Display Selected Industry Insights
        st.write(f"**📈 Sector Insights for {industry}:**")
        st.write(f"- **CAGR:** {industry_data[industry]['CAGR']}")
        st.write(f"- **Market Size:** {industry_data[industry]['Market Size']}")
        st.write(f"- **Growth Drivers:** {industry_data[industry]['Growth Drivers']}")

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
        st.success(f"📊 **Manual Investability Index Score: {manual_index:.2f}/10**")

        # Dynamic description based on score
        st.write("### Insights:")
        if manual_index > 7:
            st.write(f"🚀 **The final Investability Index Score is {manual_index:.2f}/10, indicating a strong investment opportunity!**")
        elif 5 <= manual_index <= 7:
            st.write(f"⚠️ **The final Investability Index Score is {manual_index:.2f}/10, indicating a moderate investment opportunity.**")
        else:
            st.write(f"❌ **The final Investability Index Score is {manual_index:.2f}/10, indicating a low investment potential.**")

    # Column 2: Radar Chart
    with col2:
        st.markdown("### 📊 Parameter Ratings Visualization")

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
        st.markdown("### 📌 Detailed Parameter-Based Recommendations")

        def generate_insights(parameter, value):
            if parameter == "Market Growth Potential":
                industry_info = f"{industry} sector is experiencing {industry_data[industry]['CAGR']} growth."
            else:
                industry_info = ""

            if value >= 8:
                return f"✅ **{parameter}:** Strong! Leverage this as a key strength for investors. {industry_info}"
            elif value >= 5:
                return f"⚠️ **{parameter}:** Moderate. Improve this area to strengthen investment appeal. {industry_info}"
            else:
                return f"❌ **{parameter}:** Weak. Requires significant improvement to boost investability. {industry_info}"

        for i, param in enumerate(allocated_credits.keys()):
            st.write(generate_insights(param, input_values[i]))
