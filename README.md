# bookr_django
I am reading the textbook **'Web Development with Django'** by Ben Shaw, Saurabh Badhwar, Andrew Bird, Bharath Chandra K S and Chris Guest. Following along with the book, you create the bookr app and I am currently on Chapter 4, page 190.

I am trying to make a custom Admin site for the app but I'm running into complications. Since this is my first time using Django it's confusing.

## I keep getting an error on Pycharm that says:
**"django.core.exceptions.ImproperlyConfigured: Application labels aren't unique, duplicates: admin"**

In effort to debug the issue, I commented out everything in the admin.py, apps.py and reverting everything back to the original admin site values, I still get the same error.
I checked my settings.py file in the INSTALLED_APPS list and there is no second admin.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reviews'
]
```

I've been trying every suggestion I see online for 2 days but so far I've had no success making this work.


I keep running into these issues as well, but I want to figure out what dumb mistake I'm doing for the django.core.exceptions issue.

- https://github.com/PacktPublishing/Web-Development-with-Django/issues/5

- https://github.com/PacktPublishing/Web-Development-with-Django/issues/11
