from bs4 import BeautifulSoup
import requests


#page = open('firstNaukri.html', 'r').read()
#soup = BeautifulSoup(page,'html.parser')

page = requests.get("https://www.indgovtjobs.in/")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
def retrive_jobs():
    
    all_jobs = soup.find_all('div', class_='main section')
    i=0
    print("length of all_jobs : "+ str(len(all_jobs)))
    for job in all_jobs:
        
        i=i+1
        job_title = ""
        
        job_loc = ""
        job_org =  ""
        job_posted = ""
        
        if(i==5):break
        
        t = job.find('h3',class_='post-title entry-title')
        if t is not None:
            job_title = t.getText()
            
            
            t = job.find('h2',class_='date-header')
            if t is not None:
                job_posted = t.getText()
                
            t = job.find('div',class_='post-body entry-content')
            if t is not None:
                job_org = t.getText()
                
           # t = job.find('span',class_='postedOn')
            #if t is not None:
               # job_posted = t.getText()
                
            
            
            print("********************************  " , i," ********************************")
            print("\n",job_title)
            print("**********************************************************************")        
           # print("\n\t Location: ",job_loc)
            print("\n\t Posted: ",job_posted)
            print("\n\t Description: ",job_org)
    
if __name__ == '__main__':
    retrive_jobs()
