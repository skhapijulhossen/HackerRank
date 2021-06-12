def dayOfProgrammer(year):
        if year == 1918:
            return '26.09.1918'
        elif ((year <= 1917) & (year % 4 == 0)) or ((year % 400 == 0) or ((year % 4 == 0) & (year % 100 != 0))):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'