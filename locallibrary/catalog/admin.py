from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(Language)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
class BookStackedLine(admin.StackedInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
    inlines = [BookStackedLine]
    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'summary')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'due_back', 'status')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    