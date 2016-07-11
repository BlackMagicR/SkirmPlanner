from lxml import html
import requests


def main():
    #Here we deploy all threads that we use to scrape the html in a quick fashion
    page_counter = 1
    
    while page_counter < 10:
        url = "www.nabv.nl/evenementen/page/%d" % page_counter
        print url
        page_counter+=1
        #Start timer as to have some rate limiting. With just 9 pages the updating should be relatively fast anyway


if __name__ == "__main__":
    main()