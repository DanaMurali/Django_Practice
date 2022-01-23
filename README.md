# Django_Practice
Django Tutorial 

Start django application in terminal:

mkdir tutorial
cd tutorial 
python3 -m venv venv (second venv is just name of virtual environment)
source venv/bin/activate 
pip install Django
django-admin startproject first . (first - just name of project. The space and dot means just do it in current folder)
python3 manage.py runserver

In PyCharm:

Open folder in pycharm
View -> Tool Windows -> Terminal
manage.py will fail if we just press run so we have to configure
click on downward arrow next to manage and click edit configuration
Python interpreter should be the Desktop/tutorial/venv/bin/python
We can set some parameters: “runserver"
Press run button and it will now work or type in terminal: python3 manage.py runserver
django-admin startapp demo - creates demo folder

Migrations in terminal:

python3 manage.py migrate
looking in project first then settings. You can see the installed apps.
We now have migration from this application applied to our database.
Each application has been added automatically to our project and we can use it straight away.

In models.py file in demo:
We can store some information our database. We can create some class based models.
We created a new object Book which will have a title with a max length of 36.
class Book(models.Model):
    title = models.CharField(max_length=36)
python3 manage.py makemigrations -> but no changes will be detected
so we need to go to settings and in installed apps we need to add in demo. Basically we are telling our django project we have application.
Now run python3 manage.py makemigrations
And we now have a 0001_initial.py file under migrations 
But it still hasnt been applied to database.
So we need to run “python3 manage.py migrate” again
For one column we can have title and have others etc…

User & Admin:

To see hwats in our database. We will use build in django admin view. 

http://127.0.0.1:8000/admin 

This takes us to a login page and so we shall create a user.
python3 manage.py createsuperuser
We have created a user and that has been added to database.
If you click on users after logging in you can see list of users. We don’t see our Book model and it isn’t in our admin so we have to add it in manually. 
Go to admin.py file and register our model here, “from .models import Book” and they type in “admin.site.register(Book)”


Field Options:
(everything we pass in the parentheses title = models.CharField(max_length=36))

Look at model field reference in documentation for all the different parameters that can be passes in the brckets like max_length=36
title = models.CharField(null=False). We are teling django that if this field is empty then we should start null in the database, not going to impact our validation just purely a database field.
blank=True - This means we allow this title to be blank, can create book with no title.
blank=False Booke cannot be added without title.
unique=True - title needs to be unique. Can’t add two books with the same name in the database. 
default=‘’ - this makes no sense with a null=true 
choices=BOOKS - we can create a constant - key value pairs: BOOKS = (('HB', 'Hobbit'),   ('LOTR', 'Lord of the Ring'))
choices=BOOKS
choices=STATUS
STATUS = (
    (0, 'Unknown'),
    (1, 'processed'),
    (2, 'paid')
)
choices will restrict to these choices we set up in the array.
class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
python3 manage.py makemigrations
python3 manage.py migrate  

Field Types:

class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
We are allowing description to be blank and have a max length of 256
price = models.DecimalField(default=0, decimal_places=2)
price = models.FloatField(default=0, decimal_places=2)
published = models.DateField(auto_now=True, auto_now_add=True)
auto_now=True - attach new time stamp for whichever book. This is whatever you will save this model/book and will serach for current date.
auto_now_add=True - when the book has been created.
But we don’t actually need these autos for published because it’s more for keeping track of when a record has been created. 
cover = models.FileField(upload_to='covers/')
This can save a file^
cover = models.ImageField(upload_to='covers/')
c

URLS:
in project folder first/urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
REST:

If we have data in our server we need something to communicate with our data in the front end to access data.

pip install djangorestframework
Add to settings.py in INSTALLED APPS “'rest_framework'” and then:
python3 manage.py migrate

Serializers:

Create new file in demo = serializers.py
import from rest_framework import serializers and then create class BookSerializer


Token:

Random string of secret characters. When logging in with username and password we will return a token. If the token is wrong or stale nothing will be returned.

In settings.py in project first ass to installed apps: 'rest_framework.authtoken'
python3 manage.py migrate
http://127.0.0.1:8000/auth/
{
    "detail": "Method \"GET\" not allowed."
}
This is because need to provide credentials.


Permisions:

How we can actually protect our API. How to use our token to secure application. 

in settings.py in project where ever you want add in this: REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
but now our whole project is autheticated:


Even with adding in token nothing has changed so we have to go to views in django.
from rest_framework.authentication import TokenAuthentication

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # have to pass in as a tuple
    authentication_classes = (TokenAuthentication,)
Now re run application and it should work in postman:
Now we can access all data. We have restricted people who can view the data via authorisation.c
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}
This means can still view data wihtout token auth.
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # have to pass in as a tuple so it doesn't take it as one value.
    authentication_classes = (TokenAuthentication,)
    # this overrides the settings.py where we say allow any
    permission_classes = (IsAuthenticated,)
But this overides the settings. 


