import datetime

days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

year = 1992
if year % 4 == 0:
    extra_date = datetime.datetime.strptime('29-02-{}'.format(year), '%d-%m-%Y')
    day = extra_date.weekday()
    print(days[day])
else:
    rem = year % 4
    preceding_year = year - rem
    succeeding_year = year + (4 - rem)
    pextra_date = datetime.datetime.strptime('29-02-{}'.format(preceding_year), '%d-%m-%Y')
    pday = pextra_date.weekday()
    print(days[pday])
    sextra_date = datetime.datetime.strptime('29-02-{}'.format(succeeding_year), '%d-%m-%Y')
    sday = sextra_date.weekday()
    print(days[sday])
