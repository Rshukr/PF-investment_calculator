def accrued_amount(principal_amount, annual_return_rate, years):
    p = principal_amount
    r = annual_return_rate / 100
    n = 12  # number of compounding per t; Months
    t = years

    return p * (1 + r / n) ** (n * t)

def principal_amount_given_target(target_amount, annual_return_rate, years):
    target = target_amount
    r = annual_return_rate / 100
    n = 12  # number of compounding per t; Months
    t = years

    return target / ((1 + r / n) ** (n * t))