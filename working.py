"""
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure wo
"""



import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if is_correct := re.search( r'^(([0-9][0-2]*):?([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):([0-5][0-9])*) ([A-P]M)$', s ) :
        pieces = is_correct.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12 :
            raise ValueError
        first = new_format(pieces[1],pieces[2],pieces[3])
        second = new_format(pieces[5],pieces[6],pieces[7])
    else:
        raise ValueError
         
    return f'{first} to {second}'
    

def new_format(hour,minute,am_pm) :
    if am_pm == 'PM':
        if hour == '12':
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if hour == '12':
            new_hour = 00
        else:
            new_hour = int(hour)  
    if minute == None:
        new_minute = 00
    else:
        new_minute = int(minute)            

    new_time = f'{new_hour:02}:{new_minute:02}'  
    return new_time                     


if __name__ == "__main__":
    main()