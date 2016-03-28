#Calculate Coptic Easter based on information from http://www.copticchurch.net/topics/coptic_calendar/ortheast.html

from datetime import *
from datetime import timedelta

year = 2016


def rmd(x, y):
    ''' calculate remainder'''
    return x % y


def calc_coptic_easter(year):
    year2 = str(year)  # convert to string
    year3 = year2[-2:]  # last 2 digits
    vernaleq_date = '03/21/' + year3  # make the equinox date
    date_1 = datetime.strptime(vernaleq_date, "%m/%d/%y")
    R1 = rmd(year, 19)
    R2 = rmd(year, 4)
    R3 = rmd(year, 7)
    RA = 19 * R1 + 16
    R4 = rmd(RA, 30)
    RB = 2 * R2 + 4 * R3 + 6 * R4
    R5 = rmd(RB, 7)
    RC = R4 + R5
    end_date = date_1 + timedelta(days=RC + 13)  # add 13 days to compensate for julian calendar
    print "Year is ", year, " And easter is on ", end_date


for x in range(2016, 2100):
    calc_coptic_easter(x)
