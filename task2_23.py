def is_visokos(year): 
    if year % 4 == 0:
        print (str(year) +'год - високосный.')
    else: 
        print (str(year) +' год - не високосный.')
which_year = int(input('Which year?'))
is_visokos(which_year)