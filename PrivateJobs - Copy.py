from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from timesjob_code import times_job


def find_job():
    title = d1.current()
    loc = d2.current()
    site = d3.current()
    iA0=''
    iB0=''
    iC0=''
    iD0=''
    iE0=''
    iF0=''
    
    iA1=''
    iB1=''
    iC1=''
    iD1=''
    iE1=''
    iF1=''

    iA2=''
    iB2=''
    iC2=''
    iD2=''
    iE2=''
    iF2=''

    iA3=''
    iB3=''
    iC3=''
    iD3=''
    iE3=''
    iF3=''

    iA4=''
    iB4=''
    iC4=''
    iD4=''
    iE4=''
    iF4=''

    tA0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Noida%2F+Greater+Noida'
    tB0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Pune'
    tC0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Bengaluru%2F+Bangalore'
    tD0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Gurgaon'
    tE0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Hyderabad%2F+Secunderabad'
    tF0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Cochin%2F+Kochi%2F+Ernakulam'
    
    tA1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Noida%2F+Greater+Noida'
    tB1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Pune'
    tC1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Bengaluru%2F+Bangalore'
    tD1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Gurgaon'
    tE1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Hyderabad%2F+Secunderabad'
    tF1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Cochin%2F+Kochi%2F+Ernakulam'

    tA2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Noida%2F+Greater+Noida'
    tB2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Pune'
    tC2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Bengaluru%2F+Bangalore'
    tD2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Gurgaon'
    tE2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Hyderabad%2F+Secunderabad'
    tF2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Hyderabad%2F+Secunderabad'

    tA3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Noida%2F+Greater+Noida'
    tB3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Pune'
    tC3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Bengaluru%2F+Bangalore'
    tD3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Gurgaon'
    tE3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Hyderabad%2F+Secunderabad'
    tF3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Cochin%2F+Kochi%2F+Ernakulam'

    tA4=''
    tB4=''
    tC4=''
    tD4=''
    tE4=''
    tF4=''

    sA0=''
    sB0=''
    sC0=''
    sD0=''
    sE0=''
    sF0=''
    
    sA1=''
    sB1=''
    sC1=''
    sD1=''
    sE1=''
    sF1=''

    sA2=''
    sB2=''
    sC2=''
    sD2=''
    sE2=''
    sF2=''

    sA3=''
    sB3=''
    sC3=''
    sD3=''
    sE3=''
    sF3=''

    sA4=''
    sB4=''
    sC4=''
    sD4=''
    sE4=''
    sF4=''
    
    
    timesjob=[[tA0,tB0,tC0,tD0,tE0,tF0],
              [tA1,tB1,tC1,tD1,tE1,tF1],
              [tA2,tB2,tC2,tD2,tE2,tF2],
              [tA3,tB3,tC3,tD3,tE3,tF3]]
    
    if site==1:
        l=timesjob[title]
        url=l[loc]
        
        a=times_job(url)
        a.retrive_jobs()
    
    #messagebox.showinfo("FIND JOBS",msg)

    

root=Tk(className=' Job Scrapper ')

root.geometry('500x500')



root['bg']='white'
img=PhotoImage(file="image\Logo_3.gif")
l1=Label(root,image=img,bg="white")

l2=Label(root,text="Title",bg="white",padx='2',pady='4', font = 'Helvetica 16 bold')
l3=Label(root,text="Location",bg="white",padx='2',pady='4', font = 'Helvetica 16 bold')
l4=Label(root,text="From",bg="white",padx='2',pady='4', font = 'Helvetica 16 bold')
l5=Label(root,text="Footer",bg="white",padx='2',pady='4', font = 'Helvetica 16 bold')
b1=Button(root,text="Cancel",bg="sky blue",padx='2',pady='4', font = 'Helvetica 16 bold')
b2=Button(root,text="Find Jobs",command=find_job,bg="sky blue",padx='2',pady='4', font = 'Helvetica 16 bold')
d1=ttk.Combobox(root,state="readonly",values=["Software Developer","Software Tester","Designer","Data Analyst"], font = 'Helvetica 16 bold')
d1.current(0)
d2=ttk.Combobox(root,state="readonly",values=["Noida","Pune","Bengluru","Gurgaon","Hyderabad","Kochi"], font = 'Helvetica 16 bold')
d2.current(0)
d3=ttk.Combobox(root,state="readonly",values=["indeed.com","timesjobs.com","simplyhired.com"], font = 'Helvetica 16 bold')
d3.current(0)

l1.grid(row=0,column=0,columnspan=4)


l2.grid(row=1,column=1,columnspan=2)
#l2.config(font=("Courier", 12))

d1.grid(row=1,column=3,columnspan=2)
#d1.config(font=("Courier", 12))

l3.grid(row=2,column=1,columnspan=2)
#l3.config(font=("Courier", 12))

d2.grid(row=2,column=3,columnspan=2)
#d2.config(font=("Courier", 12))

l4.grid(row=3,column=1,columnspan=2)
#l4.config(font=("Courier", 12))

d3.grid(row=3,column=3,columnspan=2)
#d3.config(font=("Courier", 12))

b1.grid(row=4,column=2)
#b1.config(font=("Courier", 12))

b2.grid(row=4,column=3)
#b2.config(font=("Courier", 12))


l5.grid(row=5,column=3)
#l5.config(font=("Courier", 22))

root.mainloop()


