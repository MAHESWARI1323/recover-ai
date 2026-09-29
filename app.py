import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Recover AI",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# STYLING
# =========================================================

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #f5f7fb;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
}

[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

/* Sidebar Logo */
.logo {
    font-size: 30px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #ffffff;
    margin-bottom: 4px;
}

.logo span {
    color: #22c55e;
}

/* Sidebar subtitle */
.small-text {
    color: #94a3b8;
    font-size: 12px;
}

/* Main headings */
h1, h2, h3 {
    color: #111827;
}

/* Cards */
.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
    margin-bottom: 15px;
}

/* KPI cards */
[data-testid="stMetric"] {
    background: #ffffff;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
}

/* KPI value */
[data-testid="stMetricValue"] {
    color: #111827;
    font-weight: 750;
}

/* AI insight */
.ai-box {
    background: linear-gradient(135deg, #ecfdf5, #f0fdf4);
    border: 1px solid #bbf7d0;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(22, 163, 74, 0.06);
}

/* Policy box */
.policy-box {
    background: linear-gradient(135deg, #eff6ff, #f8fafc);
    border: 1px solid #bfdbfe;
    padding: 20px;
    border-radius: 16px;
}

/* Warning box */
.warning-box {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    padding: 20px;
    border-radius: 16px;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    padding: 10px 18px;
}

/* Select boxes and text input */
.stSelectbox > div > div,
.stTextInput > div > div {
    border-radius: 10px;
}

/* Data tables */
[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* Divider */
hr {
    border-color: #e2e8f0;
}

/* Info / success / warning messages */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Footer text */
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TRANSACTION DATA
# =========================================================

transactions = pd.DataFrame([
    {
        "Transaction": "TXN-10481",
        "Customer": "Customer B",
        "Amount": 129.50,
        "Failure": "Temporary Bank Error",
        "Retry Count": 0
    },
    {
        "Transaction": "TXN-10482",
        "Customer": "Customer A",
        "Amount": 249.00,
        "Failure": "Insufficient Funds",
        "Retry Count": 1
    },
    {
        "Transaction": "TXN-10483",
        "Customer": "Customer C",
        "Amount": 499.00,
        "Failure": "Authentication Failure",
        "Retry Count": 0
    },
    {
        "Transaction": "TXN-10484",
        "Customer": "Customer D",
        "Amount": 79.00,
        "Failure": "Network Timeout",
        "Retry Count": 0
    },
    {
        "Transaction": "TXN-10485",
        "Customer": "Customer E",
        "Amount": 319.00,
        "Failure": "Card Expired",
        "Retry Count": 0
    },
    {
        "Transaction": "TXN-10486",
        "Customer": "Customer F",
        "Amount": 189.00,
        "Failure": "Temporary Bank Error",
        "Retry Count": 1
    },
    {
        "Transaction": "TXN-10487",
        "Customer": "Customer G",
        "Amount": 649.00,
        "Failure": "Authentication Failure",
        "Retry Count": 0
    },
    {
        "Transaction": "TXN-10488",
        "Customer": "Customer H",
        "Amount": 99.00,
        "Failure": "Network Timeout",
        "Retry Count": 0
    }
])


# =========================================================
# AI DECISION ENGINE
# =========================================================

def ai_analyze(transaction):

    failure = transaction["Failure"]
    amount = transaction["Amount"]
    retry_count = transaction["Retry Count"]

    if failure == "Temporary Bank Error":

        probability = 88
        diagnosis = "Temporary issuer-side problem"
        recommendation = "Retry payment after a short delay"

        if retry_count >= 2:
            policy = "BLOCK"
            reason = "Retry limit exceeded"
            action = "Do not retry"
        else:
            policy = "ALLOW"
            reason = "Temporary failure with high recovery probability"
            action = "Retry once"

    elif failure == "Network Timeout":

        probability = 84
        diagnosis = "Payment request timed out"
        recommendation = "Retry the transaction once"
        policy = "ALLOW"
        reason = "Network issue is usually temporary"
        action = "Retry once"

    elif failure == "Insufficient Funds":

        probability = 32
        diagnosis = "Customer balance appears insufficient"
        recommendation = "Request another payment method"
        policy = "BLOCK"
        reason = "Automatic retry may create repeated failures"
        action = "No automatic retry"

    elif failure == "Authentication Failure":

        probability = 48
        diagnosis = "Authentication or verification problem"
        recommendation = "Send transaction for human review"
        policy = "ESCALATE"
        reason = "Authentication failures require additional verification"
        action = "Human review"

    elif failure == "Card Expired":

        probability = 18
        diagnosis = "Payment card is expired"
        recommendation = "Ask customer to update payment method"
        policy = "BLOCK"
        reason = "Retrying an expired card is unlikely to succeed"
        action = "Request new payment method"

    else:

        probability = 40
        diagnosis = "Unknown payment failure"
        recommendation = "Human review"
        policy = "ESCALATE"
        reason = "Failure reason requires investigation"
        action = "Escalate"

    expected_recovery = amount * probability / 100

    return {
        "probability": probability,
        "diagnosis": diagnosis,
        "recommendation": recommendation,
        "policy": policy,
        "reason": reason,
        "action": action,
        "expected": expected_recovery
    }


# =========================================================
# SESSION STATE
# =========================================================

if "audit" not in st.session_state:

    st.session_state.audit = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="logo">recover<span>AI</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small-text">AI Revenue Recovery Agent</div>',
        unsafe_allow_html=True
    )

    st.write("")

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "AI Decision Engine",
            "Transactions",
            "Policy Center",
            "Audit Trail",
            "Merchant Assistant"
        ]
    )

    st.write("")

    st.markdown("""
    <div style="
        background:#1f2937;
        padding:15px;
        border-radius:12px;
    ">
    <b>Demo Environment</b><br>
    <span style="font-size:12px;color:#9ca3af;">
    All payment actions are simulated.
    </span>
    <br><br>
    🟢 Systems nominal
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================




# =========================================================
# OVERVIEW
# =========================================================

if page == "Overview":

    # =========================
    # HEADER
    # =========================

    st.markdown(
        "## Revenue Recovery Command Center"
    )

    st.caption(
        "Monitor failed payments, identify recovery opportunities "
        "and understand every AI decision."
    )

    # =========================
    # KPI CALCULATIONS
    # =========================

    total_risk = transactions["Amount"].sum()

    recovery_candidates = transactions[
        transactions["Failure"].isin(
            ["Temporary Bank Error", "Network Timeout"]
        )
    ]

    potential_recovery = 0

    for _, row in recovery_candidates.iterrows():
        result = ai_analyze(row)
        potential_recovery += result["expected"]

    high_risk = len(
        transactions[
            transactions["Amount"] >= 300
        ]
    )

    policy_compliance = 94.7

    # =========================
    # KPI CARDS
    # =========================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "💰 Revenue at Risk",
            f"₹{total_risk:,.0f}",
            "+8.4%"
        )

    with c2:
        st.metric(
            "🎯 Recovery Opportunity",
            f"₹{potential_recovery:,.0f}",
            "+12.8%"
        )

    with c3:
        st.metric(
            "⚡ Recovery Rate",
            "68.4%",
            "+5.2%"
        )

    with c4:
        st.metric(
            "🛡️ Policy Compliance",
            f"{policy_compliance}%",
            "Healthy"
        )

    st.divider()

    # =========================
    # AI INSIGHT + RISK
    # =========================

    left, right = st.columns([1.4, 1])

    with left:

        st.subheader("🧠 AI Insight")

        st.markdown(
            """
            <div class="ai-box">

            <b>Recovery opportunity detected</b>

            <br><br>

            Temporary payment failures currently represent the
            strongest recovery opportunity.

            <br><br>

            Recover AI recommends prioritizing high-probability
            transactions while preventing unnecessary retries.

            <br><br>

            <b>AI recommendation:</b>
            Prioritize temporary failures with recovery probability
            above 75%.

            </div>
            """,
            unsafe_allow_html=True
        )

    with right:

        st.subheader("🚨 Risk Monitor")

        st.metric(
            "High-value failed transactions",
            high_risk
        )

        st.progress(
            min(high_risk / len(transactions), 1.0)
        )

        st.caption(
            "Transactions requiring closer monitoring"
        )

    # =========================
    # REVENUE EXPOSURE
    # =========================

    st.subheader("📊 Revenue Exposure by Failure")

    exposure = transactions.groupby(
        "Failure"
    )["Amount"].sum().sort_values(
        ascending=False
    )

    st.bar_chart(exposure)

    # =========================
    # RECOVERY OPPORTUNITIES
    # =========================

    st.subheader("🎯 Top Recovery Opportunities")

    opportunity_rows = []

    for _, row in transactions.iterrows():

        result = ai_analyze(row)

        if result["policy"] == "ALLOW":

            opportunity_rows.append({
                "Transaction": row["Transaction"],
                "Failure": row["Failure"],
                "Amount": f"₹{row['Amount']:,.2f}",
                "AI Score": f"{result['probability']}%",
                "Expected Recovery": f"₹{result['expected']:,.2f}",
                "Action": result["action"]
            })

    if opportunity_rows:

        opportunity_df = pd.DataFrame(opportunity_rows)

        st.table(opportunity_df)

    else:

        st.info("No recovery opportunities found.")

    # =========================
    # DECISION WORKFLOW
    # =========================

    st.subheader("🔄 AI Decision Pipeline")

    stages = [
        ("01", "Detect", "Find failed payments"),
        ("02", "Diagnose", "Understand failure"),
        ("03", "Score", "Estimate recovery"),
        ("04", "Policy", "Check boundaries"),
        ("05", "Intervene", "Choose action"),
        ("06", "Simulate", "Predict outcome"),
        ("07", "Audit", "Record decision")
    ]

    cols = st.columns(7)

    for i, (number, name, description) in enumerate(stages):

        with cols[i]:

            st.markdown(f"### {number}")

            st.markdown(f"**{name}**")

            st.caption(description)

            if i < 6:
                st.markdown("↓")

    # =========================
    # SYSTEM STATUS
    # =========================

    st.subheader("✅ System Status")

    s1, s2, s3 = st.columns(3)

    with s1:
        st.success(
            "AI Model — Operational"
        )

    with s2:
        st.success(
            "Policy Engine — Operational"
        )

    with s3:
        st.success(
            "Audit Engine — Operational"
        )

    st.info(
        "Recover AI follows bounded autonomy: "
        "AI recommends, policy decides, and every decision is audited."
    )  

# =========================================================
# AI DECISION ENGINE
# =========================================================

elif page == "AI Decision Engine":

    st.markdown("## 🤖 AI Decision Engine")
    st.caption(
        "AI-powered payment recovery intelligence • Simulation Mode"
    )

    st.divider()

    # =========================================================
    # TRANSACTION SELECTION
    # =========================================================

    st.subheader("🔍 Analyze Failed Transaction")

    selected_txn = st.selectbox(
        "Select a transaction to analyze",
        transactions["Transaction"].tolist()
    )

    selected_row = transactions[
        transactions["Transaction"] == selected_txn
    ].iloc[0]

    result = ai_analyze(selected_row)

    # =========================================================
    # TRANSACTION OVERVIEW
    # =========================================================

    st.markdown("### 📋 Transaction Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Transaction",
            selected_row["Transaction"]
        )

    with c2:
        st.metric(
            "Customer",
            selected_row["Customer"]
        )

    with c3:
        st.metric(
            "Amount",
            f"₹{selected_row['Amount']:,.2f}"
        )

    with c4:
        st.metric(
            "Failure Type",
            selected_row["Failure"]
        )

    st.divider()

    # =========================================================
    # AI ANALYSIS
    # =========================================================

    st.subheader("🧠 AI Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### AI Diagnosis")

        st.info(
            result["diagnosis"]
        )

        st.markdown("#### Recovery Probability")

        st.progress(
            result["probability"] / 100
        )

        st.markdown(
            f"### {result['probability']}%"
        )

        st.caption(
            f"Expected recovery: "
            f"₹{result['expected']:.2f}"
        )

    with col2:

        st.markdown("#### 🛡️ Policy Decision")

        if result["policy"] == "ALLOW":

            st.success("### 🟢 ALLOW")

        elif result["policy"] == "ESCALATE":

            st.warning("### 🟡 ESCALATE")

        else:

            st.error("### 🔴 BLOCK")

        st.markdown(
            f"**Reason:** {result['reason']}"
        )

        st.markdown(
            f"**Recommended Action:** "
            f"{result['action']}"
        )

    st.divider()

    # =========================================================
    # DECISION EXPLANATION
    # =========================================================

    st.subheader("💡 Why did AI make this recommendation?")

    e1, e2, e3 = st.columns(3)

    with e1:

        st.markdown("### 01 🔎 Diagnose")

        st.caption(
            "The AI identifies the likely reason "
            "for the payment failure."
        )

    with e2:

        st.markdown("### 02 📊 Score")

        st.caption(
            "The AI estimates the probability "
            "of successful recovery."
        )

    with e3:

        st.markdown("### 03 🛡️ Policy")

        st.caption(
            "The policy engine validates whether "
            "the recommended action is allowed."
        )

    st.divider()

    # =========================================================
    # SIMULATION
    # =========================================================

    st.subheader("⚡ Recovery Simulation")

    st.write(
        "Simulate the recommended recovery action "
        "without performing a real payment."
    )

    if st.button(
        "▶ Run Recovery Simulation",
        use_container_width=True
    ):
        st.session_state.audit.append({
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Transaction": selected_row["Transaction"],
            "Failure": selected_row["Failure"],
            "AI Score": f"{result['probability']}%",
            "Policy": result["policy"],
            "Action": result["action"],
            "Expected Recovery": f"₹{result['expected']:.2f}"
        })

        if result["policy"] == "ALLOW":

            st.success(
                f"Simulation successful — "
                f"{result['action']} would be attempted."
            )

            st.metric(
                "Simulated Recovery",
                f"₹{result['expected']:.2f}"
            )

        elif result["policy"] == "ESCALATE":

            st.warning(
                "Simulation stopped. "
                "Transaction requires human review."
            )

        else:

            st.error(
                "Simulation blocked by policy. "
                "No recovery action is allowed."
            )

    st.divider()

    # =========================================================
    # DECISION FLOW
    # =========================================================

    st.subheader("🔄 Decision Flow")

    flow1, flow2, flow3, flow4 = st.columns(4)

    with flow1:
        st.markdown("### 🔍 Detect")
        st.caption("Failed payment identified")

    with flow2:
        st.markdown("### 🧠 AI Score")
        st.caption("Recovery probability calculated")

    with flow3:
        st.markdown("### 🛡️ Policy")
        st.caption("Action validated")

    with flow4:
        st.markdown("### 🧾 Audit")
        st.caption("Decision recorded")

    st.info(
        "Recover AI follows bounded autonomy: "
        "AI recommends → Policy validates → "
        "Action is simulated → Decision is audited."
    )



# =========================================================
# TRANSACTIONS
# =========================================================

elif page == "Transactions":

    st.markdown("## 💳 Transaction Intelligence")

    st.caption(
        "Investigate failed payments, understand recovery risk, "
        "and review AI-generated decisions."
    )

    st.divider()

    # =====================================================
    # TRANSACTION SUMMARY
    # =====================================================

    total_transactions = len(transactions)

    total_failed_value = transactions["Amount"].sum()

    avg_amount = transactions["Amount"].mean()

    recovery_candidates = 0

    for _, row in transactions.iterrows():

        result = ai_analyze(row)

        if result["policy"] == "ALLOW":
            recovery_candidates += 1

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Failed Transactions",
            total_transactions
        )

    with c2:
        st.metric(
            "Failed Value",
            f"₹{total_failed_value:,.0f}"
        )

    with c3:
        st.metric(
            "Average Transaction",
            f"₹{avg_amount:,.2f}"
        )

    with c4:
        st.metric(
            "Recovery Candidates",
            recovery_candidates
        )

    st.divider()

    # =====================================================
    # FAILED TRANSACTION TABLE
    # =====================================================

    st.subheader("📋 Failed Payment Queue")

    display_df = transactions.copy()

    display_df["Status"] = display_df.apply(
        lambda row:
        "🟢 Recovery Candidate"
        if ai_analyze(row)["policy"] == "ALLOW"
        else
        "🟡 Human Review"
        if ai_analyze(row)["policy"] == "ESCALATE"
        else
        "🔴 Blocked",
        axis=1
    )

    display_df["Amount"] = display_df["Amount"].apply(
        lambda x: f"₹{x:,.2f}"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================================
    # INVESTIGATE TRANSACTION
    # =====================================================

    st.subheader("🔎 Investigate Transaction")

    selected_id = st.selectbox(
        "Select a failed transaction",
        transactions["Transaction"].tolist()
    )

    tx = transactions[
        transactions["Transaction"] == selected_id
    ].iloc[0]

    result = ai_analyze(tx)

    # =====================================================
    # TRANSACTION HEADER
    # =====================================================

    st.markdown(
        f"### {selected_id}"
    )

    st.caption(
        f"{tx['Customer']} • {tx['Failure']}"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Transaction Amount",
            f"₹{tx['Amount']:,.2f}"
        )

    with c2:
        st.metric(
            "Recovery Probability",
            f"{result['probability']}%"
        )

    with c3:
        st.metric(
            "Expected Recovery",
            f"₹{result['expected']:,.2f}"
        )

    with c4:
        st.metric(
            "Retry Count",
            tx["Retry Count"]
        )

    st.divider()

    # =====================================================
    # AI DIAGNOSIS
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("🧠 AI Diagnosis")

        st.info(
            result["diagnosis"]
        )

        st.markdown("**AI Recommendation**")

        st.write(
            result["recommendation"]
        )

    with right:

        st.subheader("🛡️ Policy Decision")

        if result["policy"] == "ALLOW":

            st.success(
                "🟢 ALLOW"
            )

        elif result["policy"] == "ESCALATE":

            st.warning(
                "🟡 ESCALATE"
            )

        else:

            st.error(
                "🔴 BLOCK"
            )

        st.markdown(
            f"**Reason:** {result['reason']}"
        )

        st.markdown(
            f"**Action:** {result['action']}"
        )

    st.divider()

    # =====================================================
    # RECOVERY SCORE
    # =====================================================

    st.subheader("📊 Recovery Intelligence")

    st.progress(
        result["probability"] / 100
    )

    if result["probability"] >= 75:

        st.success(
            f"High recovery potential — "
            f"{result['probability']}% probability."
        )

    elif result["probability"] >= 50:

        st.warning(
            f"Moderate recovery potential — "
            f"{result['probability']}% probability."
        )

    else:

        st.error(
            f"Low recovery potential — "
            f"{result['probability']}% probability."
        )

    st.divider()

    # =====================================================
    # DECISION EXPLANATION
    # =====================================================

    st.subheader("💡 Decision Explanation")

    d1, d2, d3 = st.columns(3)

    with d1:

        st.markdown("### 01 🔍 Diagnose")

        st.caption(
            f"Failure identified as "
            f"**{tx['Failure']}**."
        )

    with d2:

        st.markdown("### 02 📈 Score")

        st.caption(
            f"AI estimated recovery probability "
            f"at **{result['probability']}%**."
        )

    with d3:

        st.markdown("### 03 🛡️ Policy")

        st.caption(
            f"Policy engine decided to "
            f"**{result['policy']}** the transaction."
        )

    st.divider()

    st.info(
        "Every transaction passes through the same principle: "
        "AI analyzes → Recovery score → Policy validation → "
        "Controlled action."
    )


# =========================================================
# POLICY CENTER
# =========================================================

elif page == "Policy Center":

    st.markdown("## 🛡️ Policy Control Center")

    st.caption(
        "Define safe recovery boundaries and control what Recover AI is allowed to do."
    )

    st.divider()

    # =====================================================
    # POLICY SUMMARY
    # =====================================================

    st.subheader("📊 Policy Overview")

    p1, p2, p3, p4 = st.columns(4)

    with p1:
        st.metric("Active Policies", "5")

    with p2:
        st.metric("Auto-Recovery Rules", "2")

    with p3:
        st.metric("Human Review Rules", "1")

    with p4:
        st.metric("Blocked Rules", "2")

    st.divider()

    # =====================================================
    # POLICY TABLE
    # =====================================================

    st.subheader("📋 Recovery Policy Rules")

    policies = pd.DataFrame([
        {
            "Failure Type": "Temporary Bank Error",
            "Recovery Score": "≥ 75%",
            "Decision": "ALLOW",
            "Action": "Retry once",
            "Risk Level": "Low"
        },
        {
            "Failure Type": "Network Timeout",
            "Recovery Score": "≥ 75%",
            "Decision": "ALLOW",
            "Action": "Retry once",
            "Risk Level": "Low"
        },
        {
            "Failure Type": "Insufficient Funds",
            "Recovery Score": "Any",
            "Decision": "BLOCK",
            "Action": "No automatic retry",
            "Risk Level": "High"
        },
        {
            "Failure Type": "Authentication Failure",
            "Recovery Score": "Any",
            "Decision": "ESCALATE",
            "Action": "Human review",
            "Risk Level": "Medium"
        },
        {
            "Failure Type": "Card Expired",
            "Recovery Score": "Any",
            "Decision": "BLOCK",
            "Action": "Update payment method",
            "Risk Level": "High"
        }
    ])

    st.dataframe(
        policies,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================================
    # POLICY LOGIC
    # =====================================================

    st.subheader("🧠 How Policy Decisions Work")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.markdown("### 🟢 ALLOW")
        st.write(
            "Used when the failure is temporary and "
            "the recovery probability is high."
        )

    with a2:
        st.markdown("### 🟡 ESCALATE")
        st.write(
            "Used when additional verification or "
            "human judgment is required."
        )

    with a3:
        st.markdown("### 🔴 BLOCK")
        st.write(
            "Used when automatic recovery is unsafe "
            "or unlikely to succeed."
        )

    st.divider()

    # =====================================================
    # CORE PRINCIPLE
    # =====================================================

    st.subheader("🔐 Bounded Autonomy")

    st.info(
        "AI recommends. Policy decides. "
        "Recover AI never performs an action outside "
        "the approved policy boundaries."
    )

    b1, b2, b3, b4 = st.columns(4)

    with b1:
        st.markdown("### 01")
        st.caption("AI analyzes the failure")

    with b2:
        st.markdown("### 02")
        st.caption("Recovery probability is calculated")

    with b3:
        st.markdown("### 03")
        st.caption("Policy validates the action")

    with b4:
        st.markdown("### 04")
        st.caption("Decision is audited")

# =========================================================
# AUDIT TRAIL
# =========================================================

elif page == "Audit Trail":

    st.markdown("## 📋 Decision Audit Trail")
    st.caption(
        "Complete history of AI decisions, policy checks, "
        "simulated recovery actions, and outcomes."
    )

    st.divider()

    # =====================================================
    # AUDIT SUMMARY
    # =====================================================

    total_actions = len(st.session_state.audit)

    successful = 0
    escalated = 0
    blocked = 0

    for item in st.session_state.audit:
        if item["Policy"] == "ALLOW":
            successful += 1
        elif item["Policy"] == "ESCALATE":
            escalated += 1
        elif item["Policy"] == "BLOCK":
            blocked += 1

    a1, a2, a3, a4 = st.columns(4)

    with a1:
        st.metric("Total Decisions", total_actions)

    with a2:
        st.metric("Simulated Recoveries", successful)

    with a3:
        st.metric("Escalations", escalated)

    with a4:
        st.metric("Blocked Actions", blocked)

    st.divider()

    # =====================================================
    # AUDIT HISTORY
    # =====================================================

    st.subheader("🧾 Decision History")

    if total_actions == 0:

        st.info(
            "No decisions recorded yet. "
            "Run a recovery simulation from the AI Decision Engine."
        )

    else:

        audit_df = pd.DataFrame(st.session_state.audit)

        st.dataframe(
            audit_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # =====================================================
    # AUDIT PRINCIPLES
    # =====================================================

    st.subheader("🔐 Audit Principles")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown("### 🧠 Explainable")
        st.write(
            "Every AI decision includes the recovery score "
            "and policy reasoning."
        )

    with p2:
        st.markdown("### 🛡️ Controlled")
        st.write(
            "Only policy-approved recovery actions "
            "can be simulated."
        )

    with p3:
        st.markdown("### 📋 Traceable")
        st.write(
            "Every simulated action is recorded "
            "for future review."
        )

    st.divider()

    # =====================================================
    # AUDIT FLOW
    # =====================================================

    st.subheader("🔄 Audit Flow")

    f1, f2, f3, f4 = st.columns(4)

    with f1:
        st.markdown("### 01")
        st.caption("Transaction detected")

    with f2:
        st.markdown("### 02")
        st.caption("AI decision generated")

    with f3:
        st.markdown("### 03")
        st.caption("Policy validated")

    with f4:
        st.markdown("### 04")
        st.caption("Decision recorded")

   


# =========================================================
# MERCHANT ASSISTANT
# =========================================================

elif page == "Merchant Assistant":

    st.markdown("## 💬 Merchant Assistant")
    st.caption(
        "Ask Recover AI about revenue risk, recovery opportunities, "
        "transactions, and policy decisions."
    )

    st.divider()

    # =====================================================
    # ASSISTANT OVERVIEW
    # =====================================================

    st.subheader("🤖 AI Revenue Intelligence")

    q1, q2, q3 = st.columns(3)

    # Calculate recovery opportunity
    total_opportunity = 0

    for _, row in transactions.iterrows():
        result = ai_analyze(row)

        if result["policy"] == "ALLOW":
            total_opportunity += result["expected"]

    with q1:
        st.metric(
            "Revenue at Risk",
            f"₹{transactions['Amount'].sum():,.2f}"
        )

    with q2:
        st.metric(
            "Recovery Opportunity",
            f"₹{total_opportunity:,.2f}"
        )

    with q3:
        st.metric(
            "Failed Transactions",
            len(transactions)
        )

    st.divider()

    # =====================================================
    # ASK AI
    # =====================================================

    st.subheader("💭 Ask Recover AI")

    question = st.text_input(
        "Ask a question",
        placeholder="Example: Which failure reason has the highest revenue risk?"
    )

    if st.button("✨ Ask AI", use_container_width=True):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            q = question.lower()

            # ---------------------------------------------
            # REVENUE RISK
            # ---------------------------------------------

            if "risk" in q or "highest" in q and "failure" in q:

                exposure = (
                    transactions
                    .groupby("Failure")["Amount"]
                    .sum()
                    .sort_values(ascending=False)
                )

                reason = exposure.index[0]
                amount = exposure.iloc[0]

                st.success(
                    f"💡 The highest revenue risk comes from "
                    f"**{reason}**, with approximately "
                    f"**₹{amount:,.2f}** in failed transaction exposure."
                )

            # ---------------------------------------------
            # RECOVERY OPPORTUNITY
            # ---------------------------------------------

            elif "opportunity" in q or "recover" in q:

                opportunities = []

                for _, row in transactions.iterrows():

                    result = ai_analyze(row)

                    if result["policy"] == "ALLOW":
                        opportunities.append({
                            "Transaction": row["Transaction"],
                            "Amount": row["Amount"],
                            "Probability": result["probability"],
                            "Expected": result["expected"]
                        })

                if opportunities:

                    opportunities.sort(
                        key=lambda x: x["Expected"],
                        reverse=True
                    )

                    top = opportunities[0]

                    st.success(
                        f"🎯 The highest-priority recovery opportunity is "
                        f"**{top['Transaction']}** with an estimated recovery "
                        f"of **₹{top['Expected']:,.2f}** "
                        f"({top['Probability']}% probability)."
                    )

            # ---------------------------------------------
            # TRANSACTION QUESTION
            # ---------------------------------------------

            elif "txn-" in q:

                transaction_id = None

                for txn in transactions["Transaction"]:
                    if txn.lower() in q:
                        transaction_id = txn
                        break

                if transaction_id:

                    tx = transactions[
                        transactions["Transaction"] == transaction_id
                    ].iloc[0]

                    result = ai_analyze(tx)

                    st.info(
                        f"""
**Transaction:** {transaction_id}

**Customer:** {tx['Customer']}

**Amount:** ₹{tx['Amount']:,.2f}

**Failure:** {tx['Failure']}

**Recovery Probability:** {result['probability']}%

**Policy Decision:** {result['policy']}

**Recommended Action:** {result['action']}
"""
                    )

                else:
                    st.warning(
                        "I couldn't find that transaction. "
                        "Try a transaction such as TXN-10481."
                    )

            # ---------------------------------------------
            # POLICY QUESTION
            # ---------------------------------------------

            elif "policy" in q or "allow" in q or "block" in q:

                st.info(
                    """
### 🛡️ Recover AI Policy

**AI recommends. Policy decides.**

The AI analyzes the payment failure and calculates
a recovery probability.

The policy engine then decides whether the action
should be:

🟢 **ALLOW** — controlled recovery action

🟡 **ESCALATE** — human review required

🔴 **BLOCK** — automatic recovery not allowed
"""
                )

            # ---------------------------------------------
            # PRIORITY QUESTION
            # ---------------------------------------------

            elif "priority" in q or "prioritize" in q:

                priorities = []

                for _, row in transactions.iterrows():

                    result = ai_analyze(row)

                    if result["policy"] == "ALLOW":

                        priorities.append({
                            "Transaction": row["Transaction"],
                            "Expected": result["expected"],
                            "Probability": result["probability"]
                        })

                priorities.sort(
                    key=lambda x: x["Expected"],
                    reverse=True
                )

                if priorities:

                    top = priorities[0]

                    st.success(
                        f"🚀 Prioritize **{top['Transaction']}** first. "
                        f"It has a **{top['probability']}%** recovery probability "
                        f"and approximately **₹{top['Expected']:,.2f}** expected recovery."
                    )

            # ---------------------------------------------
            # GENERAL QUESTION
            # ---------------------------------------------

            else:

                st.info(
                    """
I can help you understand:

• Revenue risk  
• Recovery opportunities  
• Transaction decisions  
• Policy rules  
• Priority recovery actions  

Try asking:

**"Which failure reason has the highest revenue risk?"**

or

**"Which transaction should I prioritize?"**
"""
                )

    st.divider()

    # =====================================================
    # SUGGESTED QUESTIONS
    # =====================================================

    st.subheader("💡 Suggested Questions")

    s1, s2 = st.columns(2)

    with s1:

        st.markdown(
            """
**📊 Revenue Analysis**

- Which failure reason has the highest revenue risk?
- What is my recovery opportunity?
- Which transaction should I prioritize?
"""
        )

    with s2:

        st.markdown(
            """
**🛡️ Decision Analysis**

- Why was TXN-10482 blocked?
- What does the policy engine do?
- What action is recommended for TXN-10481?
"""
        )

    st.divider()

    st.info(
        "Recover AI turns transaction data into explainable "
        "recovery decisions — without performing real payment actions."
    )

   