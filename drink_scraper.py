#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the approprate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function

from pymongo import MongoClient

from bs4 import BeautifulSoup
import requests
post = {}
html_page = "drink.html"
import datetime


def extract_data(page):
    data = []
    html = requests.post("http://www.hagkaup.is/vorur/matvara/drykkir/gosdrykkir")
    #html = open(page, "r")
    soup = BeautifulSoup(html.text)

    item = soup.findAll("div", {"class":"item"})
    for i, x in enumerate(item):
        '''print (i, x)
        print (type(x), i)
        print "\n\n"'''
        post = {"store": "hagkaup",
                "title": x['title'],
                "data-prid": x['data-prid'],
                "price": (x.b.string),
                "tags": ["matvara", "drykkir", "gosdrykkir"],
                "vnr":(x.a['href']),
                "date": datetime.datetime.utcnow(),
                }
        # print ("TITLE: ",x['title']) # TITLE FIXED
        # print ("DATA-PRID: ", x['data-prid'])
        # print ("DIV CLASS: ", x['class'])
        # print ("THE PRICE: ", (x.b.string))
        # print ("vnr: ", (x.a['href']))
        # print ("image: ", (x.i['style'].replace("background-image: url(\"", "").replace("\");", "")))
        # print x.getText()
        # print "\n\n"
        print post
        data.append(post)

        # page_source.html:350
        '''
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]
        # page_source.html
        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

        tab = soup.find(id="DataGrid1")
        print soup["DataGrid1"]
        '''
        # do something here to find the necessary values



    return data


def make_request(data):
    r = requests.post("http://www.hagkaup.is/vorur/matvara/drykkir/gosdrykkir")

    return r.text


def test():
    data = extract_data(html_page)
    client = MongoClient('localhost', 27017)
    db = client['hagkaup']
    collection = db['gosdrykkir']
    for x in data:
        post_id = collection.insert_one(x).inserted_id
        print post_id
    '''assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEWog")
    assert data["viewstate"].startswith("/wEPDwULLTE")
    '''
    
test()