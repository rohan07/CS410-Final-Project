import requests
from bs4 import BeautifulSoup
import re
import json

course_info = {}
# get course info
for pg in range(1,170):
    page = requests.get('https://www.koofers.com/university-of-illinois-urbana-champaign-uiuc/browse?p={}'.format(pg), "html-parser")
    data = page.text
    soup = BeautifulSoup(data)

    classes = soup.findAll("div", {"onclick" : re.compile("document.location = '/university-of-illinois-urbana.*?")})
    i = 0
    for c in classes:

        if c.text == "(adsbygoogle = window.adsbygoogle || []).push({});":
            continue

        name = c.find("div", {"class": "title"})
        if name:
            name = name.text.strip()
        else:
            name = ""

        number = c.find("div", {"class":"bubble_text"})
        if number:
            number = number.text.strip()
        else:
            number = ""

        rating = c.find("div", {"class": "rating"})
        if rating:
            rating = rating.text.strip()
        else:
            rating = ""

        num_ratings = c.find("div", {"class": "rating_link"})
        if num_ratings:
            num_ratings = num_ratings.text.strip()[:-8]
        else:
            num_ratings = ""

        gpa = c.find("span", {"class": "value"})
        if gpa:
            gpa = gpa.text.strip()
        else:
            gpa = ""

        # course_info[number]
        course_info["{}-{}".format(pg,i)] = {"name":name, "number":number, "rating":rating, "num_ratings":num_ratings, "gpa":gpa}
        i += 1

    if pg%10 == 0:
        print("On page {}".format(pg))


print("Number of classes found: {}".format(len(course_info)))

with open('koofers_courses.json', 'w') as fp:
    json.dump(course_info, fp)


professor_info = {}
# get professor info
for pg in range(1,170):
    page = requests.get('https://www.koofers.com/university-of-illinois-urbana-champaign-uiuc/professors?p={}'.format(pg), "html-parser")
    data = page.text
    soup = BeautifulSoup(data)

    profs = soup.findAll("div", {"onclick" : re.compile("go.*?")})

    i = 0
    for c in profs:

        if c.text == "(adsbygoogle = window.adsbygoogle || []).push({});":
            continue

        name = c.find("div", {"class": "title"})
        if name:
            name = name.text.strip()
        else:
            name = ""

        rating = c.find("div", {"class": "rating"})
        if rating:
            rating = rating.text.strip()
        else:
            rating = ""

        num_ratings = c.find("div", {"class": "rating_link"})
        if num_ratings:
            num_ratings = num_ratings.text.strip()[:-8]
        else:
            num_ratings = ""

        gpa = c.find("span", {"class": "value"})
        if gpa:
            gpa = gpa.text.strip()
        else:
            gpa = ""

        # professor_info[name]
        professor_info[ "{}-{}".format(pg,i)] = {"name": name, "rating":rating, "num_ratings":num_ratings, "gpa":gpa}
        i += 1

    if pg%10 == 0:
        print("On page {}".format(pg))


print("Number of professors found: {}".format(len(professor_info)))

with open('koofers_professors.json', 'w') as fp:
    json.dump(professor_info, fp)
