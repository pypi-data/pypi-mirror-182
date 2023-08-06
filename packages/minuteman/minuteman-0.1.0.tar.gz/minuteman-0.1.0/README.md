# Minuteman

Represent and transform expressions of time. For example:

- 5 minutes per day in a year in days = 1.27 days.
- 1 hour per day in a decade in weeks = 21,72 weeks
- 10 months a year in 4 decades in years = 33.33 years

### Install

`pip install minuteman`

### Usage

Basic usage: from humanreadable expression to a number
```python
from minuteman.parser import parse

# Case 1: calculation of daily habbit adding up.
expression = "5 minutes a day in 1 year in days" 
result = parse(expression)
print(result) # 1.2673611111111112 days

# Same result with rounding to given decimals.
result = parse(expression, 2)
print(result) # 1.27 days

# Case 2: how many actual years one spends working in 40 year career.
expression = "10 months a year in 4 decades in years"
result = parse(expression, 0) # indicating no decimals.
print(result) # 33 years

```

More fine tune usage: ignoring humanreadable strings and using straight number input
```python
from minuteman.core import transform, TimeExpressionRequest
from minuteman.units import TimeExpression, UnitOfTime

# Build a time expression request from parts

# Case: 8 hours a day in a year in months
request = TimeExpressionRequst(
    original=TimeExpression(
        amount=8,
        unit=UnitOfTime.HOURS,
    ),
    in_time=TimeExpression(amount=1, unit=UnitOfTime.DAYS),
    comparison=TimeExpression(amount=1, unit=UnitOfTime.YEARS),
)
resolution = UnitOfTime.MONTHS

result = transform(request, resolution)

# Result is a TimeExpression instance with amount & unit.
print(result) # TimeExpression(amount=4.055555555555555, unit=UnitOfTime.Months)


```

#### Supported units of time:
- Seconds
- Minutes
- Hours
- Days
- Weeks
- Months
- Years
- Decades
