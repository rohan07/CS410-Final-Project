import os
import json
import requests

def populate_database():
    headers = {'X-Auth-Token': 'e87e9db4568945ca8fce0012c69a8250'}
    f = open("../scrapers/koofers_professors.json", 'r')
    data_file1 = json.loads(f.read(), strict=False)
    f.close()

    for x in data_file1.values():
        if x['name'] == "":
            continue
        c = x['name'].split(',')
        instructor = RateMyProfessor.objects.filter(last_name=c[0].strip())
        if instructor.count() == 0 or x['rating'] == '' or x['num_ratings'] == '':
            continue
        else:
            t = instructor[0]
            t.avg_rating = x['rating']
            t.total_ratings = x['num_ratings']
           
            t.save()
            print(x['rating'], x['num_ratings'])
            print(t.last_name,t.first_name, t.avg_rating,t.total_ratings)
        # t.name = x['name']
        # t.number = x['number']
        # if x['rating'] == "":
        #      t.rating = 0.0
        # else:
        #     t.rating = float(x['rating'])
        # if x['num_ratings'] == "":
        #     t.num_ratings = 0
        # else:
        #     t.num_ratings = int(x['num_ratings'])
        # if x['gpa'] == "":
        #     t.gpa = 0.0
        # else:
        #     t.gpa = float(x['gpa'])
        # pass
        #z.save()

      
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FinalProject.settings")
    import django
    django.setup()
    from CourseExplorer.models import KooferData,CourseExplorerData, RateMyProfessor
    populate_database()
