years = [1900,1950,1999,2000,2001,2012,2021]

for year in years:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not a leap year")

