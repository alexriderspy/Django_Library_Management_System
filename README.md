# Recruitment_Assignment
1. Since not mentioned in specs, the password for librarian is lib1
2. For checking if password reset is working properly or not. I have created an account with account name=dummyuser1200@gmail.com, password=$dummyuser1200$ , if you login, you will be able to see the verification email and also the password reset email.

I am working on a library management system and I am completely new to django. I have finished following this tutorial https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django and more or less I have a user specific page and a librarian specific page. Librarian is a staff and has permissions(mark_as_returned, grant_request).

So, I basically want to have a borrow button on book-detail(that contains copies of books with available, maintenance and so on) page clicking on which a request to borrow a book will be sent to the librarian(who is a staff). Now he will have a list of requests which he will see when he logs in and he can accept or reject a request. Accepting will automatically update the db. Can anyone suggest what all models should I use? 
Since there is only one librarian do we need a requestlist model? 
After doing some research, I decided on the following:

From what I understand the requestlist is more of a column in our db having attributes borrower(foreign key with user), bookinstance(foreign key relation with BookInstance model(which has status,uuid), and permissions reqd='grant_or_decline_request'.
Now, do we need any more models for this purpose? How to actually design a proper flow?
Again, adding what I thought, we have this model now for the url
