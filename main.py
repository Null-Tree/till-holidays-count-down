from datetime import datetime
import tkinter as tk


def calc():
    term_end = datetime(2021, 12, 10, 15, 20) #last week was optinal
    date_end = datetime(2021, 12, 11)
    today = datetime.now()
    str_today = str(today)
    two_today = str_today.split(' ')
    dmy = two_today[0].split('-')
    t = two_today[1].split(':')
    diffrence = term_end - datetime.now()
    total_hourly_diffrence = str(diffrence).split(', ')[1].split(':')

    session_total = 0

    dif = date_end - today
    dayss = dif.days
    remainder = dayss - ((dayss // 7) * 7)
    weeks = dayss // 7
    week_s = weeks * 20
    session_total += week_s
    session_total += remainder * 4

    hour, minute = today.hour, today.minute

    if hour < 8:
        session_total += 4
    elif hour == 8 and minute <= 45:
        session_total += 4

    elif hour < 10:
        session_total += 3
    elif hour == 10 and minute <= 5:
        session_total += 3

    elif hour < 11:
        session_total += 2
    elif hour == 11 and minute <= 50:
        session_total += 2

    elif hour < 13:
        session_total += 1
    elif hour == 13 and minute <= 50:
        session_total += 1

    infotext = f'''
In total including weekends and holidays, there is:
{diffrence.days} days, 
{total_hourly_diffrence[0]} hours, 
{total_hourly_diffrence[1]} minutes and 
{total_hourly_diffrence[2]} seconds until we are free

Or in school hours:
{session_total} school sessions left,
which is also {remainder + (weeks * 5)} school days left.

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




