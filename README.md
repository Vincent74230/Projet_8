# Pur_beurre app
## Project 8.Vincent Nowaczyk.Openclassrooms student


Link to the app :  https://vincentnow-purbeurre.herokuapp.com/home/

How to run the app on your own computer:

Programm needs a postgresql database:
1-Create a postgresql database:
-Open a console, open psql and create a DB called 'pur_beurre_db' with user 'pur_beurre_owner'
-Give all privileges to pur_beurre_owner on pur_beurre_db.


2-Clone the app on github:
https://github.com/Vincent74230/Projet_8
All the app is license free

3-Run the app:
-First change the password of the database on `settings.py` (DATABASES={})
-Open a virtualenv and install requirements `pip3 install requirements.txt`
-Run it by typing `python manage.py runserver`
-Open the link given by your console