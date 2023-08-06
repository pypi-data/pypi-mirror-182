import unittest
import calendar

from monthinfo import monthinfo



class Test_Week(unittest.TestCase):
    def test_setfirstweekday(self):
        monthinfo.setfirstweekday("tuesday")
        self.assertEqual(monthinfo.Week.first_day, 1)
        monthinfo.setfirstweekday("Friday")
        self.assertEqual(monthinfo.Week.first_day, 4)


class Test_CurrentMonth(unittest.TestCase):
    def setUp(self) -> None:
        self.calendar = monthinfo.new(2022, 12, "saturday")

    def test_new(self):
        self.assertEqual(self.calendar.month, 12)

    def test_first_week_day(self) -> str:
        self.assertEqual(self.calendar.get.first_week_day, "Thursday")

    def test_is_day_in_weekday(self):
        self.assertTrue(self.calendar.validate.is_day_in_weekday(3, "Saturday"))
        self.assertFalse(
            self.calendar.validate.is_day_in_weekday(5, "Saturday"))

    def test_is_in_first_weekday(self):
        self.assertTrue(self.calendar.validate.is_in_first_weekday(3, "Saturday"))

    def test_list_of_weekday(self):
        self.assertEqual(self.calendar.get.list_of_weekday(
            "saturday"), [3, 10, 17, 24, 31])

    def test_number_of_weekday(self):
        self.assertEqual(self.calendar.get.number_of_weekday("saturday"), 5)
        self.assertEqual(self.calendar.get.number_of_weekday("monday"), 4)

    def test_number_of_weekends(self):
        self.assertEqual(self.calendar.get.number_of_weekends, 4.5)


    def test_is_weekend(self):
        self.assertTrue(self.calendar.validate.is_weekend(3))
        self.assertFalse(self.calendar.validate.is_weekend(2))

    def test_list_of_days(self):
        self.assertEqual(self.calendar.get.list_of_days[0], 1)
        self.assertEqual(self.calendar.get.list_of_days[29], 30)

    def test_list_of_weeks(self):
        self.assertEqual(self.calendar.get.list_of_weeks[0], [0, 0, 0, 0, 0, 1, 2])
        self.assertEqual(self.calendar.get.list_of_weeks[
                         1], [3, 4, 5, 6, 7, 8, 9])

    def test_calendar(self):
        self.assertEqual(self.calendar.calendar[0][6], 2)

    def test_number_of_days(self):
        self.assertEqual(self.calendar.get.number_of_days, 31)

    def test_number_of_weeks(self):
        self.assertEqual(self.calendar.get.number_of_weeks, 6)

    def test_get_calendar_indexes_for_this_day(self):
        week, day = self.calendar.get_calendar_indexes_for_this_day(1)
        self.assertEqual(week, 0)
        self.assertEqual(day, 5)
        self.assertEqual(self.calendar.calendar[week][day], 1)
