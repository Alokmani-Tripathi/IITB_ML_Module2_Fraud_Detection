

# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import joblib

# # # Load model and scaler
# # model = joblib.load('fraud_xgb_model.pkl')
# # scaler = joblib.load('fraud_scaler.pkl')

# # st.title("Banking Fraud Detection System")

# # st.write("Enter transaction details")

# # # Inputs
# # amount = st.number_input("Transaction Amount")

# # transaction_hour = st.slider(
# #     "Transaction Hour",
# #     0,
# #     23
# # )

# # high_amount_flag = st.selectbox(
# #     "High Amount Flag",
# #     [0,1]
# # )

# # night_transaction = st.selectbox(
# #     "Night Transaction",
# #     [0,1]
# # )

# # rapid_transaction = st.selectbox(
# #     "Rapid Transaction",
# #     [0,1]
# # )

# # # Prediction button
# # if st.button("Predict Fraud"):

# #     input_data = np.array([[
# #         amount,
# #         transaction_hour,
# #         high_amount_flag,
# #         night_transaction,
# #         rapid_transaction
# #     ]])

# #     input_scaled = scaler.transform(input_data)

# #     fraud_probability = model.predict_proba(
# #         input_scaled
# #     )[0][1]

# #     st.write(
# #         f"Fraud Probability: {fraud_probability:.4f}"
# #     )

# #     if fraud_probability >= 0.7:

# #         st.error("High Risk Fraud Transaction")

# #     elif fraud_probability >= 0.3:

# #         st.warning("Medium Risk Transaction")

# #     else:

# #         st.success("Low Risk Transaction")



# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px
# import plotly.graph_objects as go

# # =========================
# # PAGE CONFIGURATION
# # =========================

# st.set_page_config(
#     page_title="Banking Fraud Detection System",
#     layout="wide",
#     page_icon="🏦"
# )

# # =========================
# # LOAD MODEL & SCALER
# # =========================

# model = joblib.load('fraud_xgb_model.pkl')
# scaler = joblib.load('fraud_scaler.pkl')

# # =========================
# # APP TITLE
# # =========================

# st.title("🏦 Banking Fraud Detection & Monitoring System")

# st.markdown("""
# This system uses:
# - Machine Learning
# - XGBoost
# - Fraud Risk Scoring
# - Alert Generation
# - Monitoring Logic
# - Fraud Intelligence
# """)

# # =========================
# # SIDEBAR
# # =========================

# st.sidebar.title("⚙️ Fraud Monitoring Panel")

# threshold = st.sidebar.slider(
#     "Fraud Threshold",
#     0.0,
#     1.0,
#     0.30
# )

# st.sidebar.markdown("---")

# st.sidebar.write("### Risk Rules")
# st.sidebar.write("- Low Risk : < 30%")
# st.sidebar.write("- Medium Risk : 30% - 70%")
# st.sidebar.write("- High Risk : > 70%")

# # =========================
# # TABS
# # =========================

# prediction_tab, dashboard_tab, alerts_tab = st.tabs([
#     "🔍 Fraud Prediction",
#     "📊 Fraud Dashboard",
#     "🚨 Fraud Alerts"
# ])

# # =========================
# # FRAUD PREDICTION TAB
# # =========================

# with prediction_tab:

#     st.header("Transaction Monitoring Engine")

#     col1, col2, col3 = st.columns(3)

#     # =========================
#     # INPUT FEATURES
#     # =========================

#     with col1:

#         amount = st.number_input(
#             "Transaction Amount",
#             min_value=0.0,
#             value=5000.0
#         )

#         transaction_hour = st.slider(
#             "Transaction Hour",
#             0,
#             23,
#             12
#         )

#         transaction_day = st.slider(
#             "Transaction Day",
#             1,
#             31,
#             15
#         )

#         transaction_month = st.slider(
#             "Transaction Month",
#             1,
#             12,
#             6
#         )

#     with col2:

#         transaction_weekday = st.slider(
#             "Transaction Weekday",
#             0,
#             6,
#             3
#         )

#         is_weekend = st.selectbox(
#             "Weekend Transaction",
#             [0,1]
#         )

#         night_transaction = st.selectbox(
#             "Night Transaction",
#             [0,1]
#         )

#         high_amount_flag = st.selectbox(
#             "High Amount Flag",
#             [0,1]
#         )

#     with col3:

#         rapid_transaction_flag = st.selectbox(
#             "Rapid Transaction",
#             [0,1]
#         )

#         amount_deviation = st.number_input(
#             "Amount Deviation",
#             value=1000.0
#         )

#         amount_ratio = st.number_input(
#             "Amount Ratio To Avg",
#             value=1.2
#         )

#         rule_based_risk_score = st.slider(
#             "Rule-Based Risk Score",
#             0,
#             100,
#             25
#         )

#     st.markdown("---")

#     # =========================
#     # PREDICTION BUTTON
#     # =========================

#     if st.button("🚨 Predict Fraud"):

#         # =========================
#         # INPUT DATAFRAME
#         # =========================
#         # =========================
# # CREATE FULL FEATURE DATA
# # =========================

#         input_dict = {
        
#             'Amount': amount,
        
#             'Transaction_Hour': transaction_hour,
        
#             'Transaction_Day': transaction_day,
        
#             'Transaction_Month': transaction_month,
        
#             'Transaction_Weekday': transaction_weekday,
        
#             'Is_Weekend': is_weekend,
        
#             'Night_Transaction': night_transaction,
        
#             'High_Amount_Flag': high_amount_flag,
        
#             'Customer_Transaction_Count': 5,
        
#             'Customer_Avg_Amount': amount * 0.8,
        
#             'Customer_Max_Amount': amount * 1.5,
        
#             'Customer_Min_Amount': amount * 0.3,
        
#             'Amount_Deviation': amount_deviation,
        
#             'Amount_Ratio_To_Avg': amount_ratio,
        
#             'Customer_Std_Amount': amount * 0.2,
        
#             'Customer_Zscore_Amount': 1.2,
        
#             'Time_Difference': 30,
        
#             'Rapid_Transaction_Flag': rapid_transaction_flag,
        
#             'Daily_Transaction_Count': 8,
        
#             'Rolling_Avg_Amount': amount * 0.9,
        
#             'Rolling_Max_Amount': amount * 1.3,
        
#             'Rule_Based_Risk_Score': rule_based_risk_score,
        
#             'Transaction_Type_Encoded': 1
        
#         }
        
#         # =========================
#         # CREATE DATAFRAME
#         # =========================
        
#         input_data = pd.DataFrame([input_dict])
        
#         # =========================
#         # ENSURE EXACT FEATURE ORDER
#         # =========================
        
#         expected_columns = [
        
#             'Amount',
#             'Transaction_Hour',
#             'Transaction_Day',
#             'Transaction_Month',
#             'Transaction_Weekday',
#             'Is_Weekend',
#             'Night_Transaction',
#             'High_Amount_Flag',
#             'Customer_Transaction_Count',
#             'Customer_Avg_Amount',
#             'Customer_Max_Amount',
#             'Customer_Min_Amount',
#             'Amount_Deviation',
#             'Amount_Ratio_To_Avg',
#             'Customer_Std_Amount',
#             'Customer_Zscore_Amount',
#             'Time_Difference',
#             'Rapid_Transaction_Flag',
#             'Daily_Transaction_Count',
#             'Rolling_Avg_Amount',
#             'Rolling_Max_Amount',
#             'Rule_Based_Risk_Score',
#             'Transaction_Type_Encoded'
        
#         ]
        
#         input_data = input_data[expected_columns]

#         # =========================
#         # SCALE INPUT
#         # =========================

#         input_scaled = scaler.transform(input_data)

#         # =========================
#         # FRAUD PROBABILITY
#         # =========================

#         fraud_probability = model.predict_proba(
#             input_scaled
#         )[0][1]

#         # =========================
#         # RISK LEVEL
#         # =========================

#         if fraud_probability >= 0.70:
#             risk_level = "High Risk"
#             monitoring_action = "Block Transaction"
#             alert_message = "Immediate Investigation Required"

#         elif fraud_probability >= 0.30:
#             risk_level = "Medium Risk"
#             monitoring_action = "Send OTP Verification"
#             alert_message = "Monitor Transaction"

#         else:
#             risk_level = "Low Risk"
#             monitoring_action = "Allow Transaction"
#             alert_message = "Normal Activity"

#         # =========================
#         # DISPLAY RESULTS
#         # =========================

#         st.markdown("---")

#         st.subheader("Fraud Intelligence Results")

#         metric_col1, metric_col2, metric_col3 = st.columns(3)

#         with metric_col1:
#             st.metric(
#                 "Fraud Probability",
#                 f"{fraud_probability:.2%}"
#             )

#         with metric_col2:
#             st.metric(
#                 "Risk Level",
#                 risk_level
#             )

#         with metric_col3:
#             st.metric(
#                 "Monitoring Action",
#                 monitoring_action
#             )

#         st.progress(float(fraud_probability))

#         # =========================
#         # ALERTS
#         # =========================

#         if risk_level == "High Risk":

#             st.error(
#                 f"🚨 ALERT: {alert_message}"
#             )

#             st.error(
#                 "Recommended Action: Block transaction and escalate to fraud investigation team"
#             )

#         elif risk_level == "Medium Risk":

#             st.warning(
#                 f"⚠️ ALERT: {alert_message}"
#             )

#             st.warning(
#                 "Recommended Action: Trigger OTP verification and monitor activity"
#             )

#         else:

#             st.success(
#                 f"✅ STATUS: {alert_message}"
#             )

#         # =========================
#         # FRAUD GAUGE CHART
#         # =========================

#         gauge_chart = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=fraud_probability * 100,
#             title={'text': "Fraud Risk Score"},
#             gauge={
#                 'axis': {'range': [0,100]},
#                 'steps': [
#                     {'range': [0,30], 'color': "lightgreen"},
#                     {'range': [30,70], 'color': "yellow"},
#                     {'range': [70,100], 'color': "red"}
#                 ]
#             }
#         ))

#         st.plotly_chart(gauge_chart, use_container_width=True)

# # =========================
# # DASHBOARD TAB
# # =========================

# with dashboard_tab:

#     st.header("Fraud Analytics Dashboard")

#     # =========================
#     # SAMPLE DASHBOARD DATA
#     # =========================

#     np.random.seed(42)

#     dashboard_data = pd.DataFrame({
#         'Risk_Level': np.random.choice(
#             ['Low Risk', 'Medium Risk', 'High Risk'],
#             200,
#             p=[0.7,0.2,0.1]
#         ),
#         'Fraud_Probability': np.random.uniform(0,1,200),
#         'Transaction_Amount': np.random.randint(100,50000,200)
#     })

#     # =========================
#     # KPI CARDS
#     # =========================

#     kpi1, kpi2, kpi3, kpi4 = st.columns(4)

#     with kpi1:
#         st.metric(
#             "Total Transactions",
#             len(dashboard_data)
#         )

#     with kpi2:
#         st.metric(
#             "High Risk Transactions",
#             (dashboard_data['Risk_Level'] == 'High Risk').sum()
#         )

#     with kpi3:
#         st.metric(
#             "Average Fraud Probability",
#             f"{dashboard_data['Fraud_Probability'].mean():.2%}"
#         )

#     with kpi4:
#         st.metric(
#             "Max Fraud Probability",
#             f"{dashboard_data['Fraud_Probability'].max():.2%}"
#         )

#     st.markdown("---")

#     # =========================
#     # CHARTS
#     # =========================

#     chart_col1, chart_col2 = st.columns(2)

#     # =========================
#     # RISK DISTRIBUTION PIE CHART
#     # =========================

#     with chart_col1:

#         risk_pie = px.pie(
#             dashboard_data,
#             names='Risk_Level',
#             title='Fraud Risk Distribution'
#         )

#         st.plotly_chart(
#             risk_pie,
#             use_container_width=True
#         )

#     # =========================
#     # FRAUD PROBABILITY HISTOGRAM
#     # =========================

#     with chart_col2:

#         fraud_hist = px.histogram(
#             dashboard_data,
#             x='Fraud_Probability',
#             title='Fraud Probability Distribution'
#         )

#         st.plotly_chart(
#             fraud_hist,
#             use_container_width=True
#         )

#     # =========================
#     # HIGH RISK TABLE
#     # =========================

#     st.subheader("High Risk Investigation Queue")

#     high_risk_data = dashboard_data[
#         dashboard_data['Risk_Level'] == 'High Risk'
#     ]

#     st.dataframe(
#         high_risk_data.head(20),
#         use_container_width=True
#     )

# # =========================
# # ALERTS TAB
# # =========================

# with alerts_tab:

#     st.header("Real-Time Fraud Alert Center")

#     alerts_df = pd.DataFrame({
#         'Transaction_ID': np.arange(1001,1011),
#         'Fraud_Probability': np.random.uniform(0.5,1.0,10),
#         'Risk_Level': np.random.choice(
#             ['Medium Risk', 'High Risk'],
#             10
#         ),
#         'Monitoring_Action': np.random.choice(
#             [
#                 'Block Transaction',
#                 'OTP Verification',
#                 'Manual Review'
#             ],
#             10
#         )
#     })

#     for index, row in alerts_df.iterrows():

#         if row['Risk_Level'] == 'High Risk':

#             st.error(
#                 f"🚨 Transaction {row['Transaction_ID']} | Fraud Probability: {row['Fraud_Probability']:.2%} | Action: {row['Monitoring_Action']}"
#             )

#         else:

#             st.warning(
#                 f"⚠️ Transaction {row['Transaction_ID']} | Fraud Probability: {row['Fraud_Probability']:.2%} | Action: {row['Monitoring_Action']}"
#             )

# # =========================
# # FOOTER
# # =========================

# st.markdown("---")

# st.caption(
#     "Banking Fraud Detection System | Machine Learning + Fraud Intelligence + Monitoring Dashboard"
# )

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Banking Fraud Detection System",
    layout="wide",
    page_icon="🏦"
)

# =========================
# LOAD MODEL & SCALER
# =========================

model = joblib.load('fraud_xgb_model.pkl')
scaler = joblib.load('fraud_scaler.pkl')

# =========================
# APP TITLE
# =========================

st.title("🏦 Banking Fraud Detection & Monitoring System")

st.markdown("""
This system uses:
- Machine Learning
- XGBoost
- Fraud Risk Scoring
- Alert Generation
- Monitoring Logic
- Fraud Intelligence
""")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("⚙️ Fraud Monitoring Panel")

threshold = st.sidebar.slider(
    "Fraud Threshold",
    0.0,
    1.0,
    0.10
)

st.sidebar.markdown("---")

st.sidebar.write("### Risk Rules")
st.sidebar.write("- Low Risk : 0% - 10%")
st.sidebar.write("- Medium Risk : 10% - 20%")
st.sidebar.write("- High Risk : > 20%")

# =========================
# TABS
# =========================

prediction_tab, dashboard_tab, alerts_tab = st.tabs([
    "🔍 Fraud Prediction",
    "📊 Fraud Dashboard",
    "🚨 Fraud Alerts"
])

# =========================
# FRAUD PREDICTION TAB
# =========================

with prediction_tab:

    st.header("Transaction Monitoring Engine")

    col1, col2, col3 = st.columns(3)

    # =========================
    # INPUT FEATURES
    # =========================

    with col1:

        amount = st.number_input(
            "Transaction Amount",
            min_value=0.0,
            value=5000.0
        )

        transaction_hour = st.slider(
            "Transaction Hour",
            0,
            23,
            12
        )

        transaction_day = st.slider(
            "Transaction Day",
            1,
            31,
            15
        )

        transaction_month = st.slider(
            "Transaction Month",
            1,
            12,
            6
        )

    with col2:

        transaction_weekday = st.slider(
            "Transaction Weekday",
            0,
            6,
            3
        )

        is_weekend = st.selectbox(
            "Weekend Transaction",
            [0,1]
        )

        night_transaction = st.selectbox(
            "Night Transaction",
            [0,1]
        )

        high_amount_flag = st.selectbox(
            "High Amount Flag",
            [0,1]
        )

    with col3:

        rapid_transaction_flag = st.selectbox(
            "Rapid Transaction",
            [0,1]
        )

        amount_deviation = st.number_input(
            "Amount Deviation",
            value=1000.0
        )

        amount_ratio = st.number_input(
            "Amount Ratio To Avg",
            value=1.2
        )

        rule_based_risk_score = st.slider(
            "Rule-Based Risk Score",
            0,
            100,
            25
        )

    st.markdown("---")

    # =========================
    # PREDICTION BUTTON
    # =========================

    if st.button("🚨 Predict Fraud"):

        # =========================
        # CREATE FULL FEATURE DATA
        # =========================

        input_dict = {

            'Amount': amount,

            'Transaction_Hour': transaction_hour,

            'Transaction_Day': transaction_day,

            'Transaction_Month': transaction_month,

            'Transaction_Weekday': transaction_weekday,

            'Is_Weekend': is_weekend,

            'Night_Transaction': night_transaction,

            'High_Amount_Flag': high_amount_flag,

            'Customer_Transaction_Count': 5,

            'Customer_Avg_Amount': amount * 0.8,

            'Customer_Max_Amount': amount * 1.5,

            'Customer_Min_Amount': amount * 0.3,

            'Amount_Deviation': amount_deviation,

            'Amount_Ratio_To_Avg': amount_ratio,

            'Customer_Std_Amount': amount * 0.2,

            'Customer_Zscore_Amount': 1.2,

            'Time_Difference': 30,

            'Rapid_Transaction_Flag': rapid_transaction_flag,

            'Daily_Transaction_Count': 8,

            'Rolling_Avg_Amount': amount * 0.9,

            'Rolling_Max_Amount': amount * 1.3,

            'Rule_Based_Risk_Score': rule_based_risk_score,

            'Transaction_Type_Encoded': 1

        }

        # =========================
        # CREATE DATAFRAME
        # =========================

        input_data = pd.DataFrame([input_dict])

        # =========================
        # ENSURE EXACT FEATURE ORDER
        # =========================

        expected_columns = [

            'Amount',
            'Transaction_Hour',
            'Transaction_Day',
            'Transaction_Month',
            'Transaction_Weekday',
            'Is_Weekend',
            'Night_Transaction',
            'High_Amount_Flag',
            'Customer_Transaction_Count',
            'Customer_Avg_Amount',
            'Customer_Max_Amount',
            'Customer_Min_Amount',
            'Amount_Deviation',
            'Amount_Ratio_To_Avg',
            'Customer_Std_Amount',
            'Customer_Zscore_Amount',
            'Time_Difference',
            'Rapid_Transaction_Flag',
            'Daily_Transaction_Count',
            'Rolling_Avg_Amount',
            'Rolling_Max_Amount',
            'Rule_Based_Risk_Score',
            'Transaction_Type_Encoded'

        ]

        input_data = input_data[expected_columns]

        # =========================
        # SCALE INPUT
        # =========================

        input_scaled = scaler.transform(input_data)

        # =========================
        # FRAUD PROBABILITY
        # =========================

        fraud_probability = model.predict_proba(
            input_scaled
        )[0][1]

        # =========================
        # RISK LEVEL
        # =========================

        if fraud_probability > 0.20:

            risk_level = "High Risk"
            monitoring_action = "Block Transaction"
            alert_message = "Immediate Investigation Required"

        elif fraud_probability >= 0.10:

            risk_level = "Medium Risk"
            monitoring_action = "Send OTP Verification"
            alert_message = "Monitor Transaction"

        else:

            risk_level = "Low Risk"
            monitoring_action = "Allow Transaction"
            alert_message = "Normal Activity"

        # =========================
        # DISPLAY RESULTS
        # =========================

        st.markdown("---")

        st.subheader("Fraud Intelligence Results")

        metric_col1, metric_col2, metric_col3 = st.columns(3)

        with metric_col1:
            st.metric(
                "Fraud Probability",
                f"{fraud_probability:.2%}"
            )

        with metric_col2:
            st.metric(
                "Risk Level",
                risk_level
            )

        with metric_col3:
            st.metric(
                "Monitoring Action",
                monitoring_action
            )

        st.progress(float(fraud_probability))

        # =========================
        # ALERTS
        # =========================

        if risk_level == "High Risk":

            st.error(
                f"🚨 ALERT: {alert_message}"
            )

            st.error(
                "Recommended Action: Block transaction and escalate to fraud investigation team"
            )

        elif risk_level == "Medium Risk":

            st.warning(
                f"⚠️ ALERT: {alert_message}"
            )

            st.warning(
                "Recommended Action: Trigger OTP verification and monitor activity"
            )

        else:

            st.success(
                f"✅ STATUS: {alert_message}"
            )

        # =========================
        # FRAUD GAUGE CHART
        # =========================

        gauge_chart = go.Figure(go.Indicator(
            mode="gauge+number",
            value=fraud_probability * 100,
            title={'text': "Fraud Risk Score"},
            gauge={
                'axis': {'range': [0,100]},
                'steps': [
                    {'range': [0,10], 'color': "lightgreen"},
                    {'range': [10,20], 'color': "yellow"},
                    {'range': [20,100], 'color': "red"}
                ]
            }
        ))

        st.plotly_chart(gauge_chart, use_container_width=True)

# =========================
# DASHBOARD TAB
# =========================

with dashboard_tab:

    st.header("Fraud Analytics Dashboard")

    np.random.seed(42)

    dashboard_data = pd.DataFrame({
        'Risk_Level': np.random.choice(
            ['Low Risk', 'Medium Risk', 'High Risk'],
            200,
            p=[0.5,0.2,0.3]
        ),
        'Fraud_Probability': np.random.uniform(0,1,200),
        'Transaction_Amount': np.random.randint(100,50000,200)
    })

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            "Total Transactions",
            len(dashboard_data)
        )

    with kpi2:
        st.metric(
            "High Risk Transactions",
            (dashboard_data['Risk_Level'] == 'High Risk').sum()
        )

    with kpi3:
        st.metric(
            "Average Fraud Probability",
            f"{dashboard_data['Fraud_Probability'].mean():.2%}"
        )

    with kpi4:
        st.metric(
            "Max Fraud Probability",
            f"{dashboard_data['Fraud_Probability'].max():.2%}"
        )

    st.markdown("---")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:

        risk_pie = px.pie(
            dashboard_data,
            names='Risk_Level',
            title='Fraud Risk Distribution'
        )

        st.plotly_chart(
            risk_pie,
            use_container_width=True
        )

    with chart_col2:

        fraud_hist = px.histogram(
            dashboard_data,
            x='Fraud_Probability',
            title='Fraud Probability Distribution'
        )

        st.plotly_chart(
            fraud_hist,
            use_container_width=True
        )

    st.subheader("High Risk Investigation Queue")

    high_risk_data = dashboard_data[
        dashboard_data['Risk_Level'] == 'High Risk'
    ]

    st.dataframe(
        high_risk_data.head(20),
        use_container_width=True
    )

# =========================
# ALERTS TAB
# =========================

with alerts_tab:

    st.header("Real-Time Fraud Alert Center")

    alerts_df = pd.DataFrame({
        'Transaction_ID': np.arange(1001,1011),
        'Fraud_Probability': np.random.uniform(0.1,1.0,10),
        'Risk_Level': np.random.choice(
            ['Medium Risk', 'High Risk'],
            10
        ),
        'Monitoring_Action': np.random.choice(
            [
                'Block Transaction',
                'OTP Verification',
                'Manual Review'
            ],
            10
        )
    })

    for index, row in alerts_df.iterrows():

        if row['Risk_Level'] == 'High Risk':

            st.error(
                f"🚨 Transaction {row['Transaction_ID']} | Fraud Probability: {row['Fraud_Probability']:.2%} | Action: {row['Monitoring_Action']}"
            )

        else:

            st.warning(
                f"⚠️ Transaction {row['Transaction_ID']} | Fraud Probability: {row['Fraud_Probability']:.2%} | Action: {row['Monitoring_Action']}"
            )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Banking Fraud Detection System | Machine Learning + Fraud Intelligence + Monitoring Dashboard"
)

