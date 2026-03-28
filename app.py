import streamlit as st

from agents.profile_agent import calculate_savings
from agents.risk_agent import calculate_score
from agents.investment_agent import suggest_sip
from agents.suggestion_agent import generate_advice

st.title("FinMate AI 💰")
st.write("Your Personal Money Mentor")

st.header("Enter Your Details")

age = st.number_input("Enter your Age", min_value=18, max_value=100)
salary = st.number_input("Monthly Salary (₹)", min_value=0)
expenses = st.number_input("Monthly Expenses (₹)", min_value=0)

if st.button("Analyze"):
    st.success("Analysis Result")

    savings, savings_percent = calculate_savings(salary, expenses)
    score = calculate_score(savings_percent)
    sip = suggest_sip(savings)
    advice_list = generate_advice(score, expenses, salary, savings)

    st.subheader("📊 Financial Summary")
    st.write(f"Monthly Savings: ₹{savings}")
    st.write(f"Savings %: {savings_percent:.2f}%")

    st.subheader("💯 Money Health Score")
    st.success(f"Your Score: {score} / 100")

    st.subheader("💡 SIP Recommendation")
    st.write(f"Invest ₹{int(sip)} per month")

    st.subheader("🤖 AI Financial Advice")
    for adv in advice_list:
        st.write(adv)