def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
    
# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder 

# - unless the year is also divisible by 400 with no remainder  

