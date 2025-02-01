import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set Streamlit Layout
st.set_page_config(layout="wide")

# Currency & Fund Selection
st.sidebar.markdown("💰 **Investment Settings**")
currency = st.sidebar.radio("Select Currency", ["INR ₹", "USD $"])
funds = st.sidebar.selectbox("Total Investment Fund", ["₹5M", "₹10M", "$1M", "$5M"])
fund_value = int(funds.replace("₹", "").replace("$", "").replace("M", "000000"))  # Convert to numeric

# Industry Data Expansion (20+ Industries)
industry_data = {
    "Fintech": {"CAGR": "15-20%", "Market Growth Potential": "🚀 Strong digital adoption", "Profitability": "💰 High"},
    "Pharma": {"CAGR": "30%", "Market Growth Potential": "📈 Growing AI diagnostics", "Profitability": "🔬 R&D Heavy"},
    "FMCG": {"CAGR": "9.4%", "Market Growth Potential": "🛍️ Online FMCG Boom", "Profitability": "💸 Consistent"},
    "Edtech": {"CAGR": "15-18%", "Market Growth Potential": "📚 Digital Education Growth", "Profitability": "⚖️ Moderate"},
    "Quick Commerce": {"CAGR": "25-30%", "Market Growth Potential": "🚴 Fast Deliveries Demand", "Profitability": "📊 Growing"},
    "EV & Automobiles": {"CAGR": "66.52%", "Market Growth Potential": "🔋 Electric Mobility Transition", "Profitability": "🔧 Tech Intensive"},
    "Renewable Energy": {"CAGR": "25-30%", "Market Growth Potential": "🌱 Sustainability Investments", "Profitability": "💵 Capital Intensive"},
    # Add more industries...
}

# Tabs for UI
tab1, tab2, tab3 = st.tabs(["📊 Index Calculator", "💸 Investment Allocation", "📈 Industry Insights"])

# 📊 **TAB 1: Investability Index Calculator**
with tab1:
    st.markdown("### 📊 Investability Index Calculator")
    
    # Industry Selection
    industry = st.selectbox("Select Industry", list(industry_data.keys()))

    # Parameter Sliders
    market_growth = st.slider("Market Growth Potential", 1, 10, 5)
    profitability = st.slider("Profitability", 1, 10, 5)
    competitive_advantage = st.slider("Competitive Advantage", 1, 10, 5)
    management_quality = st.slider("Management Quality", 1, 10, 5)
    innovation_rd = st.slider("Innovation & R&D", 1, 10, 5)
    regulatory_env = st.slider("Regulatory Environment", 1, 10, 5)
    financial_stability = st.slider("Financial Stability", 1, 10, 5)
    sustainability_esg = st.slider("Sustainability & ESG", 1, 10, 5)

    # Compute Investability Index
    input_values = [market_growth, profitability, competitive_advantage, management_quality, innovation_rd, regulatory_env, financial_stability, sustainability_esg]
    allocated_credits = [12, 10, 10, 8, 8, 6, 4, 2]  # Fixed credit allocation
    investability_score = sum(np.array(input_values) * np.array(allocated_credits)) / 60

    st.success(f"📊 **Investability Index Score: {investability_score:.2f}/10**")

# 💸 **TAB 2: Investment Allocation**
with tab2:
    st.markdown("### 💸 Investment Allocation")

    # Example: Select 3 from 5 hypothetical companies
    company_options = ["Company A", "Company B", "Company C", "Company D", "Company E"]
    selected_companies = st.multiselect("Select Top 3 Companies", company_options, default=company_options[:3])

    if len(selected_companies) == 3:
        # Example Scores (Randomized)
        scores = {company: np.random.uniform(5, 10) for company in selected_companies}
        total_score = sum(scores.values())

        # Allocate Investment
        investments = {company: (score / total_score) * fund_value for company, score in scores.items()}

        # Display Allocation
        st.write("### 🏦 Investment Distribution")
        for company, investment in investments.items():
            st.write(f"💰 **{company}:** {currency} {investment:,.2f}")

# 📈 **TAB 3: Industry Insights**
with tab3:
    st.markdown("### 📈 Industry Insights")

    # Auto-populate data based on selection
    if industry in industry_data:
        st.markdown(f"🚀 **Sector Overview: {industry}**")
        st.write(f"📈 **CAGR:** {industry_data[industry]['CAGR']}")
        st.write(f"🏆 **Market Growth Potential:** {industry_data[industry]['Market Growth Potential']}")
        st.write(f"💰 **Profitability:** {industry_data[industry]['Profitability']}")

