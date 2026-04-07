def dcf_valuation(fcf, growth_rate, discount_rate, terminal_growth, years=5):
    projected_fcf = []

    for i in range(1, years + 1):
        fcf *= (1 + growth_rate)
        projected_fcf.append(fcf / ((1 + discount_rate) ** i))

    terminal_value = (fcf * (1 + terminal_growth)) / (discount_rate - terminal_growth)
    terminal_value_discounted = terminal_value / ((1 + discount_rate) ** years)

    return sum(projected_fcf) + terminal_value_discounted