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
