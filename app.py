import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Set page layout to wide mode
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

# Load CSV data
uploaded_file = "your_dataset.csv"  # Replace with your CSV file
df = pd.read_csv(uploaded_file)

# Train Machine Learning Model
def train_ml_model(dataframe):
    features = list(allocated_credits.keys())
    target = "Investability Index"

    # Split data
    X = dataframe[features]
    y = dataframe[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest Regressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    return model, mse, pd.DataFrame({"Feature": features, "Importance": model.feature_importances_}).sort_values(by="Importance", ascending=False)

# Train the model and get feature importance
model, mse, feature_importance = train_ml_model(df)

# Main container
with st.container():
    # Layout: Three equal columns
    col1, col2, col3 = st.columns([1, 1, 1])

    # Column 1: Sliders
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

        # Compute Investability Index
        input_values = [
            market_growth, profitability, competitive_advantage, management_quality,
            innovation_rd, regulatory_env, financial_stability, sustainability_esg
        ]
        manual_index = calculate_manual_index(input_values, allocated_credits)

        # Display manual calculation
        st.success(f"**📊 Manual Investability Index Score:** {manual_index:.2f}")

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

        def generate_insights(parameter, value):
            if value >= 8:
                return f"✅ **{parameter}:** Strong! Leverage this as a key strength for investors."
            elif value >= 5:
                return f"⚠️ **{parameter}:** Moderate. Improve this area to strengthen investment appeal."
            else:
                return f"❌ **{parameter}:** Weak. Requires significant improvement to boost investability."

        # Display recommendations
        for i, param in enumerate(allocated_credits.keys()):
            st.write(generate_insights(param, input_values[i]))

# Scrollable ML Insights Section
with st.expander("🔍 Machine Learning Insights"):
    st.subheader("📊 Feature Importance")
    st.write("The following shows which parameters most influence the Investability Index, as learned by the machine learning model:")
    st.dataframe(feature_importance)

    st.subheader("📈 Model Evaluation")
    st.write(f"Mean Squared Error of the Model: {mse:.2f}")
