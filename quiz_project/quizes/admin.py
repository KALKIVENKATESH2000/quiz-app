from django.contrib import admin
from .models import Exam
# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'option1','option2','option3','option4', 'carrans')

admin.site.register(Exam, ExamAdmin)