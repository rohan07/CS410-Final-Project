Steps to install the application:

- Clone the repository
- Set up a virtual enviroment or you can use the one we have provided. 
- Install dependencies using 
  ```
   pip install -r requirements.txt
  ```
 
 - Inside the FinalProject directory, run:
 ```
  python manage.py makemigrations && python manage.migrate
 ```
 
 - Run the server using
 ```
  python manage.py runserver
 ```
 
 -If you want to use your own database, run the following commands, while the server is running, in a different terminal tab, run:
 ```
  python CourseExlorerLoader.py
 ```
 and then run:
  ```
  python load_koofer_professor.py
 ```
 
 - You can also just use the database we committed - db.sqlite3 if you run into any errors. 
 

 You can run the server - 
 ```
 python manage.py runsever
 ```
  
 The urls are defined in urls.py in the folder FinalProject/CourseExplorer 


 # Implementation:
 models.py - Definition of our data tables 
 views.py - controller logic
 urls.py - mapping from view to templates 
 templates/ - Templates for the appllication
 base.py - application settings.  
  

# Contribution:

  Rohan - Developed the application
  Genevieve - Implemented the scrapers
  Will - Finished the testing and helped in developing the application
