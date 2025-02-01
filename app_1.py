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

# Expanded Industry Data (with Real Startups & Giants)
industry_data = {
    "Fintech": {
        "CAGR": "15-20%", 
        "Market Growth Potential": "🚀 Strong digital adoption", 
        "Profitability": "💰 High",
        "Description": "Fintech is revolutionizing banking, payments, and lending with AI & blockchain innovations.",
        "Examples": "Startups: Razorpay, Stripe | Giants: PayPal, Visa"
    },
    "Pharma": {
        "CAGR": "30%", 
        "Market Growth Potential": "📈 Growing AI diagnostics", 
        "Profitability": "🔬 R&D Heavy",
        "Description": "Pharma is booming with AI-driven drug discovery, precision medicine, and biotech advances.",
        "Examples": "Startups: Tempus, PathAI | Giants: Pfizer, Johnson & Johnson"
    },
    "EV & Automobiles": {
        "CAGR": "66.52%", 
        "Market Growth Potential": "🔋 Electric Mobility", 
        "Profitability": "🔧 Tech Intensive",
        "Description": "EVs are reshaping transportation with battery innovations & government incentives.",
        "Examples": "Startups: Rivian, Ola Electric | Giants: Tesla, Toyota"
    },
}

# Tabs for UI
tab1, tab2, tab3 = st.tabs(["📊 Index Calculator", "💸 Investment Allocation", "📈 Industry Insights"])

# Global Storage for Selected Companies
if "selected_companies" not in st.session_state:
    st.session_state.selected_companies = {}

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

    # Company Name Input
    company_name = st.text_input("Enter Company Name:", value="")

    # ➕ Add Company Button
    if st.button("➕ Add Company for Investment"):
        if company_name:
            st.session_state.selected_companies[company_name] = (industry, investability_score)
            st.success(f"✅ **{company_name} added to Investment Allocation!**")

# 💸 **TAB 2: Investment Allocation**
with tab2:
    st.markdown("### 💸 Investment Allocation")

    if not st.session_state.selected_companies:
        st.warning("⚠️ No companies added yet. Go to the **Index Calculator** and add companies.")
    else:
        # Display Added Companies
        st.write("🏦 **Selected Companies for Investment:**")
        for company, (industry, score) in st.session_state.selected_companies.items():
            st.write(f"📊 **{company} ({industry})** - Investability Score: {score:.2f}")

        # Allocate Investment
        total_score = sum(score for _, score in st.session_state.selected_companies.values())
        investments = {company: (score / total_score) * fund_value for company, (_, score) in st.session_state.selected_companies.items()}

        # Display Allocation
        st.write("### 🏦 Investment Distribution")
        for company, investment in investments.items():
            st.write(f"💰 **{company}:** {currency} {investment:,.2f}")

# 📈 **TAB 3: Industry Insights**
with tab3:
    st.markdown("### 📈 Industry Insights")

    if not st.session_state.selected_companies:
        st.warning("⚠️ No companies added yet. Go to the **Index Calculator** and add companies.")
    else:
        industries_displayed = set()

        for company, (industry, score) in st.session_state.selected_companies.items():
            if industry not in industries_displayed:
                industries_displayed.add(industry)

                # 🎨 Highlighted Sector Overview for Better Visibility
                st.markdown(f""" 
                <div style="background-color:#f4f4f4; padding:10px; border-radius:5px; font-weight:bold;">
                🚀 <span style="color:#e63946;">Sector Overview: {industry}</span>
                </div>
                """, unsafe_allow_html=True)

                # Display Industry Info
                st.write(f"📈 **CAGR:** {industry_data[industry]['CAGR']}")
                st.write(f"🏆 **Market Growth Potential:** {industry_data[industry]['Market Growth Potential']}")
                st.write(f"💰 **Profitability:** {industry_data[industry]['Profitability']}")
                st.write(f"📜 **Industry Description:** {industry_data[industry]['Description']}")
                st.write(f"🏢 **Rising Startups & Giants:** {industry_data[industry]['Examples']}")
