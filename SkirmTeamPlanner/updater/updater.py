from lxml import html
from threading import Thread
import requests, time


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
    print "----------------Start parsing the html-----------------"
    elements = html.xpath('//h2[@class="sfitemTitle"]/span[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/text()')
    # elements = html.xpath('//*[@id="ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl"]')
    for element in elements:
        print element.encode('UTF-8')
        
    

if __name__ == "__main__":
    main()