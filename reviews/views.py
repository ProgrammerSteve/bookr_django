from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Review
from .utils import average_rating


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({
            'book': book,
            'book_rating': book_rating,
            'number_of_reviews': number_of_reviews
        })
    context = {
        'book_list': book_list
    }
    return render(request, 'books_list.html', context)




def index(request):
    name = "world"
    return render(request, 'base.html', {'name': name})


def search(request):
    book = "Web Development with Django"
    return render(request, 'search.html', {'book': book})


def welcome_view(request):
    return render(request, 'base.html')


def example_view(request):
    return render(request, 'example.html')


def book_details(request, pk_num):
    book = get_object_or_404(Book, pk=pk_num)
    title = book.title
    publisher = book.publisher
    pub_date = book.publication_date
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        number_of_reviews = len(reviews)
        reviews_creation_date = [review.date_created for review in reviews]
        reviews_edit_date = [review.date_edited for review in reviews]
        reviews_creators = [review.creator for review in reviews]
    else:
        book_rating = None
        number_of_reviews = 0
        reviews_creation_date = []
        reviews_edit_date = []
        reviews_creators = []
    context = {
        'Book': title,
        'publisher': publisher,
        'publication_date': pub_date,
        'reviews': reviews,
        'rating': book_rating,
        'number_of_reviews': number_of_reviews,
        'reviews_creation_date': reviews_creation_date,
        'reviews_edit_date': reviews_edit_date,
        'reviews_creators': reviews_creators,
    }
    return render(request, 'book_details.html', context)


def book_details_reviews(request, pk_num):
    book = get_object_or_404(Book, pk=pk_num)
    title = book.title
    publisher = book.publisher
    pub_date = book.publication_date
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        number_of_reviews = len(reviews)
        reviews_creation_date = [review.date_created for review in reviews]
        reviews_edit_date = [review.date_edited for review in reviews]
        reviews_creators = [review.creator for review in reviews]
    else:
        book_rating = None
        number_of_reviews = 0
        reviews_creation_date = []
        reviews_edit_date = []
        reviews_creators = []
    context = {
        'Book_id': pk_num,
        'Book': title,
        'publisher': publisher,
        'publication_date': pub_date,
        'reviews': reviews,
        'rating': book_rating,
        'number_of_reviews': number_of_reviews,
        'reviews_creation_date': reviews_creation_date,
        'reviews_edit_date': reviews_edit_date,
        'reviews_creators': reviews_creators,
    }
    return render(request, 'book_details_reviews.html', context)
