def compound_interest(principal, rate, time, compounds_per_year):
    # Convert rate to decimal
    rate_decimal = rate / 100
    
    # Calculate the compound interest
    amount = principal * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * time)
    
    # Calculate the interest earned
    interest = amount - principal
    
    return amount, interest

# Example usage
principal_amount = 1000  # Principal amount
annual_interest_rate = 5  # Annual interest rate (in percentage)
time_period_years = 3     # Time period in years
compounds_per_year = 12   # Number of times interest is compounded per year

amount_accumulated, interest_earned = compound_interest(principal_amount, annual_interest_rate, time_period_years, compounds_per_year)
print("Amount accumulated after {} years: ${:.2f}".format(time_period_years, amount_accumulated))
print("Interest earned: ${:.2f}".format(interest_earned))
