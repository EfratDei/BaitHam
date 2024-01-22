# BaitHam


#### Authors: 

* Afik Danan - afikda@ac.sce.ac.il
* Topaz Aakal – topazaa@ac.sce.ac.il
* Avigail Shekasta - avigash@ac.sce.ac.il
* Daniel Diei - Danieha6@ac.sce.ac.il

#### Description:

The project is part of a "Fundamentals in Software Engineering" course. 
We are group #33.
This is a website for an animal shelter. 

The website have three users: 
* Adopter - the regular user, anonymous user. 
This user can read articles and upload his success story with his adopted animal, donate to the shelter, view the animals available for adoption, and adopt an animal.
In addition, he can report an abandoned animal or animal abuse, export reports from the system (like how many animals are in the shelter, the association's income from donations and more), get information about upcoming events and ask questions in the forum.

* Volunteer - the staff at the shelter. he have more permissions compared to the adopters.
The staff can see all the pages like the adopter but can do more things. 
The Volunteer needs to log in to his account in order to use the permissions he has.
He can add / edit / delete an animal to / from the database. 
also, the volunteer has a Taskboard on the site that he can see all the "to-do tasks" and assign himself for a task. 
he can download all kinds of useful reports to his computer and report his monthly attendance.
Besides that, he can respond in the forum to questions asked by the adopters, and his other job is to respond to reports received from the field (about abuse or abandonment).

* Manager- the manager of the shelter is the person with all the permissions, he create users in the database (the volunteer users), he can export all the reports, view everything and control the database, edit objects, create objects and delete them.
The manager adds new tasks to the Taskboard, and the volunteers can assign themselves.

#### Environment:
  the code was devloped on pycharm, the framework is django 4.0.0, most of the code is python, but we have some html and css code.
  Database: SQlite3 
  
#### How to run:

```
git clone https://github.com/BaitHam-33/BaitHam.git
 ```
#### Requirements:
```
pip install asgiref==3.4.1  
pip install Django==4.0    
pip install django-filter==21.1   
pip install Pillow==8.4.0  
pip install pip==21.3.1 
pip install reportlab==3.6.3  
pip install sqlparse==0.4.2
pip install tzdata==2021.5
pip install xlwt==1.3.0
```

#### Create tables
```
 python manage.py makemigrations
 python manage.py migrate
```

#### Start the application (development)
 ```
 python manage.py runserver
```

 #### Access the web app in browser: http://127.0.0.1:8000/
 #### Access the web site: https://bait-ham.herokuapp.com/

 
# Unit Test
```
python manage.py test                # all tests
python manage.py test Animal         # Animal test
python manage.py test Article        # Article test
python manage.py test Donations      # Donations test
python manage.py test Event          # Event test
python manage.py test forum          # forum test
python manage.py test Report         # Report test
python manage.py test success_story  # success_story test
python manage.py test Taskboard      # Taskboard test
python manage.py test volunteer      # volunteer test
      
```
