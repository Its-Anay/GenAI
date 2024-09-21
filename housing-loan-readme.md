# Housing Loan Model

This project implements a Python-based housing loan model that calculates EMI (Equated Monthly Installment), generates amortization schedules, and visualizes loan repayment details. It also includes functionality to calculate interest lost on early loan closure.

## Features

- Calculate monthly EMI for a given loan amount, interest rate, and loan term
- Generate a complete amortization schedule
- Visualize EMI breakdown with a stacked bar chart
- Calculate interest lost on early loan closure
  

## Usage

1. Import the `HousingLoan` class from the main script:

```python
from housing_loan_model import HousingLoan
```

2. Create a loan object with your desired parameters:

```python
loan_amount = 300000
annual_interest_rate = 7.5
loan_term_years = 20

loan = HousingLoan(loan_amount, annual_interest_rate, loan_term_years)
```

3. Calculate and display the monthly EMI:

```python
print(f"Monthly EMI: ${loan.emi:.2f}")
```

4. Generate and display the EMI breakdown chart:

```python
loan.plot_emi_chart()
```

5. Calculate interest lost on early closure:

```python
early_closure_month = 60  # Closing after 5 years
interest_lost, remaining_months = loan.calculate_interest_lost_on_early_closure(early_closure_month)
print(f"\nInterest lost on early closure after {early_closure_month} months: ${interest_lost:.2f}")
print(f"Interest lost per remaining month: ${interest_lost / remaining_months:.2f}")
```
## Code
```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class Vehicle:
    def __init__(self, make, model, year, initial_value):
        self.make = make
        self.model = model
        self.year = year
        self.initial_value = initial_value

class InsurancePolicy:
    def __init__(self, vehicle, start_date, base_premium_rate=0.05, depreciation_rate=0.07):
        self.vehicle = vehicle
        self.start_date = start_date
        self.base_premium_rate = base_premium_rate
        self.depreciation_rate = depreciation_rate

    def calculate_current_value(self, current_year):
        years_passed = current_year - self.start_date.year
        depreciation_factor = (1 - self.depreciation_rate) ** years_passed
        return self.vehicle.initial_value * depreciation_factor

    def calculate_premium(self, current_year, frequency='yearly'):
        current_value = self.calculate_current_value(current_year)
        yearly_premium = current_value * self.base_premium_rate

        if frequency == 'yearly':
            return yearly_premium
        elif frequency == 'quarterly':
            return yearly_premium / 4
        elif frequency == 'monthly':
            return yearly_premium / 12
        else:
            raise ValueError("Invalid frequency. Choose 'yearly', 'quarterly', or 'monthly'.")

def generate_premium_chart(policy, years=5):
    data = []
    current_year = policy.start_date.year

    for year in range(years):
        yearly_premium = policy.calculate_premium(current_year + year, 'yearly')
        quarterly_premium = policy.calculate_premium(current_year + year, 'quarterly')
        monthly_premium = policy.calculate_premium(current_year + year, 'monthly')
        vehicle_value = policy.calculate_current_value(current_year + year)

        data.append({
            'Year': current_year + year,
            'Vehicle Value': vehicle_value,
            'Yearly Premium': yearly_premium,
            'Quarterly Premium': quarterly_premium,
            'Monthly Premium': monthly_premium
        })

    return pd.DataFrame(data)

def plot_premium_chart(premium_chart):
    plt.figure(figsize=(12, 8))
    
    plt.plot(premium_chart['Year'], premium_chart['Yearly Premium'], label='Yearly Premium', marker='o')
    plt.plot(premium_chart['Year'], premium_chart['Quarterly Premium'] * 4, label='Quarterly Premium (Annualized)', marker='s')
    plt.plot(premium_chart['Year'], premium_chart['Monthly Premium'] * 12, label='Monthly Premium (Annualized)', marker='^')
    plt.plot(premium_chart['Year'], premium_chart['Vehicle Value'], label='Vehicle Value', linestyle='--', marker='x')
    
    plt.title('Insurance Premiums and Vehicle Value Over Time')
    plt.xlabel('Year')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Example usage
vehicle = Vehicle("Toyota", "Camry", 2022, 25000)
policy = InsurancePolicy(vehicle, datetime(2022, 1, 1))
premium_chart = generate_premium_chart(policy)

print("Premium Chart:")
print(premium_chart.to_string(index=False))

plot_premium_chart(premium_chart)
```
## Example Output

When you run the script, you'll see:
![image](https://github.com/user-attachments/assets/8422939f-d434-4b76-972e-a720d8c71ed5)

1. The calculated monthly EMI printed to the console.
2. A stacked bar chart showing the EMI breakdown over the loan term.
3. The total interest lost if closing the loan early and the interest lost per remaining month.

## Customization

You can easily modify the loan parameters in the script to model different scenarios:

- Change the `loan_amount` to model different loan principals.
- Adjust the `annual_interest_rate` to see how interest rates affect the EMI and total interest paid.
- Modify the `loan_term_years` to model shorter or longer loan terms.
- Change the `early_closure_month` to calculate interest lost for different early closure scenarios.


