def calculate_savings(salary, expenses):
    savings = salary - expenses

    if salary > 0:
        savings_percent = (savings / salary) * 100
    else:
        savings_percent = 0

    return savings, savings_percent