from django.db import models

# Create your models here.
# we created a new object Book which will have a title with a max length of 36.
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    # creating relationships between both classes: Python reads file top to bottom.
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)
    # this OneToOneField makes it so one book can only have one isbn code.

    # we can specify how our class can be converted to string because the admin is not human readable
    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

# many to many relationship
class Author(models.Model):
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='authors')

