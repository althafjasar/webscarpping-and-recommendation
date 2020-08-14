# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:12:34 2020

@author: Jasar Althaf
"""

#importing packages
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import pandas as pd
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords



url=['https://timesofindia.indiatimes.com/home/education/news/career-in-data-science-in-india-courses-certification-salary-future-growth/articleshow/75023624.cms',
     'https://timesofindia.indiatimes.com/india/62064-more-covid-19-cases-in-india-recoveries-cross-15-lakh-mark/articleshow/77456041.cms',
     'https://timesofindia.indiatimes.com/world/pakistan/pakistan-us-review-bilateral-relationship/articleshow/77503580.cms',
     'https://timesofindia.indiatimes.com/india/as-china-factor-looms-india-hopes-to-work-with-lankas-rajapaksas-for-development/articleshow/77509553.cms',
     'https://timesofindia.indiatimes.com/sports/football/champions-league/top-stories/thousands-have-tried-bayern-munich-ponder-how-to-stop-messi/articleshow/77489723.cms']

section=['section1','clearfix rel','clearfix rel','clearfix rel','clearfix rel']


def fun(url,section):
    article = ''
    response = requests.get(url)
#initializing parser
    soup = BeautifulSoup(response.text, "html.parser")
#Fetching Div = "section1" data
    content = soup.find('div', {"class": section})
#Creating the text data
    for i in content.findAll('div'):
        article = article + ' ' +  i.text
        keywor=keywords(article).split('\n')
        summary=(summarize(article,ratio=0.25))
        return article,keywor,summary

data=[]

def funtion(url,text,key,summary):
    for i in range(0,length):
        data.append({
            'url':url[i],
            'text':text[i],
            'key':key[i],
            'summary':summary[i]})
    
    return data


length=len(url)-1

text=[]
key=[]
summary=[]



for i in range(0,length):
    tex,keyw,summa=fun(url[i],section[i])
    text.append(tex)
    key.append(keyw)
    summary.append(summa)
    
    
    
data=funtion(url,text,key,summary)


df=pd.DataFrame(data)


df.head()
