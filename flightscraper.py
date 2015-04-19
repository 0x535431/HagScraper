#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the approprate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import json


html_page = "virgin_and_logan_airport.html"

def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        # page_source.html:350
        ev = soup.find()
        data["eventvalidation"] = ev["value"]
        # page_source.html
        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

        tab = soup.find(id="DataGrid1")
        print soup["DataGrid1"]

        # do something here to find the necessary values



    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_data(html_page)
    #assert data["eventvalidation"] != ""
    #assert data["eventvalidation"].startswith("/wEWog")
    #assert data["viewstate"].startswith("/wEPDwULLTE")

    
test()