from django.core.management.base import BaseCommand, CommandError

from threading import Thread
from lxml import html
from datetime import datetime
import requests, time, os, logging

from updater.models import Skirm

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.month_names = {'januari':1, 'februari':2, 'maart':3, 'april':4, 'mei':5, 'juni':6, 'juli':7, 'augustus':8, 'september':9, 'oktober':10, 'november':11, 'december':12}
        page_counter = 1
        failed_url_list = []
        while page_counter < 2:
            url = "http://www.nabv.nl/evenementen/page/%d" % page_counter
            print url
            try:
                page = requests.get(url)
                tree = html.fromstring(page.content)
                thread = Thread(target=self.parse_skirms, args=(tree,))
                thread.start()
                thread.join()
            except Exception as e:
                print e
                failed_url_list.append(url)
            page_counter+=1
            time.sleep(3)
        #Start timer as to have some rate limiting. With just 9 pages the updating should be relatively fast anyway


    def parse_skirms(self, html):
        #See if we can compare the performance between getting all items matching the xpath or getting the items seperately using a counter
        titles = html.xpath('//h2[@class="sfitemTitle"]/span[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/text()')
        days = html.xpath('//div[@class="dateDay"]/span[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/text()')
        month_years = html.xpath('//div[@class="dateMonthYear"]/span[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/text()')
        cities = html.xpath('//span[@class="eventLocation"]/text()')
        links = html.xpath('//div[@class="sf_colsIn sf_1col_1in_100 listItemEvent sfitemDetails"]/a[starts-with(@id, "ctl00_sectionContent_ctl10_ctl00_ctl00_dynamicContentListView_ctrl")]/@href')
        #This can propably be done better.
        counter = 0
        for title in titles:
            title =  title.encode('UTF-8')
            day = days[counter].encode('UTF-8')
            month_year = month_years[counter].encode('UTF-8')
            city = cities[counter].encode('UTF-8').strip('Plaats: ')
            link = "http://nabv.nl/evenementen" + links[counter].encode('UTF-8').strip('..')
            skirm_date = datetime(year=int(month_year.split()[1]), month=int(self.month_names[month_year.split()[0]]), day=int(day))
            skirm = Skirm(title=title, link=link, date=skirm_date, city=city)
            skirm.save()
            counter+=1

class SkirmParser(object):
    logger = logging.getLogger('skirm_updater_log')

    def __init__(self, html):
        self.htmldata = html

    def __enter__(self):
        pass

    def __exit__(self):
        logger.error('Failed to update skirms: ' + self.htmldata)

        #Send error email to warn me
            
