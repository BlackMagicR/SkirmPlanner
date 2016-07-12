from lxml import html
from threading import Thread
import requests, time


def main():
    #Here we deploy all threads that we use to scrape the html in a quick fashion
    page_counter = 1
    failed_url_list = []
    while page_counter < 10:
        url = "http://www.nabv.nl/evenementen/page/%d" % page_counter
        print url
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
            print tree
            print "Starting thread"
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
    print "Start parsing the html"
    print html.xpath('//*[@id="ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl0_Label1"]/text()')

if __name__ == "__main__":
    main()