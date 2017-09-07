from django.contrib import admin
from choices.models import MyQuestion,MyChoice,MyText,Content,AnserTime
# Register your models here.


class MyQuestionModel(admin.ModelAdmin):
    list_display = ['question','name','add_time','type','orde']
    list_filter = ['question']
    search_fields = ['name']


class MyChoiceModel(admin.ModelAdmin):
    list_display = ['question', 'name', 'add_time','num']
    list_filter = ['question']
    search_fields = ['name']


class MyTextModel(admin.ModelAdmin):
    list_display = ['question', 'name', 'add_time']
    list_filter = ['question']
    search_fields = ['name']


class ContentModel(admin.ModelAdmin):
    list_display = ['mytext', 'name', 'add_time']
    list_filter = ['mytext']

class AnserTimeModel(admin.ModelAdmin):
    list_display = ['question', 'anser_time']
    list_filter = ['question']

admin.site.register(MyText, MyTextModel)
admin.site.register(MyChoice, MyChoiceModel)
admin.site.register(MyQuestion,MyQuestionModel)
admin.site.register(Content,ContentModel)
admin.site.register(AnserTime,AnserTimeModel)