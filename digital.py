from tkinter import *
import datetime

def date_time():
    time= datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    lab_hr.config(text = hr)
    lab_min.config(text = mi)
    lab_sec.config(text = sec)
    lab_am.config(text = am)
    lab_hr.after(200,date_time)

    lab_date.config(text =date)
    lab_mo.config(text = month)
    lab_year.config(text=year)
    lab_day.config(text = day)
    

clock = Tk()

clock.title("****DIGITAL CLOCK****")

clock.geometry('1000x500')
clock.config(bg='black')

#hour
lab_hr = Label(clock,text ='00', font = ("Times New Roman",50,'bold'),bg = "black", fg = "white")
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_txt = Label(clock,text ='Hour', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_hr_txt.place(x=120,y=190,height=40,width=100)

#minute
lab_min= Label(clock,text ='00', font = ("Times New Roman",50,'bold'),bg = "black", fg = "white")
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_txt = Label(clock,text ='Min.', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_min_txt.place(x=340,y=190,height=40,width=100)

#second
lab_sec= Label(clock,text ='00', font = ("Times New Roman",50,'bold'),bg = "black", fg = "white")
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_txt = Label(clock,text ='Sec.', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_sec_txt.place(x=560,y=190,height=40,width=100)

#am/pm
lab_am= Label(clock,text ='00', font = ("Times New Roman",50,'bold'),bg = "black", fg = "white")
lab_am.place(x=780,y=50,height=110,width=100)
lab_am_txt = Label(clock,text ='AM/PM', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_am_txt.place(x=780,y=190,height=40,width=100)

# date
lab_date = Label(clock,text ='00', font = ("Times New Roman",50,'bold'),bg = "black", fg = "white")
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt = Label(clock,text ='Date', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_date_txt.place(x=120,y=410,height=40,width=100)

#month
lab_mo= Label(clock,text ='00', font = ("Times New Roman",50,'bold'),bg = "black", fg = "white")
lab_mo.place(x=340,y=270,height=110,width=100)
lab_mo_txt = Label(clock,text ='Month', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_mo_txt.place(x=340,y=410,height=40,width=100)

#year
lab_year= Label(clock,text ='00', font = ("Times New Roman",50,'bold'),bg = "black", fg = "white")
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt = Label(clock,text ='Year', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_year_txt.place(x=560,y=410,height=40,width=100)

#day
lab_day= Label(clock,text ='00', font = ("Times New Roman",40,'bold'),bg = "black", fg = "white")
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_txt = Label(clock,text ='day', font = ("Times New Roman",20,'bold'),bg = "white", fg = "grey")
lab_day_txt.place(x=780,y=410,height=40,width=100)


date_time()

clock.mainloop()
