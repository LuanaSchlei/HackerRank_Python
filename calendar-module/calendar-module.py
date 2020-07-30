#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/calendar-module/problem
#
# Title: Calendar Module
#

import calendar

# tells the interpreter to create a text calendar. Start of the month will be Sunday. 
# In Python, you can format the calendar as you can change the day of the month to begin with
# c = calendar.TextCalendar(calendar.SUNDAY)

# Example: We are creating calendar for the year 2025, Month 1 – January
# calendario_por_mes = c.formatmonth(2025, 1)
# print(calendario_por_mes)

mes_dia_ano = map(int, input().split(' '))
formato_mes_dia_ano = str(mes_dia_ano)
dia_da_semana = calendar.weekday(formato_mes_dia_ano)

print(dia_da_semana)