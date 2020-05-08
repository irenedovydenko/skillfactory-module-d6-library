from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release',
              'author', 'price', 'copy_count', 'pub', 'hold_by', 'image')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pub_title', 'pub_description',)


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass