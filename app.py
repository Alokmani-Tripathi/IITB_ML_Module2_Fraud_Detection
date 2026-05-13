



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
#     0.15
# )

# st.sidebar.markdown("---")

# st.sidebar.write("### Risk Rules")
# st.sidebar.write("- Low Risk : 0% - 15%")
# st.sidebar.write("- Medium Risk : 15% - 30%")
# st.sidebar.write("- High Risk : > 30%")

# st.sidebar.markdown("---")

# st.sidebar.write("### Threshold Logic")
# st.sidebar.write(
#     "If Fraud Probability ≥ Threshold → Alert Triggered"
# )

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
#         # CREATE FULL FEATURE DATA
#         # =========================

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
#         # RISK CLASSIFICATION
#         # =========================

#         if fraud_probability > 0.30:

#             risk_level = "High Risk"
#             monitoring_action = "Block Transaction"

#         elif fraud_probability >= 0.15:

#             risk_level = "Medium Risk"
#             monitoring_action = "OTP Verification"

#         else:

#             risk_level = "Low Risk"
#             monitoring_action = "Allow Transaction"

#         # =========================
#         # ALERT THRESHOLD LOGIC
#         # =========================

#         if fraud_probability >= threshold:

#             alert_status = "🚨 ALERT TRIGGERED"

#         else:

#             alert_status = "✅ No Alert"

#         # =========================
#         # ALERT MESSAGE
#         # =========================

#         if risk_level == "High Risk":

#             alert_message = "Immediate Investigation Required"

#         elif risk_level == "Medium Risk":

#             alert_message = "Monitor Transaction"

#         else:

#             alert_message = "Normal Activity"

#         # =========================
#         # DISPLAY RESULTS
#         # =========================

#         st.markdown("---")

#         st.subheader("Fraud Intelligence Results")

#         metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

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

#         with metric_col4:
#             st.metric(
#                 "Alert Status",
#                 alert_status
#             )

#         st.progress(float(fraud_probability))

#         # =========================
#         # ALERT DISPLAY
#         # =========================

#         if fraud_probability >= threshold:

#             if risk_level == "High Risk":

#                 st.error(
#                     f"🚨 ALERT TRIGGERED | {alert_message}"
#                 )

#                 st.error(
#                     "Recommended Action: Block transaction and escalate to fraud investigation team"
#                 )

#             elif risk_level == "Medium Risk":

#                 st.warning(
#                     f"⚠️ ALERT TRIGGERED | {alert_message}"
#                 )

#                 st.warning(
#                     "Recommended Action: Trigger OTP verification and monitor activity"
#                 )

#         else:

#             st.success(
#                 f"✅ No Alert Triggered | {alert_message}"
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
#                     {'range': [0,15], 'color': "lightgreen"},
#                     {'range': [15,30], 'color': "yellow"},
#                     {'range': [30,100], 'color': "red"}
#                 ]
#             }
#         ))

#         st.plotly_chart(gauge_chart, use_container_width=True)

# # =========================
# # DASHBOARD TAB
# # =========================

# with dashboard_tab:

#     st.header("Fraud Analytics Dashboard")

#     np.random.seed(42)

#     dashboard_data = pd.DataFrame({
#         'Risk_Level': np.random.choice(
#             ['Low Risk', 'Medium Risk', 'High Risk'],
#             200,
#             p=[0.6,0.25,0.15]
#         ),
#         'Fraud_Probability': np.random.uniform(0,1,200),
#         'Transaction_Amount': np.random.randint(100,50000,200)
#     })

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

#     chart_col1, chart_col2 = st.columns(2)

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
#         'Fraud_Probability': np.random.uniform(0.15,1.0,10),
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
from datetime import datetime

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
# SESSION STATE STORAGE
# =========================

if "fraud_alerts" not in st.session_state:

    st.session_state.fraud_alerts = []

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
- Real-Time Fraud Monitoring
- Investigation Queue Management
""")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("⚙️ Fraud Monitoring Panel")

threshold = st.sidebar.slider(
    "Fraud Threshold",
    0.0,
    1.0,
    0.15
)

st.sidebar.markdown("---")

st.sidebar.write("### Risk Rules")
st.sidebar.write("- Low Risk : 0% - 15%")
st.sidebar.write("- Medium Risk : 15% - 30%")
st.sidebar.write("- High Risk : > 30%")

st.sidebar.markdown("---")

st.sidebar.write("### Threshold Logic")
st.sidebar.write(
    "If Fraud Probability ≥ Threshold → Alert Triggered"
)

# =========================
# TABS
# =========================

prediction_tab, dashboard_tab, alerts_tab = st.tabs([
    "🔍 Fraud Prediction",
    "📊 Fraud Dashboard",
    "🚨 Fraud Alerts"
])

# ============================================================
# FRAUD PREDICTION TAB
# ============================================================

with prediction_tab:

    st.header("Transaction Monitoring Engine")

    col1, col2, col3 = st.columns(3)

    # =========================
    # INPUTS
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

    # ============================================================
    # PREDICT BUTTON
    # ============================================================

    if st.button("🚨 Predict Fraud"):

        # =========================
        # INPUT FEATURE DICTIONARY
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
        # FEATURE ORDER
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
        # SCALE FEATURES
        # =========================

        input_scaled = scaler.transform(input_data)

        # =========================
        # MODEL PREDICTION
        # =========================

        fraud_probability = model.predict_proba(
            input_scaled
        )[0][1]

        # =========================
        # RISK CLASSIFICATION
        # =========================

        if fraud_probability > 0.30:

            risk_level = "High Risk"
            monitoring_action = "Block Transaction"

        elif fraud_probability >= 0.15:

            risk_level = "Medium Risk"
            monitoring_action = "OTP Verification"

        else:

            risk_level = "Low Risk"
            monitoring_action = "Allow Transaction"

        # =========================
        # ALERT PRIORITY
        # =========================

        if risk_level == "High Risk":

            alert_priority = "P1 - Critical"

        elif risk_level == "Medium Risk":

            alert_priority = "P2 - Moderate"

        else:

            alert_priority = "P3 - Low"

        # =========================
        # ALERT THRESHOLD LOGIC
        # =========================

        if fraud_probability >= threshold:

            alert_status = "🚨 ALERT TRIGGERED"

        else:

            alert_status = "✅ No Alert"

        # =========================
        # FRAUD REASONS
        # =========================

        fraud_reasons = []

        if high_amount_flag == 1:
            fraud_reasons.append("High Amount Transaction")

        if night_transaction == 1:
            fraud_reasons.append("Night Activity")

        if rapid_transaction_flag == 1:
            fraud_reasons.append("Rapid Transactions")

        if amount_ratio > 1.5:
            fraud_reasons.append("Behavioral Amount Deviation")

        if is_weekend == 1:
            fraud_reasons.append("Weekend Activity")

        if len(fraud_reasons) == 0:
            fraud_reasons.append("Normal Transaction Pattern")

        # =========================
        # ALERT MESSAGE
        # =========================

        if risk_level == "High Risk":

            alert_message = "Immediate Investigation Required"

        elif risk_level == "Medium Risk":

            alert_message = "Monitor Transaction"

        else:

            alert_message = "Normal Activity"

        # =========================
        # DISPLAY RESULTS
        # =========================

        st.markdown("---")

        st.subheader("Fraud Intelligence Results")

        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

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

        with metric_col4:

            st.metric(
                "Alert Status",
                alert_status
            )

        st.progress(float(fraud_probability))

        # =========================
        # ALERT DISPLAY
        # =========================

        if fraud_probability >= threshold:

            if risk_level == "High Risk":

                st.error(
                    f"🚨 ALERT TRIGGERED | {alert_message}"
                )

                st.error(
                    "Recommended Action: Block transaction and escalate to fraud investigation team"
                )

            elif risk_level == "Medium Risk":

                st.warning(
                    f"⚠️ ALERT TRIGGERED | {alert_message}"
                )

                st.warning(
                    "Recommended Action: Trigger OTP verification and monitor activity"
                )

        else:

            st.success(
                f"✅ No Alert Triggered | {alert_message}"
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

                    {'range': [0,15], 'color': "lightgreen"},

                    {'range': [15,30], 'color': "yellow"},

                    {'range': [30,100], 'color': "red"}

                ]
            }
        ))

        st.plotly_chart(
            gauge_chart,
            use_container_width=True
        )

        # ============================================================
        # STORE LIVE ALERTS
        # ============================================================

        if fraud_probability >= threshold:

            alert_record = {

                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "Transaction_ID": f"TXN{np.random.randint(10000,99999)}",

                "Fraud_Probability": round(
                    fraud_probability * 100,
                    2
                ),

                "Risk_Level": risk_level,

                "Priority": alert_priority,

                "Monitoring_Action": monitoring_action,

                "Fraud_Reasons": ", ".join(fraud_reasons),

                "Status": "Open"

            }

            st.session_state.fraud_alerts.append(
                alert_record
            )

# ============================================================
# DASHBOARD TAB
# ============================================================

with dashboard_tab:

    st.header("Fraud Analytics Dashboard")

    np.random.seed(42)

    dashboard_data = pd.DataFrame({

        'Risk_Level': np.random.choice(

            ['Low Risk', 'Medium Risk', 'High Risk'],

            200,

            p=[0.6,0.25,0.15]

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
            (
                dashboard_data['Risk_Level']
                == 'High Risk'
            ).sum()
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

# ============================================================
# ALERT TAB
# ============================================================

with alerts_tab:

    st.header("🚨 Real-Time Fraud Alert Center")

    # =========================
    # NO ALERTS
    # =========================

    if len(st.session_state.fraud_alerts) == 0:

        st.success(
            "✅ No Fraud Alerts Generated Yet"
        )

    else:

        alerts_df = pd.DataFrame(
            st.session_state.fraud_alerts
        )

        # =========================
        # FILTERS
        # =========================

        st.subheader("Fraud Monitoring Filters")

        filter_col1, filter_col2 = st.columns(2)

        with filter_col1:

            selected_risk = st.multiselect(

                "Filter by Risk Level",

                options=alerts_df[
                    'Risk_Level'
                ].unique(),

                default=alerts_df[
                    'Risk_Level'
                ].unique()

            )

        with filter_col2:

            selected_status = st.multiselect(

                "Filter by Status",

                options=alerts_df[
                    'Status'
                ].unique(),

                default=alerts_df[
                    'Status'
                ].unique()

            )

        filtered_df = alerts_df[

            (
                alerts_df['Risk_Level'].isin(
                    selected_risk
                )
            )

            &

            (
                alerts_df['Status'].isin(
                    selected_status
                )
            )

        ]

        st.markdown("---")

        # =========================
        # LIVE ALERT FEED
        # =========================

        st.subheader("📡 Live Fraud Alert Feed")

        for index, row in filtered_df.iterrows():

            alert_text = f"""
            🚨 {row['Transaction_ID']}
            | Fraud Probability: {row['Fraud_Probability']}%
            | Risk: {row['Risk_Level']}
            | Priority: {row['Priority']}
            | Action: {row['Monitoring_Action']}
            """

            if row['Risk_Level'] == "High Risk":

                st.error(alert_text)

            elif row['Risk_Level'] == "Medium Risk":

                st.warning(alert_text)

            else:

                st.info(alert_text)

        st.markdown("---")

        # =========================
        # ALERT ANALYTICS
        # =========================

        st.subheader("📊 Fraud Alert Analytics")

        analytic_col1, analytic_col2 = st.columns(2)

        with analytic_col1:

            risk_chart = px.pie(

                filtered_df,

                names='Risk_Level',

                title='Alert Distribution by Risk Level'

            )

            st.plotly_chart(
                risk_chart,
                use_container_width=True
            )

        with analytic_col2:

            priority_chart = px.histogram(

                filtered_df,

                x='Priority',

                title='Alert Priority Distribution'

            )

            st.plotly_chart(
                priority_chart,
                use_container_width=True
            )

        # =========================
        # INVESTIGATION QUEUE
        # =========================

        st.subheader("🕵️ Fraud Investigation Queue")

        st.dataframe(

            filtered_df[[
                'Timestamp',
                'Transaction_ID',
                'Fraud_Probability',
                'Risk_Level',
                'Priority',
                'Monitoring_Action',
                'Fraud_Reasons',
                'Status'
            ]],

            use_container_width=True

        )

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "Banking Fraud Detection System | Machine Learning + Real-Time Fraud Intelligence + Monitoring Dashboard"
)
