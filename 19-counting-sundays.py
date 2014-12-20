from datetime import date

current_date = date(1901, 1, 1)
last_date = date(2000, 12, 31)
sundays = 0

while current_date <= last_date:
    if current_date.weekday() == 6:
        sundays +=1
    
    month = current_date.month + 1
    year = current_date.year
    
    if month == 13:
        month = 1
        year = current_date.year + 1
        
    current_date = date(year, month, 1)

print sundays