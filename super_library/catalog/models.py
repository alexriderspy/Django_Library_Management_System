from django.db import models
from django.urls import reverse
import uuid
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date

class Borrow_Request(models.Model):
    from_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="from_user")
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="to_user")
    book_id=models.ForeignKey('BookInstance',on_delete=models.CASCADE,related_name="bookinst")

    class Meta:
       # ordering=['self.bookinst.due_back']
        permissions = (("can_grant_decline_request", "Grant or decline a Request"),)

    def __str__(self):
        return f'{self.borrower.username}({self.book_id.book.title})'
    def get_absolute_url(self):
        return reverse('borrow-detail', args=[str(self.id)]) 

class Genre(models.Model):
    name=models.CharField(max_length=200, help_text='Enter a book genre(eg literature)')
    def __str__(self):
        return self.name

class Book(models.Model):
    #id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    language=models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    summary=models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn=models.CharField('ISBN', max_length=13, unique=True, help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre=models.ManyToManyField(Genre, help_text='Select a genre for this book')
    publisher=models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)]) 
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description='Genre'

    
class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    book=models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
   # imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True, blank=True)
    borrower=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    @property
    def is_overdue(self):
        if self.due_back and date.today()>self.due_back:
            return True
        return False
    
    LOAN_STATUS=(
        ('m','Maintenance'),
        ('o','on loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status=models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability',
    )
    class Meta:
        ordering=['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)
    def __str__(self):
        return f'{self.id}({self.book.title})'

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    thesis=models.TextField(max_length=200, null=True)
    last_accessed=models.DateTimeField(null=True)

    class Meta:
        ordering=['last_name','first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Language(models.Model):
    name=models.CharField(max_length=200, help_text="Enter book's natural language")
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=60)
    website=models.URLField()

    class Meta:
        ordering=["-name"]
    def __str__(self):
        return self.name
