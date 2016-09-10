#!/usr/bin/python
"""
Generate file for any leetcode question
Fetch the content from leetcode
"""
import sys
import re
import os
import urllib2
from bs4 import BeautifulSoup

headers = { 'User-Agent':'''Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; 
    rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6''' }  # pretend to be browser 


class QuestionContent(object):
    def __init__(self, url):
        self.url = url

    def get_content(self):
        print 'fetching from {}'.format(self.url)
        req = urllib2.Request(self.url,headers=headers)  
        page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page)
        soup.prettify()
        print soup.html


if __name__ == "__main__":
    def main():
        url = "https://leetcode.com/problems/reverse-string/"
        ques = QuestionContent(url)
        ques.get_content()
        
    main()
