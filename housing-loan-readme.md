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
import numpy as np
import matplotlib.pyplot as plt

class HousingLoan:
    def __init__(self, principal, annual_interest_rate, loan_term_years):
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_years = loan_term_years
        self.monthly_interest_rate = annual_interest_rate / 12 / 100
        self.total_payments = loan_term_years * 12
        self.emi = self.calculate_emi()

    def calculate_emi(self):
        emi = (self.principal * self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.total_payments) / \
              ((1 + self.monthly_interest_rate) ** self.total_payments - 1)
        return emi

    def generate_amortization_schedule(self):
        balance = self.principal
        schedule = []
        for month in range(1, self.total_payments + 1):
            interest = balance * self.monthly_interest_rate
            principal = self.emi - interest
            balance -= principal
            schedule.append((month, self.emi, principal, interest, balance))
        return schedule

    def calculate_interest_lost_on_early_closure(self, closure_month):
        schedule = self.generate_amortization_schedule()
        total_interest = sum(payment[3] for payment in schedule[closure_month:])
        remaining_months = self.total_payments - closure_month
        return total_interest, remaining_months

    def plot_emi_chart(self):
        schedule = self.generate_amortization_schedule()
        months = [payment[0] for payment in schedule]
        principal_payments = [payment[2] for payment in schedule]
        interest_payments = [payment[3] for payment in schedule]

        plt.figure(figsize=(12, 6))
        plt.bar(months, principal_payments, label='Principal')
        plt.bar(months, interest_payments, bottom=principal_payments, label='Interest')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.title(f'EMI Breakdown (Principal: {self.principal}, Rate: {self.annual_interest_rate}%, Term: {self.loan_term_years} years)')
        plt.legend()
        plt.tight_layout()
        plt.show()

# Example usage
loan_amount = 300000
annual_interest_rate = 7.5
loan_term_years = 20

loan = HousingLoan(loan_amount, annual_interest_rate, loan_term_years)
print(f"Monthly EMI: ${loan.emi:.2f}")

# Plot EMI chart
loan.plot_emi_chart()

# Calculate interest lost on early closure
early_closure_month = 60  # Closing after 5 years
interest_lost, remaining_months = loan.calculate_interest_lost_on_early_closure(early_closure_month)
print(f"\nInterest lost on early closure after {early_closure_month} months: ${interest_lost:.2f}")
print(f"Interest lost per remaining month: ${interest_lost / remaining_months:.2f}")

```
## Example Output

When you run the script, you'll see:
![Screenshot 2024-09-21 224812](https://github.com/user-attachments/assets/66c51676-41e6-466f-ac7a-ff09a2a2f3a6)


1. The calculated monthly EMI printed to the console.
2. A stacked bar chart showing the EMI breakdown over the loan term.
3. The total interest lost if closing the loan early and the interest lost per remaining month.

## Customization

You can easily modify the loan parameters in the script to model different scenarios:

- Change the `loan_amount` to model different loan principals.
- Adjust the `annual_interest_rate` to see how interest rates affect the EMI and total interest paid.
- Modify the `loan_term_years` to model shorter or longer loan terms.
- Change the `early_closure_month` to calculate interest lost for different early closure scenarios.


