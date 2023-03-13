import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",  "Sunday"]
        return weekday[calendar.weekday(year, month, day)]
