# monthinfo

A collection of utility functions for working with a given month.


## Installation

To install MonthInfo, use `pip`:

```
pip install monthinfo
```

### Usage

To use MonthInfo, import the `CurrentMonth` class and call the `new` function, passing in the year, month, and first day of the week as arguments:

```python
from monthinfo import new

current_month = new(2022, 12, 'Sunday')
```

The `CurrentMonth` class provides several methods and properties for accessing and manipulating information about the given month:


- `get.first_week_day`: returns the day of the week of the first day of the month.
- `validate.is_day_in_weekday(day: int, weekday: str) -> bool`: checks if a given day in the month falls on a specific weekday.
- `validate.is_in_first_weekday(day: int, weekday: str) -> bool`: returns True if the specified day is the first weekday of the month, False otherwise.
- `validate.is_weekend(day: int) -> bool`: returns True if the specified day is a weekend day (Saturday or Sunday), False otherwise.
- `get.list_of_weekday(weekday: str) -> list`: returns a list of the days in the month that fall on the specified weekday.
- `get.number_of_weekday(weekday: str) -> int`: returns the number of days in the month that fall on the specified weekday.
- `get.number_of_weekends() -> float`: returns the number of weekend days (Saturday or Sunday) in the month as a float.
- `get.list_of_days`: returns a list of the days in the month as integers.
- `get.list_of_weeks`: returns a list of the weeks in the month, where each element is a list of integers representing the days of the week. Days that are not part of the current month are represented by zeros.
- `get.number_of_days`: returns the number of days in the month.
- `get.number_of_weeks`: returns the number of weeks in the month.
- `get_calendar_indexes_for_this_day(day: int) -> tuple`: returns a tuple containing the index of the week and the index of the day within the week for the specified day.
- `calendar`: returns a list of lists representing the calendar for the month, where each inner list represents a week and contains integers representing the days of the week. Days that are not part of the current month are represented by zeros.

Here is an example of using some of these methods and properties:

```python
# Get the day of the week of the first day of the month
first_week_day = current_month.get.first_week_day
print(f'First week day: {first_week_day}')

# Check if the 15th day of the month falls on a Wednesday
is_wednesday = current_month.validate.is_day_in_weekday(15, 'Wednesday')
print(f'15th day is Wednesday: {is_wednesday}')

# Get the list of Saturdays in the month
saturdays = current_month.get.list_of_weekday('Saturday')
print(f'Saturdays in the month: {saturdays}')

# Get the calendar for the month
calendar = current_month.calendar
print(f'Calendar for the month: {calendar}')

# Get the indexes for the 3rd day of the month in the calendar
week_index, day_index = current_month.get_calendar_indexes_for_this_day(3)
print(f'3rd day is in week {week_index + 1}, day {day_index + 1}')
```


You can then use these methods and properties to extract various information about the month, such as the day of the week of the first day of the month, whether a specific day falls on a particular weekday, the list of days in the month that are on a specific weekday, the number of days in the month, the number of weeks in the month, and so on.

