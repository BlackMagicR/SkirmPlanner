from threading import Thread
from lxml import html
import requests, time, os


def main():
    #Here we deploy all threads that we use to scrape the html in a quick fashion
    page_counter = 1
    failed_url_list = []
    while page_counter < 2:
        url = "http://www.nabv.nl/evenementen/page/%d" % page_counter
        print url
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            thread = Thread(target=parse_skirms, args=(tree,))
            thread.start()
            thread.join()
        except Exception as e:
            print e
            failed_url_list.append(url)
        page_counter+=1
        time.sleep(3)
       #Start timer as to have some rate limiting. With just 9 pages the updating should be relatively fast anyway


def parse_skirms(html):
    #See if we can compare the performance between getting all items matching the xpath or getting the items seperately using a counter
    print "----------------Start parsing the html-----------------"
    titles = html.xpath('//h2[@class="sfitemTitle"]/span[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/text()')
    days = html.xpath('//div[@class="dateDay"]/span[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/text()')
    month_year = html.xpath('//div[@class="dateMonthYear"]/span[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/text()')
    city = html.xpath('//span[@class="eventLocation"]/text()')
    #This can propably be done better.
    counter = 0
    for title in titles:
        print title.encode('UTF-8')
        print days[counter].encode('UTF-8')
        print month_year[counter].encode('UTF-8')
        print city[counter].encode('UTF-8')
        counter+=1
        
    

if __name__ == "__main__":
    #I still need to add a context manager with Error email to make sure I get an email when the format is no longer working
    main()