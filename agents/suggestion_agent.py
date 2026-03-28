def generate_advice(score, expenses, salary, savings):
    advice = []

    # Score-based advice
    if score >= 80:
        advice.append("🚀 Excellent financial health! Increase long-term investments.")
        advice.append("📈 Consider investing in mutual funds for better returns.")
    elif score >= 60:
        advice.append("👍 You are doing okay. Try to increase your savings.")
        advice.append("💡 Reduce unnecessary expenses like subscriptions.")
    else:
        advice.append("⚠️ Financial risk detected. Focus on saving first.")
        advice.append("❌ Avoid risky investments for now.")

    # Savings advice
    if savings < 5000:
        advice.append("💰 Build an emergency fund of at least ₹50,000.")
    else:
        advice.append("✅ Good savings habit. Maintain consistency.")

    # Expense advice
    if expenses > salary * 0.7:
        advice.append("⚠️ High spending detected. Cut down unnecessary costs.")
    else:
        advice.append("✅ Your expenses are under control.")

    return advice