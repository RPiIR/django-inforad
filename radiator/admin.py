from django.contrib import admin

# Register your models here.
from radiator.models import Publisher, Author, Book, BrokenStatus, Question, Choice

admin.site.register(BrokenStatus)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)



