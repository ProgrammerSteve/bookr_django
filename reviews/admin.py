from django.contrib import admin
from reviews.models import Publisher, Contributor, \
    Book, BookContributor, Review


admin.site.title_header = 'Bookr Admin'
admin.site.site_header = 'Bookr administration'
admin.site.index_title = 'Bookr site admin'

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
