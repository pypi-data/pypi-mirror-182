import calendar
from dataclasses import dataclass
import datetime
from enum import Enum
from tkinter import Y


class Week:
    first_day = calendar.MONDAY
    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
            3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

    @classmethod
    def inverted_days(cls) -> dict:
        return {value: key for key, value in cls.days.items()}


@dataclass()
class Month:
    year: int
    month_number: int


@dataclass()
class Validators:
    month: Month

    def is_day_in_weekday(self, day: int, weekday: str) -> bool:
        """
        Check if a given day in a month falls on a specific weekday.

        Parameters:
            day (int): The day of the month.
            weekday (str): The name of the weekday (e.g., 'Monday', 'Tuesday').

        Returns:
            bool: True if the day falls on the given weekday, False otherwise.
        """
        return datetime.date(self.month.year, self.month.month_number, day).weekday() == Week.inverted_days()[weekday.capitalize()]

    def is_in_first_weekday(self, day: int, weekday: str) -> bool:
        """
        Returns True if the specified day is the first Weekday of the month, False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is the first Weekday of the month.
        """
        return self.is_day_in_weekday(day, weekday) and day < 8

    def is_weekend(self, day) -> bool:
        """
        Returns True if the specified day is a weekend day (Saturday or Sunday), False otherwise.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A boolean indicating whether the specified day is a weekend day.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        return datetime.date(self.month.year, self.month.month_number, day).weekday() >= 5


@dataclass()
class Retrievers:
    month: Month
    validator: Validators

    @property
    def list_of_days(self) -> list:
        """
        Returns a list of the days in the current month.

        The list contains integers representing the days of the month, starting from 1.

        Returns:
            A list of integers representing the days of the month.
        """
        return list(range(1, calendar.monthrange(self.month.year, self.month.month_number)[1]+1))

    @property
    def list_of_weeks(self) -> list:
        """
        Returns a list of the weeks in the current month.

        Each element of the list is a list of integers representing the days of the Week.
        Days that are not part of the current month are represented by zeros.

        Returns:
            A list of lists containing integers representing the days of the month.
        """
        return list(calendar.monthcalendar(self.month.year, self.month.month_number))

    @property
    def number_of_weeks(self) -> int:
        """
        Returns the number of weeks in the current month.

        Returns:
            An integer representing the number of weeks in the current month.
        """
        return len(calendar.monthcalendar(self.month.year, self.month.month_number))

    @property
    def number_of_days(self) -> int:
        """
        Returns the number of days in the current month.

        Returns:
            An integer representing the number of days in the current month.
        """
        return calendar.monthrange(self.month.year, self.month.month_number)[1]

    @property
    def first_week_day(self) -> str:
        """
        Returns the day of the week of the first day of the current month.

        Returns:
            A string representing the day of the week (e.g. "Monday").
        """
        return Week.days[datetime.date(self.month.year, self.month.month_number, 1).weekday()]


    def list_of_weekday(self, weekday: str) -> list:
        """
        Returns a list of days in the current month that are given weekday.

        Returns:
            A list of integers representing the days of the month that are weekday.

        Example:
            If the current month is December 2022, the method would return [5, 12, 19, 26] for Mondays.
        """
        return [day for day in self.list_of_days if self.validator.is_day_in_weekday(day, weekday)]

    def number_of_weekday(self, weekday: str) -> int:
        """
        Returns the number of weekday in the current month.

        Returns:
            An integer representing the number of weekday in the current month.
        """
        return len(self.list_of_weekday(weekday))

    @property
    def number_of_weekends(self) -> float:
        """
        Returns the number of weekend days (Saturdays and Sundays) in the current month.

        The number of weekend days is calculated as the maximum number of Saturdays or Sundays in the month.

        Returns:
            An float representing the number of weekend days in the current month.
        """
        return (self.number_of_weekday("saturday") + self.number_of_weekday("sunday")) * 0.5


    def number_of_weekdays(self) -> int:
        """
        Returns the number of weekdays in the current month.

        This method returns the number of weekdays in the current month, by calling the
        `number_of_sundays` and `number_of_mondays` methods.

        Returns:
            The number of weekdays in the current month.
        """
        return self.number_of_days - (self.number_of_weekday("saturday") + self.number_of_weekday("sundays"))



@dataclass()
class CurrentMonth:
    year: int
    month: int
    validate: Validators
    get: Retrievers

    @property
    def calendar(self):
        """
        Returns a matrix representing a month's calendar.

        Each row represents a week, and each column represents a day of the Week.
        Days that are not part of the current month are represented by zeros.

        Returns:
            A list of lists containing integers representing the days of the month.
        """
        return calendar.monthcalendar(self.year, self.month)

    def get_calendar_indexes_for_this_day(self, day):
        """
        Returns the indexes of the specified day in the month's calendar.

        The first index represents the week number (starting from 0), and the second
        index represents the day of the week (starting from 0). Days that are not
        part of the current month are represented by zeros in the calendar.

        Args:
            day: An integer representing the day of the month (1-31).

        Returns:
            A tuple containing two integers representing the indexes of the specified
            day in the month's calendar.

        Raises:
            ValueError: If the specified day is not in the current month.
        """
        for i, week in enumerate(self.calendar):
            for j, d in enumerate(week):
                if d == day:
                    return i, j


def setfirstweekday(first_week_day: str):
    Week.first_day = Week.inverted_days()[first_week_day.capitalize()]
    calendar.setfirstweekday(Week.first_day)


def new(year: int, month: int, first_week_day: str) -> CurrentMonth:
    first_week_day = first_week_day
    setfirstweekday(first_week_day.capitalize())
    m = Month(year=year, month_number=month)
    v = Validators(m)
    g = Retrievers(m, v)
    return CurrentMonth(year, month, v, g)

