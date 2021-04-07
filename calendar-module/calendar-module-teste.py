#!/bin/python3

#
# Url: https://www.hackerrank.com/challenges/calendar-module/problem
#
# Title: Calendar Module
#
# Arquivo de Teste
#

import calendar

# mes_dia_ano = map(int, input().split(' '))
inputValue = '12 25 2059'
mes_dia_ano = list(map(int, inputValue.split(' ')))
month, day, year = mes_dia_ano[0], mes_dia_ano[1], mes_dia_ano[2]

num_dia_da_semana = calendar.weekday(year, month, day)
#dias_da_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_result = calendar.day_name[num_dia_da_semana]
weekday_upper = weekday_result.upper()

print(weekday_upper)

print(calendar.day_name[0])