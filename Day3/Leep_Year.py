year = int(input('Enter Year to find this year is leep Year or NoT : '))

if year%4==0:
    print('This year is Leep Year...')
elif year%100==0:
    print('This year is Leep Year...')
elif year%400==0:
    print('This year is Leep Year...')
else :
    print('This year is Not Leep Year')