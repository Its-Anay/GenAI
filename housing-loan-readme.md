# Housing Loan Model

This project implements a Python-based housing loan model that calculates EMI (Equated Monthly Installment), generates amortization schedules, and visualizes loan repayment details. It also includes functionality to calculate interest lost on early loan closure.

## Features

- Calculate monthly EMI for a given loan amount, interest rate, and loan term
- Generate a complete amortization schedule
- Visualize EMI breakdown with a stacked bar chart
- Calculate interest lost on early loan closure

## Requirements

- Python 3.6+
- NumPy
- Matplotlib

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```
pip install numpy matplotlib
```

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

## Example Output

When you run the script, you'll see:

1. The calculated monthly EMI printed to the console.
2. A stacked bar chart showing the EMI breakdown over the loan term.
3. The total interest lost if closing the loan early and the interest lost per remaining month.

## Customization

You can easily modify the loan parameters in the script to model different scenarios:

- Change the `loan_amount` to model different loan principals.
- Adjust the `annual_interest_rate` to see how interest rates affect the EMI and total interest paid.
- Modify the `loan_term_years` to model shorter or longer loan terms.
- Change the `early_closure_month` to calculate interest lost for different early closure scenarios.

## Contributing

Contributions to improve the model or add new features are welcome. Please feel free to submit a pull request or open an issue to discuss potential changes.

## License

This project is open-source and available under the MIT License.
