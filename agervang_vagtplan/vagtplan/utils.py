from calendar import HTMLCalendar
from datetime import datetime
from .models import vagt



 
class calendarMonth():
    today = datetime.today()
    year = today.year
    month = today.month 

    def cMonth(self, year=year, month=month): 
        tc = calendar.HTMLCalendar(firstweekday=0)
        return tc.formatmonth(year, month, withyear = True)

