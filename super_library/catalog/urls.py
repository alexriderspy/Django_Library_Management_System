from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('books/',views.BookListView.as_view(),name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/',views.AuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('publishers/',views.PublisherListView.as_view(),name='publishers'),    
    path('mybooks/',views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path("register/", views.register_request, name="register"),
    path("register/success/", views.register_request_successful, name="register-success"),
    path('acceptrequests/<int:userID>&&<int:bookID>', views.process_borrow,name="process-borrow"),
    path('books/<int:pk>/sendrequest/<int:userID>/<int:bookID>/',views.send_borrow_request, name='send-request'),
    path('viewrequests/',views.ViewRequest.as_view(), name='all-requests'),

]
