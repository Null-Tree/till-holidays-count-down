from ast import Pass
from datetime import datetime
from threading import current_thread
import tkinter as tk
from datetime import timedelta

def calc():
    term_end = datetime(2022, 4, 8, 15, 20)
    date_end = datetime(2022, 4, 9)
    the_monday_after = datetime(2022, 4, 11)
    total_sessions = 0

    today = datetime.now()
    str_today = str(today) #2022-03-10 10:32:33.559660
    

    diffrence = term_end - today #only for the final string   

    diffrence_to_home = term_end-today #until when school ends at 2.30
    diffrence_uteond = date_end - today #diffrence until 0:00 am the next day

    no__weeks_left = ((the_monday_after - today).days)//7
    remainder_days_not_whole_week = (the_monday_after - today).days - (((the_monday_after - today).days)//7)*7 #total days - total of the number of weeks times 7 so the total days

    total_weekdays_full = no__weeks_left * 5 #total of week days in the full weeks
    
    if remainder_days_not_whole_week == 0:
        weekdays_misc = remainder_days_not_whole_week
    elif remainder_days_not_whole_week == 1:
        weekdays_misc = remainder_days_not_whole_week - 1
    else:
        weekdays_misc = remainder_days_not_whole_week - 2 #the weekdays not in full weeks
    
    total_weekdays_all = weekdays_misc + total_weekdays_full

    total_sessions_fulldays = total_weekdays_all * 4 #the total sessions left of the full days
    total_fullday_sessions = total_sessions_fulldays

    timeleft = datetime(today.year, today.month, int(today.day) + 1) - today #time until the day ends

    first_session_time = datetime(today.year,today.month,today.day,8,45)
    second_session_time = datetime(today.year,today.month,today.day,10,5)
    third_session_time = datetime(today.year,today.month,today.day,11,50)
    fourth_session_time = datetime(today.year,today.month,today.day,13,50)
    
    sessions_left_of_today = 0 #the number of sessions that is of today

    if today > fourth_session_time:    #if it is past the time for the fourth session
        Pass
    elif today > third_session_time: #if it has past third
        sessions_left_of_today += 1
    elif today > second_session_time:
        sessions_left_of_today += 2 
    elif today > first_session_time:
        sessions_left_of_today += 3
    elif today < first_session_time:
        sessions_left_of_today += 4
        
    if int(today.weekday()) in range(0,5): #tests if today is a weekday
        total_sessions = total_fullday_sessions + sessions_left_of_today
    else:
        total_sessions = total_fullday_sessions  #todo: plus four temp, fix

    list_diffrence = str(diffrence).split(",")
    time_list = list_diffrence[1].split(":")

    infotext = f'''
In total including weekends and holidays, there is:
{list_diffrence[0]}, 
{time_list[0]} hours, 
{time_list[1]} minutes and 
{time_list[2]} seconds until we are free

Or in school hours:
{total_sessions} school sessions left,
which is also {total_weekdays_all} school days left.

What do we suffer for? This tiny taste of freedom.
'''
    return (infotext)

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set(calc())
        self.label = tk.Label(self.root, textvariable=self.text)

        self.button = tk.Button(self.root,
                                text="Click To Update",
                                command=self.changeText, bg='gray', fg='white')
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def changeText(self):
        self.text.set(calc())

app= Test()