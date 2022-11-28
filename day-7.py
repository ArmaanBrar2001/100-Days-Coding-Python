year = int(input('Enter the year: '))
month = input('Enter the month: ')

months_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
months_30 = ['April', 'June', 'September', 'November']

if month in months_31:
    print('31')
if month in months_30:
    print('30')
if month == 'February':
    if year % 4 == 0 and year % 100 != 0:
        print('29')
    elif year % 400 == 0:
        print('29')
    else:
        print('28')
