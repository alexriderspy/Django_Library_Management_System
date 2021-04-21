from django.contrib import admin
from .models import Author,Book,BookInstance,Genre,Language,Publisher
# Register your models here.
#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'display_genre','language')
#admin.site.register(Author)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('book','status','due_back')
    list_filter=('status','due_back')
    fieldsets=((None,{'fields':('book','id')}),('Availability',{'fields':('status','due_back','borrower')}),)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Publisher)