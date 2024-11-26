def sip_calculator():
    print("SIP Calculator")
    
    # Taking inputs from the user
    monthly_investment = float(input("Enter your monthly investment amount (in ₹): "))
    annual_return_rate = float(input("Enter the expected annual return rate (in %): "))
    time_period_years = int(input("Enter the time period (in years): "))
    
    # Converting annual return rate to monthly return rate
    monthly_return_rate = annual_return_rate / 12 / 100
    
    # Converting time period in years to months
    total_months = time_period_years * 12
    
    # Calculating final amount using the formula
    future_value = monthly_investment * (((1 + monthly_return_rate) ** total_months - 1) / monthly_return_rate) * (1 + monthly_return_rate)
    
    # Displaying the result
    print(f"\nTotal Investment: ₹{monthly_investment * total_months:,.2f}")
    print(f"Expected Future Value: ₹{future_value:,.2f}")

# Running the calculator
sip_calculator()
