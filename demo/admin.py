from django.contrib import admin
from .models import Book, BookNumber, Character


# Register your models here.

# this is very generic:
# admin.site.register(Book)

# can use decorator:

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # can decide which fields can be displayed in django
    # fields = ['title', 'description']
    # this shows the price next to the title:
    list_display = ['title', 'price']
    # we can also filter:
    list_filter = ['published']
    search_fields = ['title']
    # search_fields = ['title', 'description'] - can also search by title and description

# we have to register our new model:
admin.site.register(BookNumber)
admin.site.register(Character)