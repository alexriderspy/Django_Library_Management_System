from django.shortcuts import render, get_object_or_404,redirect
from catalog.models import Book, BookInstance, Genre, Author, Publisher,Borrow_Request,User
from django.views import generic
from django.utils import timezone
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import login,authenticate
from django.contrib import messages
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from catalog.forms import GrantRequestForm

@login_required
def send_borrow_request(request, userID, bookID):
    from_user=request.user
    to_user =User.objects.get(id=userID)
    book_id=BookInstance.objects.get(id=bookID)
    borrow_request, created= Borrow_Request.objects.get_or_create(from_user=from_user, to_user=to_user, book_id=book_id)
    if created:
        return HttpResponse('borrow request sent')
    else:
        return HttpResponse('borrow request was already sent')

@login_required
@permission_required('catalog.can_grant_decline_request')        
def process_borrow(request,pk):
    book_instance=get_object_or_404(BookInstance,pk=pk)
    
    if request.method == 'POST':
        data={'bookinstpk':book_instance.id}
        form = GrantRequestForm(request.POST, initial=data)
        
        if form.is_valid():
            
            book_instance.status__exact='o'
            book_instance.due_back=datetime.date.today() + datetime.timedelta(days=7)
            book_instance.borrower=form.cleaned_data['name']
            book_instance.save()
            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        form=GrantRequestForm()
    context={
        'form':form, 
        'book_instance':book_instance,
        'borrower':book_instance.borrower,
    }
    return render(request,'catalog/process_borrow.html',context)

class ViewRequest(PermissionRequiredMixin,generic.ListView):
    model=Borrow_Request
    template_name='catalog/all_requests.html'
    paginate_by =3
    permission_required = 'catalog.can_mark_returned'
    def get_queryset(self):
        return Borrow_Request.objects.all()
    
def register_request_successful(request):
    return render(request,'catalog/register_success.html')

def register_request(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            messages.success(request,"Successful")
            return redirect("success/")
        messages.error(request,"Unsuccessful")
    else:
        form=UserCreationForm() #to re-empty all fields
    return render(request=request, template_name="catalog/register.html", context={"register_form":form})

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model=BookInstance
    template_name='catalog/bookinstance_list_borrowed_user.html'
    paginate_by=10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):

    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    num_books_Introduction=Book.objects.filter(title__startswith='Introduction').count()
    num_visits=request.session.get('num_visits',1)
    request.session['num_visits']=num_visits+1

    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'startswith':num_books_Introduction,
        'num_visits':num_visits
    }
    return render(request,'index.html',context=context)

class BookListView(generic.ListView):
    model=Book
    paginate_by=4

    def get_queryset(self):
 #       return Book.objects.filter(title__icontains='Introduction')[:3]
        return Book.objects.all()
    def get_context_data(self, **kwargs):
        context=super(BookListView, self).get_context_data(**kwargs)
        context['some_data']='This is some data'
        return context

class PublisherListView(generic.ListView):
    model=Publisher
    paginate_by=4

def publisher_detail_view(request, primary_key):
    publisher=get_object_or_404(Publisher, pk=primary_key)
    return render(request, 'catalog/publisher_detail.html', context={'publisher':publisher})

class AuthorListView(generic.ListView):
    model=Author
    paginate_by=4

class AuthorDetailView(generic.DetailView):
    queryset=Author.objects.all()
    def get_object(self):
        obj=super().get_object()
        obj.last_accessed=timezone.now()
        obj.save()
        return obj

class BookDetailView(generic.DetailView):
    model=Book