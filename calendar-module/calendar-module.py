#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/calendar-module/problem
#
# Title: Calendar Module
#


# tells the interpreter to create a text calendar. Start of the month will be Sunday. 
# In Python, you can format the calendar as you can change the day of the month to begin with
# c = calendar.TextCalendar(calendar.SUNDAY)

# Example: We are creating calendar for the year 2025, Month 1 – January
# calendario_por_mes = c.formatmonth(2025, 1)
# print(calendario_por_mes)

import calendar

inputValue = map(int, input().split(' '))
mes_dia_ano = list(inputValue)
month, day, year = mes_dia_ano[0], mes_dia_ano[1], mes_dia_ano[2]

num_dia_da_semana = calendar.weekday(year, month, day)
dias_da_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thirsday', 'Friday', 'Saturday', 'Sunday']
weekday_result = dias_da_semana[num_dia_da_semana]
weekday_upper = weekday_result.upper()

print(weekday_upper)