import urllib3
urllib3.disable_warnings()
import math
import time
import datetime
import requests
from bs4 import BeautifulSoup
import dataset

#*********************PLEASE UPDATE THIS***********************
total_comments = 2433
start_urls = 'https://mygov.in/group-issue/ministry-railway-invites-suggestions-public-regarding-forthcoming-railway-budget-2016-17/'
issue = "ministry-railway-invites-suggestions-public-regarding-forthcoming-railway-budget-2016-17"
#*********************PLEASE UPDATE THIS***********************


db = dataset.connect('sqlite:///./mygov.sqlite')
db.begin()
db_comments_table = db['comments']
current_page_number = -1
comments_per_page = 10
pages =  math.ceil( float(total_comments)/10) 

try:
    print str(len(db_comments_table))
    get_comments = db.query('SELECT max(page) as max_page FROM comments where issue="'+issue+'"')
    for current in get_comments:
        current_page_number = int(current['max_page'])
        break
except Exception,e:
    print str(e)
    pass

    
print "INITIAL ----------------------------------------------------------------"
print "issue="+str(issue)
print "current_page_number="+str(current_page_number)
print "----------------------------------------------------------------"

while(current_page_number < pages):
    current_page_number = current_page_number + 1
    print "LOOP ----------------------------------------------------------------"
    print "current_page_number="+str(current_page_number)
    print "----------------------------------------------------------------"

    user_agent = {'User-agent': 'Mozilla/5.0'}
    params = "?field_hashtags_tid=&sort_by=created&sort_order=DESC&page=0%2C"+str(current_page_number)
    url = start_urls+params
    html_get_src = requests.get(url, headers = user_agent,verify=False)
    soup = BeautifulSoup(html_get_src.content)
    comments_div = soup.find_all("div", class_="comment_content")
    for comment in comments_div:
        insert_data = {}
        username  = comment.find("span", class_="username").contents[0]
        date_time = comment.find("span", class_="date_time").contents[0]
        comment_body  = ""
        content = comment.find("div", class_="comment_body")
        comment_body = unicode(content.get_text())
        insert_data = dict({"page":current_page_number , "comment":comment_body, "username":username, "date_time":date_time, "url":url, "issue":issue })
        print str(insert_data)
        db_comments_table.insert(insert_data)
    db.commit()
    print "Waiting"
    print datetime.datetime.now()
    time.sleep(5)
