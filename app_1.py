import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set Streamlit Layout
st.set_page_config(layout="wide")

# Sidebar for Currency & Fund Selection
st.sidebar.markdown("💰 **Investment Settings**")

# Currency Selection
currency = st.sidebar.radio("Select Currency", ["INR ₹", "USD $"])

# Predefined & Custom Fund Selection
fund_options = ["1M", "5M", "10M", "50M", "Custom"]
selected_fund = st.sidebar.selectbox("Total Investment Fund", fund_options)

# Handle Custom Fund Entry
if selected_fund == "Custom":
    fund_value = st.sidebar.number_input("Enter Custom Fund Amount", min_value=1_000_000, step=500_000, value=5_000_000)
else:
    fund_value = int(selected_fund.replace("M", "")) * 1_000_000

# Handle Currency Conversion
if currency == "USD $":
    fund_value /= 80  # Assuming 1 USD = 80 INR for conversion

# Expanded Industry Data (20+ Industries)
industry_data = {
    "Fintech": {"CAGR": "15-20%", "Market Growth Potential": "🚀 Strong digital adoption", "Profitability": "💰 High"},
    "Pharma": {"CAGR": "30%", "Market Growth Potential": "📈 Growing AI diagnostics", "Profitability": "🔬 R&D Heavy"},
    "FMCG": {"CAGR": "9.4%", "Market Growth Potential": "🛍️ Online FMCG Boom", "Profitability": "💸 Consistent"},
    "Edtech": {"CAGR": "15-18%", "Market Growth Potential": "📚 Digital Learning", "Profitability": "⚖️ Moderate"},
    "Quick Commerce": {"CAGR": "25-30%", "Market Growth Potential": "🚴 Fast Deliveries", "Profitability": "📊 Growing"},
    "EV & Automobiles": {"CAGR": "66.52%", "Market Growth Potential": "🔋 Electric Mobility", "Profitability": "🔧 Tech Intensive"},
    "Renewable Energy": {"CAGR": "25-30%", "Market Growth Potential": "🌱 Sustainability Focus", "Profitability": "💵 Capital Heavy"},
    "Healthcare AI": {"CAGR": "20%", "Market Growth Potential": "🤖 AI in Diagnostics", "Profitability": "📊 Data Driven"},
    "Cloud Computing": {"CAGR": "17%", "Market Growth Potential": "☁️ Rising SaaS Adoption", "Profitability": "💡 High Margins"},
    "Blockchain": {"CAGR": "45%", "Market Growth Potential": "🔗 DeFi & Crypto Growth", "Profitability": "⚖️ Risky but High"},
    "Space Tech": {"CAGR": "40%", "Market Growth Potential": "🚀 Private Space Missions", "Profitability": "🌍 High Entry Costs"},
    "Cybersecurity": {"CAGR": "22%", "Market Growth Potential": "🛡️ Rising Data Breaches", "Profitability": "🔒 Stable"},
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
    allocated_credits = [12, 10, 10, 8, 8, 6, 4, 2]
    investability_score = sum(np.array(input_values) * np.array(allocated_credits)) / 60

    # Show Result
    st.success(f"📊 **Investability Index Score: {investability_score:.2f}/10**")

    # One-Liner Insight
    if investability_score > 7.5:
        st.write("🚀 **Strong Investment Opportunity!**")
    elif investability_score > 5:
        st.write("⚠️ **Good, but some areas need improvement.**")
    else:
        st.write("❌ **Not recommended for investment.**")

# 💸 **TAB 2: Investment Allocation**
with tab2:
    st.markdown("### 💸 Investment Allocation")

    # Select Top 3 Companies
    company_options = ["Company A", "Company B", "Company C", "Company D", "Company E"]
    selected_companies = st.multiselect("Select Top 3 Companies", company_options, default=company_options[:3])

    if len(selected_companies) == 3:
        # Example Scores (Based on User Index Score)
        scores = {company: investability_score + np.random.uniform(-1, 1) for company in selected_companies}
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
