from django.contrib import admin

# Register your models here.
from users.models import QuestionNaire


class QuestionNaireModel(admin.ModelAdmin):
    list_display = ['user','title','put_time']
    list_filter = ['user']
    search_fields = ['user']

admin.site.register(QuestionNaire,QuestionNaireModel)