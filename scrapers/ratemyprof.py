import requests
import json

r = requests.get("https://search-a.akamaihd.net/typeahead/suggest/?solrformat=true&rows=4296&q=*%3A*+AND+schoolid_s%3A1112&defType=edismax&qf=teacherfirstname_t%5E2000+teacherlastname_t%5E2000+teacherfullname_t%5E2000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=total_number_of_ratings_i+desc&siteName=rmp&rows=200&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s&fq=")

j_r = r.json()

with open('ratemyprof.json', 'w') as fp:
    json.dump(j_r, fp)

# list of dictionaries
teachers = j_r['response']['docs']

# id = "pk_id"
first_name = "teacherfirstname_t"
last_name = "teacherlastname_t"
total_ratings = "total_number_of_ratings_i"
average_rating = "averageratingscore_rf"
