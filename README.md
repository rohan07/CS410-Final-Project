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
 
 - While the server is running, in a different terminal tab, run:
 ```
  python CourseExlorerLoader.py
 ```
 and then run:
  ```
  python load_koofer_professor.py
 ```
   
  
  
