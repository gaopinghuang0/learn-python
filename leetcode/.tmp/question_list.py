#!/usr/bin/python
# question_list.py
import os
import urllib2
from bs4 import BeautifulSoup

headers = { 'User-Agent':'''Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; 
    rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6''' }  # pretend to be browser 


class QuestionList(object):
    def __init__(self, fn, url="https://leetcode.com/problemset/algorithms/"):
        self.fn = fn
        self.url = url 

    def generate_question_list(self, overwrite=False):
        if os.path.isfile(self.fn):
            print '{} already exists'.format(self.fn)
            if not overwrite:
                print 'You can set overwrite=True to overwrite'
                return
            print 'overwriting...'

        print 'fetching from {}'.format(self.url)
        req = urllib2.Request(self.url,headers=headers)  
        page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page)
        soup.prettify()
        print soup.html
        for tr in soup.html.find('tbody', attrs={'class': 'reactable-data'}).contents:
            print tr


if __name__ == "__main__":
    def main():
        fn = 'question_list.json'
        ques = QuestionList(fn)
        ques.generate_question_list()


    main()
