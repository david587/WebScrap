from bs4 import BeautifulSoup
import requests
import time

print("Put some skill that you are not familiar with")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
    html_text = requests.get("url").text  #html_text->html code
    soup = BeautifulSoup(html_text,"lxml")
    jobs = soup.find_all("li", class_="clarfix job-bx wht-shd-bx")

    for index,job in enumerate(jobs):
        published_date = job.find_all("span", class_="sim-posted").span.text
        if "few" in published_date:
            company_name = job.find_all("h3", class_="joblist-comp-name").text.replace(" ","")
            skills = job.find_all("span", class_="srp_skills").text.replace(" ","")
            #poston belül a header tag, azon belül h2 azon belül a
            more_info =job.header.h2.a["href"]
            if unfamiliar_skill not in skills:
                #we want the date in he notes
                with open(f"posts/{index}.txt","w") as f:
                    #we can get rid of spaces with strip()
                    f.write(f"Company name:{company_name.strip()} \n")
                    f.write(f"Required skills:{skills.strip()} \n")
                    f.write(f"More info:{more_info} \n")
                print(f"File saved:{index}")
#unfamiliar
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait=10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)

#we can execute our file:
#-set to mechanize directroy
#python WebScrap.py







    