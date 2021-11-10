from datetime import datetime
import tkinter as tk


term_end = datetime(2021, 12, 17, 15, 30)
date_end = datetime(2021, 12, 18)
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

if hour <= 8 and minute <= 45:
    session_total += 4
elif hour <= 10 and minute <= 5:
    session_total += 3
elif hour <= 11 and minute <= 50:
    session_total += 2
elif hour <= 1 and minute <= 50:
    session_total += 1


root = tk.Tk()

canvas1 = tk.Canvas(root, width=555, height=300)
canvas1.pack()

label1 = tk.Label(root, text=f'''
In total including weekends and holidays, there is:
{diffrence.days} days, 
{total_hourly_diffrence[0]} hours, 
{total_hourly_diffrence[1]} minutes and 
{total_hourly_diffrence[2]} seconds until we are free

Or in school hours:
{session_total} school sessions left,
which is also {remainder+(weeks*5)} school days left.

What do we suffer for? This tiny taste of freedom.
''', fg='green', font=('helvetica', 12, 'bold'))
canvas1.create_window(277, 150, window=label1)

label2 = tk.Label(root, text='Should be right, otherwise I am dumb ---> [            ]#9778', fg='green', font=('helvetica', 6, 'bold'))
canvas1.create_window(277, 266, window=label2)

root.mainloop()
