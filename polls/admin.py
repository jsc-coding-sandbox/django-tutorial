from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
            ]
    # Present the option to add choices when creating a question
    inlines = [ChoiceInline]
    # Display a proper table with question text, date published, etc
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Add filter by date published
    list_filter = ['pub_date']
    # Add search by question text
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
