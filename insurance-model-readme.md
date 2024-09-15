# Insurance Company Vehicle Model

## Overview

This Python script implements a model for an insurance company to manage vehicle information and calculate insurance premiums over time. The model takes into account vehicle depreciation and allows for flexible premium calculations based on different time intervals (yearly, quarterly, monthly).

## Features

- Vehicle information management
- Insurance policy creation with customizable parameters
- Premium calculation considering vehicle depreciation
- Generation of premium charts over multiple years
- Visualization of premium trends and vehicle value depreciation

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries:

```
pip install pandas matplotlib
```

3. Download the `insurance_model.py` file to your project directory.

## Usage

### Basic Usage

1. Import the necessary classes and functions:

```python
from insurance_model import Vehicle, InsurancePolicy, generate_premium_chart, plot_premium_chart
```

2. Create a vehicle:

```python
vehicle = Vehicle("Toyota", "Camry", 2022, 25000)
```

3. Create an insurance policy:

```python
from datetime import datetime

policy = InsurancePolicy(vehicle, datetime(2022, 1, 1))
```

4. Generate a premium chart:

```python
premium_chart = generate_premium_chart(policy)
```

5. Display the chart data:

```python
print(premium_chart.to_string(index=False))
```

6. Visualize the data:

```python
plot_premium_chart(premium_chart)
```

### Customization

You can customize various parameters when creating an `InsurancePolicy`:

```python
policy = InsurancePolicy(
    vehicle,
    start_date,
    base_premium_rate=0.05,  # 5% of the vehicle's current value
    depreciation_rate=0.07   # 7% annual depreciation
)
```

## Classes and Functions

### Vehicle

Represents a vehicle with its basic information.

Attributes:
- `make`: The manufacturer of the vehicle
- `model`: The model of the vehicle
- `year`: The year the vehicle was manufactured
- `initial_value`: The initial value of the vehicle

### InsurancePolicy

Represents an insurance policy for a vehicle.

Attributes:
- `vehicle`: The insured vehicle
- `start_date`: The start date of the policy
- `base_premium_rate`: The base rate for calculating premiums (default: 5%)
- `depreciation_rate`: The annual depreciation rate of the vehicle (default: 7%)

Methods:
- `calculate_current_value(current_year)`: Calculates the current value of the vehicle
- `calculate_premium(current_year, frequency)`: Calculates the premium for a given year and frequency

### generate_premium_chart(policy, years=5)

Generates a pandas DataFrame containing premium and vehicle value information over a specified number of years.

### plot_premium_chart(premium_chart)

Creates a matplotlib visualization of the premium chart data.

## Example

```python
from insurance_model import Vehicle, InsurancePolicy, generate_premium_chart, plot_premium_chart
from datetime import datetime

# Create a vehicle
vehicle = Vehicle("Toyota", "Camry", 2022, 25000)

# Create an insurance policy
policy = InsurancePolicy(vehicle, datetime(2022, 1, 1))

# Generate premium chart
premium_chart = generate_premium_chart(policy)

# Display chart data
print(premium_chart.to_string(index=False))

# Visualize data
plot_premium_chart(premium_chart)
```

## Extending the Model

You can extend this model by:
1. Adding more attributes to the `Vehicle` class (e.g., mileage, condition)
2. Implementing more complex premium calculation logic in the `InsurancePolicy` class
3. Creating additional visualization functions for different aspects of the data

## License

This project is open-source and available under the MIT License.
