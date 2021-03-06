from infrastructure.string_service import StringService as _string
from infrastructure.date_service   import DateService   as _date

class PeriodHour:
    def __init__(self, schedule):
        self.schedule = schedule

    def getFormula(self):
        return (self.getMinutes()      + ' ' + 
                self.getHours()        + ' ' +
                self.getDaysOfMonth()  + ' ' +
                self.getMonths()       + ' ' +
                self.getDaysOfWeek() )

    def getMinutes(self):
        return self.schedule.startMinute

    def getHours(self):
        hours = self.schedule.frequency
        
        if self.divisible_by_hours_in_day( int(hours) ):
            hours = self.calculate_hours ( int(hours) )
            hours = _string.replace_values_from_task( hours, '24', '0' )
            hours = _string.removeCommaFromLastChar ( hours )
            return hours

        hours = '*/' + self.schedule.frequency
        return hours

    def getDaysOfMonth(self):
        return '*'

    def getMonths(self):
        return '*'

    def getDaysOfWeek(self):
        days = self.schedule.runDaysOfWeek
        if _string.isEmpty( days ):
            return '*'

        days = _date.decrease_1_day_to_match_crontab( days )
        days = _string.removeCommaFromLastChar( days )
        return days

    @staticmethod
    def divisible_by_hours_in_day(hours):
        hours_in_day = 24
        return hours_in_day % int(hours) == 0

    @staticmethod
    def calculate_hours( frequency ):
        hours_in_day = 24
        hours_count = frequency
        result = str(frequency) + ','

        while 1 == 1:
            hours_count += frequency
            if hours_count > hours_in_day:
                break
            result += str(hours_count) + ','

        return result