
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
month, day, year = '8', '5', '2015'
mes_dia_ano_split = month, day, year.split(',')
num_dia_da_semana = calendar.weekday(year, month, day)
dias_da_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thirsday', 'Friday', 'Saturday', 'Sunday']
weekday_result = dias_da_semana[num_dia_da_semana]

print(weekday_result)

