# Recruitment_Assignment
1. Since not mentioned in specs, the password for librarian is lib1
2. For checking if password reset is working properly or not. I have created an account with account name=dummyuser1200@gmail.com, password=$dummyuser1200$ , if you login, you will be able to see the verification email and also the password reset email.

Journey with Django
Started on 18/4/2021, completely a novice. read the docs and watched the tutorial suggested. First few videos were enough to get me going. Worked non stop for 3 days.
Django is a framework that links frontend(html,css,js) with backend(sqlite database) and is indeed an ideal partner for making dreams of webapp come true. I really hope to work with this superb framework and make my web-dev dreams come true.
Library Management System: Basically, Django has an admin interface and I gave certain permissions to librarian user. New users can register and old users can login. The basic workflow is pretty simple: we create a model, we define a url for the page we wish to direct the user to, we add a view that will call that url, finally we add a template which shows the page we want the user to view when they click on that url. Amazing isn't it? Just we need to make sure to python manage.py makemigrations, python manage.py migrate, every time to ensure the changes in our models are updated to the database. Now if we want our user to fill a form, we can use default forms for registration but for borrowing books I made a button that appears beside the book copy that is marked as available and clicking on which, sends our request to the librarian who will accept or reject the request. If he/she accepts the request , database will be updated. 
This is my plan basically. 
Also I love designing so in the mean time, as I was developing this backend system, I also looked up a huge number of websites (which you can find enlisted in my part2 repo) and designed few beautiful pages. My journey with Figma is in readme of part2. :)

And lastly, I would like to add that I love backend + design so choosing one over the other as a preference is really difficult. But come what may, I will definitely give in my best to achieve my goal.
