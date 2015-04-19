
from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        # page_source.html:350
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]
        # page_source.html
        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

        # do something here to find the necessary values


    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r

def request_extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}

    r = s.get(page)
    soup = BeautifulSoup(r.text)

    ev = soup.find(id="__EVENTVALIDATION")
    data["eventvalidation"] = ev["value"]

    vs = soup.find(id="__VIEWSTATE")
    data["viewstate"] = vs["value"]


        # do something here to find the necessary values


    return data

def test():

    # data = extract_data(html_page)
    data = request_extract_data("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
    r = make_request(data)
    f = open("virgin_and_logan_airport.html", "w")
    f.write(r.text)
    soup = BeautifulSoup(r.text)




s = requests.Session()
test()