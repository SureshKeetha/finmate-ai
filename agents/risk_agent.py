def calculate_score(savings_percent):
    if savings_percent > 40:
        return 95
    elif savings_percent > 20:
        return 80
    elif savings_percent > 10:
        return 60
    else:
        return 40