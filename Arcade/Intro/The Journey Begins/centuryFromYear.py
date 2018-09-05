# Given a year, return the century it is in. 
# The first century spans from the year 1 up to and including the year 100, 
# the second - from the year 101 up to and including the year 200, etc.


#     For year = 1905, the output should be
#     centuryFromYear(year) = 20;
#     For year = 1700, the output should be
#     centuryFromYear(year) = 17.


def centuryFromYear(year):

    century = year / 100
    if (century < 1):
        return 1
    round = int(century)
    
    remainder = century - round
    
    if (remainder > 0):
        return round + 1
    else:
        return round
