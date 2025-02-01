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
        "CAGR": "15-20% (2023-2028)", 
        "Market Growth Potential": "🚀 Strong digital adoption", 
        "Profitability": "💰 High",
        "Description": "Fintech is revolutionizing banking, payments, and lending with AI & blockchain innovations. UPI payments, digital lending, and neobanking are driving financial inclusion.",
        "Examples": "Startups: Razorpay, CRED, PhonePe | Giants: PayPal, Visa"
    },
    "Pharma": {
        "CAGR": "30% (2023-2027)", 
        "Market Growth Potential": "📈 Growing AI diagnostics", 
        "Profitability": "🔬 R&D Heavy",
        "Description": "Pharma is booming with AI-driven drug discovery, precision medicine, and biotech advances. Generic drug manufacturing and contract research are key growth drivers.",
        "Examples": "Startups: Tempus, Innoplexus | Giants: Sun Pharma, Dr. Reddy's"
    },
    "EV & Automobiles": {
        "CAGR": "66.52% (2022-2027)", 
        "Market Growth Potential": "🔋 Electric Mobility", 
        "Profitability": "🔧 Tech Intensive",
        "Description": "EVs are reshaping transportation with battery innovations & government incentives. Local manufacturing, charging infrastructure, and battery tech development are driving growth.",
        "Examples": "Startups: Ather Energy, Ola Electric | Giants: Tata Motors, Mahindra Electric"
    },
    "EdTech": {
        "CAGR": "19.5% (2023-2028)",
        "Market Growth Potential": "📚 Digital Learning Revolution",
        "Profitability": "💡 High Customer Acquisition Cost",
        "Description": "EdTech platforms are transforming education through personalized learning, gamification, and hybrid models. Test prep, upskilling, and K-12 supplementary education are major segments.",
        "Examples": "Startups: BYJU'S, Unacademy | Giants: Coursera, Duolingo"
    },
    "Renewable Energy": {
        "CAGR": "35.3% (2023-2028)",
        "Market Growth Potential": "☀️ Clean Energy Transition",
        "Profitability": "🌱 Government Incentives",
        "Description": "Solar, wind, and hydrogen energy solutions are driving sustainable development. Policy support, declining costs, and corporate commitments fuel sector growth.",
        "Examples": "Startups: ReNew Power, Fourth Partner | Giants: Adani Green, Tata Power"
    },
    "AgriTech": {
        "CAGR": "25% (2023-2028)",
        "Market Growth Potential": "🌾 Farm Digitization",
        "Profitability": "🚜 Seasonal Variations",
        "Description": "AgriTech is modernizing farming through IoT sensors, precision agriculture, and supply chain optimization. Digital marketplaces and farm automation drive efficiency.",
        "Examples": "Startups: DeHaat, Ninjacart | Giants: Bayer, Mahindra Agri"
    },
    "SpaceTech": {
        "CAGR": "41.2% (2023-2028)",
        "Market Growth Potential": "🛰️ Private Space Economy",
        "Profitability": "🚀 Capital Intensive",
        "Description": "Private space exploration, satellite communications, and space tourism are emerging. Small satellite launches and space-based internet drive innovation.",
        "Examples": "Startups: Skyroot Aerospace, Pixxel | Giants: ISRO, SpaceX"
    },
    "HealthTech": {
        "CAGR": "27.9% (2023-2028)",
        "Market Growth Potential": "⚕️ Digital Healthcare",
        "Profitability": "📱 Platform Economics",
        "Description": "Telemedicine, AI diagnostics, and digital health records are transforming healthcare delivery. Remote monitoring and mental health tech show strong growth.",
        "Examples": "Startups: Practo, 1mg | Giants: Apollo Hospitals, Philips"
    },
    "Cybersecurity": {
        "CAGR": "13.8% (2023-2028)",
        "Market Growth Potential": "🔒 Digital Protection",
        "Profitability": "💪 High Margins",
        "Description": "Rising cyber threats drive demand for AI-powered security, cloud protection, and zero-trust architecture. Data privacy regulations boost adoption.",
        "Examples": "Startups: Lucideus, CloudSEK | Giants: Tata Security, Quick Heal"
    },
    "Gaming": {
        "CAGR": "28.6% (2023-2028)",
        "Market Growth Potential": "🎮 Mobile Gaming Boom",
        "Profitability": "🎲 Hit-Driven",
        "Description": "Mobile gaming, esports, and AR/VR experiences drive growth. Real-money gaming and social gaming platforms show strong user engagement.",
        "Examples": "Startups: Dream11, MPL | Giants: Nazara, Jetsynthesys"
    },
    "D2C Brands": {
        "CAGR": "24.3% (2023-2028)",
        "Market Growth Potential": "🛍️ Digital-First Retail",
        "Profitability": "📦 Brand Dependent",
        "Description": "Direct-to-consumer brands leverage social commerce and personalization. Beauty, fashion, and food segments show strong growth potential.",
        "Examples": "Startups: Mamaearth, boAt | Giants: Lenskart, Nykaa"
    },
    "Cloud Computing": {
        "CAGR": "17.9% (2023-2028)",
        "Market Growth Potential": "☁️ Digital Infrastructure",
        "Profitability": "💻 Scale Advantages",
        "Description": "Cloud services, edge computing, and serverless architecture drive digital transformation. AI/ML workloads and data analytics fuel demand.",
        "Examples": "Startups: Druva, Postman | Giants: TCS, Infosys"
    },
    "Logistics": {
        "CAGR": "10.7% (2023-2028)",
        "Market Growth Potential": "📦 Supply Chain Tech",
        "Profitability": "🚛 Asset Heavy",
        "Description": "E-commerce growth drives logistics innovation through AI route optimization, warehouse automation, and last-mile delivery solutions.",
        "Examples": "Startups: Delhivery, BlackBuck | Giants: Blue Dart, Mahindra Logistics"
    },
    "WaterTech": {
        "CAGR": "8.8% (2023-2028)",
        "Market Growth Potential": "💧 Water Security",
        "Profitability": "🌊 Infrastructure Dependent",
        "Description": "Water treatment, conservation tech, and smart metering address scarcity. Wastewater management and desalination show growing adoption.",
        "Examples": "Startups: Vasitum, WEGoT | Giants: VA Tech WABAG, Ion Exchange"
    },
    "FoodTech": {
        "CAGR": "22.4% (2023-2028)",
        "Market Growth Potential": "🍽️ Digital Food Economy",
        "Profitability": "🍳 Operations Intensive",
        "Description": "Cloud kitchens, food delivery platforms, and alternative protein solutions transform food services. Tech-enabled supply chain and restaurant tech show promise.",
        "Examples": "Startups: Swiggy, Zomato | Giants: ITC Foods, Jubilant"
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

        # Allocate Investment (Before Currency Conversion)
        total_score = sum(score for _, score in st.session_state.selected_companies.values())
        investments = {company: (score / total_score) * fund_value for company, (_, score) in st.session_state.selected_companies.items()}

        # ✅ Apply Currency Conversion AFTER Allocation
        if currency == "USD $":
            investments = {company: amount / 80 for company, amount in investments.items()}  # Convert to USD

        # Display Corrected Allocation
        st.write("### 🏦 Investment Distribution (Corrected)")
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
