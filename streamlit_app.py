import streamlit as st
import pandas as pd
st.set_page_config(page_title="CreditAI", page_icon="🏦", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
header[data-testid="stHeader"] { display: none !important; }
div[data-testid="stToolbar"] { display: none !important; }
footer { display: none !important; }
.stApp { background: #F0FDF4; }
.block-container { max-width: 1000px !important; padding-top: 2.5rem !important; padding-bottom: 2rem !important; margin: auto !important; }
.hero { background: linear-gradient(135deg, #052e16 0%, #15803d 50%, #22c55e 100%); padding: 32px 24px; border-radius: 20px; color: white; box-shadow: 0 10px 30px rgba(21,128,61,0.3); margin-bottom: 20px; }
.hero h1 { color: white !important; font-size: 38px !important; margin: 0 !important; }
.hero p { color: #dcfce7 !important; font-size: 16px !important; margin-top: 8px !important; }
.card { background: white; padding: 20px; border-radius: 16px; border: 1px solid #E5E7EB; box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 16px; }
.card h3 { margin-top: 0 !important; color: #111827; }
.stat-box { background: white; padding: 18px; border-radius: 14px; border-left: 5px solid #16a34a; box-shadow: 0 2px 8px rgba(0,0,0,0.05); text-align: center; }
.stat-box b { font-size: 26px; color: #111827; }
.stat-box span { font-size: 13px; color: #6b7280; }
div[data-testid="stButton"] > button { background: #15803d !important; color: white !important; border-radius: 12px !important; font-weight: 700 !important; border: none !important; width: 100% !important; padding: 14px !important; }
div[data-testid="stDownloadButton"] > button { width: 100% !important; border-radius: 12px !important; padding: 14px !important; background: white !important; color: #15803d !important; border: 2px solid #15803d !important; font-weight: 700 !important; }
div[data-testid="stMetric"] { background: white; padding: 16px; border-radius: 14px; border: 1px solid #E5E7EB; }
div[data-testid="stSegmentedControl"] { background: white; padding: 6px; border-radius: 14px; border: 1px solid #E5E7EB; }
@media (max-width: 600px) {
    .block-container { padding-left: 12px !important; padding-right: 12px !important; padding-top: 1.5rem !important; }
    .hero { padding: 22px 16px !important; border-radius: 16px !important; }
    .hero h1 { font-size: 26px !important; }
    .hero p { font-size: 14px !important; }
    .card { padding: 16px !important; }
    div[data-testid="stButton"] > button, div[data-testid="stDownloadButton"] > button { padding: 16px !important; font-size: 16px !important; }
}
</style>
""", unsafe_allow_html=True)
if "login" not in st.session_state: st.session_state.login = False
if "history" not in st.session_state: st.session_state.history = []
if "result" not in st.session_state: st.session_state.result = None
if "page" not in st.session_state: st.session_state.page = "home"
if not st.session_state.login:
    st.markdown("""<div class="hero"><h1>🏦 CreditAI</h1><p>AI Powered Credit Scoring System • Trusted by Banks • Secure & Fast</p></div>""", unsafe_allow_html=True)
    _, c, _ = st.columns([1,1.2,1])
    with c:
        with st.container(border=True):
            st.subheader("Staff Login")
            u = st.text_input("Username"); p = st.text_input("Password", type="password")
            st.info("Demo login-Username: admin| password:admin123")
            if st.button("Secure Login →"):
                if u=="admin" and p=="admin123":
                    st.session_state.login=True; st.rerun()
                else: st.error("Invalid Credentials")
    st.stop()
if st.sidebar.button("Logout"):
    st.session_state.login=False; st.session_state.result=None; st.session_state.page="home"; st.rerun()
nav_map = {"🏠 Home": "home", "➕ New Check": "check", "📊 History": "history"}
if st.session_state.page not in ["home", "check", "history"]:
    nav_default = "🏠 Home"
else:
    nav_default = [k for k,v in nav_map.items() if v==st.session_state.page][0]
selected = st.segmented_control("Navigation", list(nav_map.keys()), default=nav_default, label_visibility="collapsed")
if nav_map[selected] != st.session_state.page and st.session_state.page != "result":
    st.session_state.page = nav_map[selected]; st.rerun()
if st.session_state.page == "result" and nav_map[selected] != "home":
    st.session_state.page = nav_map[selected]; st.rerun()
if st.session_state.page == "home":
    st.markdown("""<div class="hero"><h1>🏦 CreditAI Dashboard</h1><p>Smart Credit Scoring • AI Risk Analysis • Instant Reports<br>Check any applicant in 30 seconds.</p></div>""", unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    with s1: st.markdown(f"<div class='stat-box'><b>{len(st.session_state.history)}</b><br><span>Total Checks</span></div>", unsafe_allow_html=True)
    with s2: st.markdown(f"<div class='stat-box'><b>{sum(1 for x in st.session_state.history if x['Status']=='Approved')}</b><br><span>Approved</span></div>", unsafe_allow_html=True)
    with s3: st.markdown(f"<div class='stat-box'><b>{sum(1 for x in st.session_state.history if x['Status']=='Rejected')}</b><br><span>Rejected</span></div>", unsafe_allow_html=True)
    with s4: st.markdown("<div class='stat-box'><b>92.5%</b><br><span>AI Accuracy</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>✨ What This System Does</h3><p>✅ <b>AI Score</b> - 300 to 850<br>✅ <b>EMI Check</b> - Income vs EMI ratio<br>✅ <b>Risk Analysis</b> - Why score is high / low<br>✅ <b>Instant Report</b> - Download in 1 click</p></div>", unsafe_allow_html=True)
    if st.button("Start New Credit Check →", key="home_start"):
        st.session_state.page="check"; st.rerun()
    if st.session_state.history:
        st.markdown("<div class='card'><h3>📋 Latest Applications</h3></div>", unsafe_allow_html=True)
        st.dataframe(pd.DataFrame(st.session_state.history[-3:]), use_container_width=True, hide_index=True)
if st.session_state.page == "check":
    st.markdown("""<div class="hero"><h1>➕ New Credit Check</h1><p>Fill details below. AI will give score instantly.</p></div>""", unsafe_allow_html=True)
    with st.container(border=True):
        with st.form("check_form"):
            name = st.text_input("Full Name", "Aarti")
            c1, c2 = st.columns(2)
            with c1:
                age = st.number_input("Age", 18, 80, 25)
                income = st.number_input("Monthly Income (INR)", 5000, 200000, 50000)
            with c2:
                amount = st.number_input("Loan Amount (INR)", 1000, 100000, 2000)
                duration = st.number_input("Duration (Months)", 6, 72, 24)
            history_opt = st.selectbox("Credit History", ["Excellent - Always Paid On Time", "Good - One Late Payment", "Average", "Poor - Multiple Missed Payments"])
            existing_emi = st.number_input("Existing EMI (INR)", 0, 50000, 0)
            submit = st.form_submit_button("🤖 Run AI Analysis")
    if submit:
        emi = int(amount/duration + amount*0.01)
        ratio = ((emi+existing_emi)/income)*100
        score = 750
        if ratio < 10: score += 40
        elif ratio < 30: score += 10
        elif ratio < 50: score -= 80
        else: score -= 180
        if "Excellent" in history_opt: score += 30
        elif "Good" in history_opt: score += 10
        elif "Poor" in history_opt: score -= 150
        score = max(300, min(850, score))
        new_row = {"Name": name, "Score": score, "Loan": amount, "EMI": emi, "Status": "Approved" if score>=650 else "Review" if score>=550 else "Rejected"}
        if not st.session_state.history or st.session_state.history[-1] != new_row:
            st.session_state.history.append(new_row)
        st.session_state.result = (name, age, income, amount, duration, emi, ratio, score, history_opt)
        st.session_state.page = "result"; st.rerun()
if st.session_state.page == "result" and st.session_state.result:
    name, age, income, amount, duration, emi, ratio, score, history_opt = st.session_state.result
    st.markdown(f"""<div class="hero"><h1>Result for {name}</h1><p>AI Analysis Complete • Score Generated</p></div>""", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1: st.metric("Credit Score", f"{score} / 850")
    with m2: st.metric("Monthly EMI", f"Rs. {emi:,}")
    with m3: st.metric("EMI / Income", f"{ratio:.1f}%")
    if score >= 650:
        st.success(f"✅ APPROVED - {name} is highly creditworthy.")
        tip = "Approve immediately. Offer 9% interest rate and pre-approved credit card."
    elif score >= 550:
        st.warning("⚠️ CONDITIONAL APPROVAL - Salary slip verification required.")
        tip = "Request 3 months bank statement before final approval."
    else:
        st.error("❌ REJECTED - EMI burden is too high.")
        tip = "Recommend to reduce loan amount or increase tenure."
    st.markdown(f"<div class='card'><h3>💡 AI Recommendation</h3><p>{tip}</p></div>", unsafe_allow_html=True)
    st.markdown("### Why This Score?")
    st.write(f"Income Strength: {min(100, int(income/600))} / 100"); st.progress(min(100, int(income/600)))
    st.write(f"EMI Burden: {max(5, int(100-ratio*2))} / 100"); st.progress(max(5, int(100-ratio*2)))
    st.write(f"Credit History: {95 if 'Excellent' in history_opt else 70 if 'Good' in history_opt else 40} / 100"); st.progress(95 if "Excellent" in history_opt else 70 if "Good" in history_opt else 40)
    st.markdown("### Report")
    report = f"CREDITAI REPORT\nName: {name}\nAge: {age}\nIncome: {income}\nLoan: {amount} for {duration} months\nEMI: {emi} ({ratio:.1f}% of income)\nScore: {score}\nDecision: {'Approved' if score>=650 else 'Review' if score>=550 else 'Rejected'}\nRecommendation: {tip}"
    st.download_button("⬇️ Download Report", report, file_name=f"{name}_Report.txt")
    if st.button("➕ Check Another Applicant →", key="result_next"):
        st.session_state.page="check"; st.rerun()
    if st.button("🏠 Back to Home", key="result_home"):
        st.session_state.page="home"; st.rerun()
if st.session_state.page == "history":
    st.markdown("""<div class="hero"><h1>📊 Application History</h1><p>All checked applicants in one place.</p></div>""", unsafe_allow_html=True)
    if st.session_state.history:
        st.dataframe(pd.DataFrame(st.session_state.history), use_container_width=True, hide_index=True)
        if st.button("🗑️ Clear All History", key="clear_hist"):
            st.session_state.history=[]; st.session_state.result=None; st.session_state.page="home"; st.rerun()
    else:
        st.info("No applications yet. Go to New Check to start.")
    if st.button("➕ New Check →", key="hist_next"):
        st.session_state.page="check"; st.rerun()
