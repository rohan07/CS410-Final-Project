import os
import json
import requests

def populate_database():
    headers = {'X-Auth-Token': 'e87e9db4568945ca8fce0012c69a8250'}
    f = open("../scrapers/result.json", 'r')
    data_file1 = json.loads(f.read(), strict=False)
    f.close()

    for x in data_file1:
        t = CourseExplorerData()
        t.number = x['dept'] + " " + x['num']
        t.name = x['title']
        t.description = x['description']
        t.save()
        if x['instructors'] == "":
            continue
        else:
            for y in x['instructors']:
                if y == "":
                    continue
                z = RateMyProfessor()
                z.instructor = t
                c = y.split(",")
                print(c)
                z.last_name = c[0]
                z.first_name = c[1]
                print(z.first_name)
                print(z.last_name)

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
        z.save()

      
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FinalProject.settings")
    import django
    django.setup()
    from CourseExplorer.models import KooferData,CourseExplorerData, RateMyProfessor
    populate_database()
